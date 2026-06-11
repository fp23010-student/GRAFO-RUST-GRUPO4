while True:
    try:
        numero = int(input("Introduce un número positivo para iniciar la cuenta regresiva: "))
        if numero >= 0:
            break
        else:
            print("Error: Debes ingresar un número positivo.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
while numero >= 0:
    if numero == 0:
        print("¡Despegue!")
    else:
        print(numero)
    numero -= 1