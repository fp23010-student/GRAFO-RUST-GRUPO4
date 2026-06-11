while True:
    try:
        numero = float(input("Introduce un número positivo: "))
        if numero > 0:
            break
        else:
            print("Error: Debes ingresar un número positivo.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
iteraciones = 0
while numero <= 1000:
    numero *= 2
    iteraciones += 1
print(f"El resultado final es {numero}, que supera el tope de 1000.")
print(f"Se realizaron {iteraciones} iteraciones.")