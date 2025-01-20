# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Calculadora Básica ---")
    print("Selecciona la operación que deseas realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")
    return opcion

# Función para realizar la operación solicitada
def calcular(opcion):
    if opcion == "1":
        # Sumar
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")

    elif opcion == "2":
        # Restar
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")

    elif opcion == "3":
        # Multiplicar
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")

    elif opcion == "4":
        # Dividir
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    
    elif opcion == "5":
        # Salir
        print("¡Hasta luego!")
        return False

    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")
    
    return True

def main():
    while True:
        opcion = mostrar_menu()
        if not calcular(opcion):
            break

if __name__ == "__main__":
    main()
