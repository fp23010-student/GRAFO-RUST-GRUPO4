numero = int(input("Introduce un número entero positivo: "))
if numero > 0:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Error: Debes ingresar un número entero positivo.")