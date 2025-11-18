import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):

    if not client.api_key:
        return ["Error: La API key de OpenAI no está configurada."]
    
    try:
        prompt = f"""Desglosa la siguiente tarea compleja en una lista de 3 tareas simples y accionables

        Tarea: {description}
        Foramto de respuesta:
        1. Subtarea 1
        2. Subtarea 2
        3. Subtarea 3
        etc.
    
        Responde solo con la lista de subtareas, una por linea empezando cada línea con un guión."""

        params = {
            "model": "gpt-5",
            "messages": [
                {"role": "system", "content": "Eres un asistente experto en gestión de tareas que ayuda a dividir tareas complejas en pasos simples y accionables."},
                {"role": "user", "content": prompt}
            ],
            "max_completion_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal"
        }

        response = client.chat.completions.create(**params)
        content= response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: No se pudieron generar subtareas."] 
    except Exception as e:
        return [f"Error: No se pudo conectar con OpenAI. {str(e)}"]
