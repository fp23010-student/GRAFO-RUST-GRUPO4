dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

while True:
    try:
        numero = int(input("Introduce un número del 1 al 7: "))
        
        if 1 <= numero <= 7:
            print(f"El día correspondiente es: {dias_semana[numero]}")
            break
        else:
            print("Error: El número debe estar entre 1 y 7.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")