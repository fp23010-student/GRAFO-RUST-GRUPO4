meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}
while True:
    try:
        numero = int(input("Introduce un número del 1 al 12: "))
        if 1 <= numero <= 12:
            print(f"El mes correspondiente es: {meses[numero]}")
            break
        else:
            print("Error: El número debe estar entre 1 y 12.")
    except ValueError:
        print("Error: Debes ingresar un número válido")