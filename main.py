from task_manager import TaskManager
def print_menu():
    print("\n--- Gestor de Tareas Inteligente---")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():

    manager = TaskManager()
    
    while True:

        print_menu()

        try:

            choice = int(input("Seleccione una opción: "))

            match choice:
                case 1:
                    description = input("Ingrese la descripción de la tarea: ")
                    manager.add_task(description)
                case 2:
                    manager.list_tasks()
                case 3:
                    id = int(input("Ingrese el ID de la tarea a completar: "))
                    manager.complete_task(id)
                case 4:
                    id = int(input("Ingrese el ID de la tarea a eliminar: "))
                    manager.delete_task(id)
                case 5:
                    print("Saliendo del gestor de tareas. ¡Hasta luego!")
                    break
                case _:
                    print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")
if __name__ == "__main__":
    main()

