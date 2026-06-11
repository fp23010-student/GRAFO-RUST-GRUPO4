meses = {
    1: ("Enero", 31),
    2: ("Febrero", 28),
    3: ("Marzo", 31),
    4: ("Abril", 30),
    5: ("Mayo", 31),
    6: ("Junio", 30),
    7: ("Julio", 31),
    8: ("Agosto", 31),
    9: ("Septiembre", 30),
    10: ("Octubre", 31),
    11: ("Noviembre", 30),
    12: ("Diciembre", 31)
}
for numero in range(1, 13):
    nombre_mes, dias = meses[numero]
    print(f"{nombre_mes}: {dias} días")