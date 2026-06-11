# Funciones para conversiones
def millas_a_kilometros(millas):
    return millas * 1.61

def kilometros_a_millas(kilometros):
    return kilometros / 1.61

# Solicitar al usuario la conversión deseada
print("Conversor de Millas y Kilómetros")
print("1. Convertir Millas a Kilómetros")
print("2. Convertir Kilómetros a Millas")
opcion = int(input("Elige una opción (1 o 2): "))

if opcion == 1:
    millas = float(input("Introduce la cantidad en millas: "))
    print(f"{millas} millas son {millas_a_kilometros(millas):.2f} kilómetros.")
elif opcion == 2:
    kilometros = float(input("Introduce la cantidad en kilómetros: "))
    print(f"{kilometros} kilómetros son {kilometros_a_millas(kilometros):.2f} millas.")
else:
    print("Opción no válida.")