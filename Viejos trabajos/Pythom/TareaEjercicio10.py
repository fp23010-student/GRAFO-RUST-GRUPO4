for _ in range(1):
    try:
        numero = float(input("Introduce un número positivo: "))
        if numero <= 0:
            print("Error: Debes ingresar un número positivo.")
            exit()
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        exit()
resultado = numero
iteraciones = 0
for _ in range(1000):
    if resultado > 1000:
        break
    resultado *= 2
    iteraciones += 1
print(f"El resultado final es {resultado}, que supera el tope de 1000.")
print(f"Se realizaron {iteraciones} iteraciones.")