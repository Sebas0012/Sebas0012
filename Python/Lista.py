import os

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Guardar y salir")
    opcion = input("Seleccione una opción (1-5): ")
    return opcion

# Función para cargar las tareas desde un archivo
def cargar_tareas():
    if os.path.exists("tareas.txt"):
        with open("tareas.txt", "r") as file:
            tareas = file.readlines()
        return [tarea.strip() for tarea in tareas]
    return []

# Función para guardar las tareas en un archivo
def guardar_tareas(tareas):
    with open("tareas.txt", "w") as file:
        for tarea in tareas:
            file.write(tarea + "\n")

# Función para agregar una tarea
def agregar_tarea(tareas):
    tarea = input("Ingrese la descripción de la nueva tarea: ")
    tareas.append(tarea)

# Función para marcar una tarea como completada
def marcar_completada(tareas):
    mostrar_tareas(tareas)
    try:
        tarea_numero = int(input("Ingrese el número de la tarea a marcar como completada: "))
        if 1 <= tarea_numero <= len(tareas):
            tareas[tarea_numero - 1] += " (Completada)"
            print("Tarea completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor ingrese un número válido.")

# Función para eliminar una tarea
def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        tarea_numero = int(input("Ingrese el número de la tarea a eliminar: "))
        if 1 <= tarea_numero <= len(tareas):
            del tareas[tarea_numero - 1]
            print("Tarea eliminada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor ingrese un número válido.")

# Función para mostrar todas las tareas
def mostrar_tareas(tareas):
    if tareas:
        print("\n--- Lista de Tareas ---")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas en la lista.")

def main():
    tareas = cargar_tareas()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            guardar_tareas(tareas)
            print("Tareas guardadas. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, por favor elija nuevamente.")

if __name__ == "__main__":
    main()
