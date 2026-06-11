print("Verificar si un número es primo gemelo")
cuentaresiduos = 0
pares = 0
impares = 0
rango = 0
num = int(input("Ingrese un número: "))
if num < 0:
    print("El número no es válido, debe ser positivo")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            cuentaresiduos += 1
            print(i)
            if i % 2 == 0:
                pares += 1
            else:
                impares += 1
            if i >= 5 and i <= 20:
                rango += 1
    print("Hay", rango, "divisores entre 5 y 20")
    print("Hay", pares, "divisores pares")
    print("Hay", impares, "divisores impares")
    if cuentaresiduos == 2:
        print("El número es primo")
        es_gemelo = False
        for vecino in [num - 2, num + 2]:
            cuentaresiduos_vecino = 0
            for i in range(1, vecino + 1):
                if vecino % i == 0:
                    cuentaresiduos_vecino += 1
            if cuentaresiduos_vecino == 2:
                es_gemelo = True
                print(f"El número {num} es primo gemelo con {vecino}")
                break
        if not es_gemelo:
            print(f"El número {num} no tiene un primo gemelo")
    else:
        print("El número no es primo")