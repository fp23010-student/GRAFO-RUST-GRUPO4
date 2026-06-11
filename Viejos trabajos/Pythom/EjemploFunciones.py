def leerValores(tipo):
    dato = input("Ingrese un valor: ")
    if tipo == 1:
        print("El tipo de dato es entero", dato)
        return int(dato)
    elif tipo == 2:
        print("El tipo de dato es flotante", dato)
        return float(dato)
    elif tipo == 3:
        print("El tipo de dato es cadena", dato)
        return str(dato)
    else:
        print("Tipo de dato no válido")

entero = leerValores(1)
flotante = leerValores(2)
cadena = leerValores(3)