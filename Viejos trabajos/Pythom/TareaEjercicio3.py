while True:
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        operacion = input("Introduce la operación a realizar (+, -, *, /): ")
        if operacion == "+":
            resultado = numero1 + numero2
            print(f"El resultado de {numero1} + {numero2} es: {resultado}")
        elif operacion == "-":
            resultado = numero1 - numero2
            print(f"El resultado de {numero1} - {numero2} es: {resultado}")
        elif operacion == "*":
            resultado = numero1 * numero2
            print(f"El resultado de {numero1} * {numero2} es: {resultado}")
        elif operacion == "/":
            if numero2 != 0:
                resultado = numero1 / numero2
                print(f"El resultado de {numero1} / {numero2} es: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
        break
    except ValueError:
        print("Error: Debes ingresar números válidos.")