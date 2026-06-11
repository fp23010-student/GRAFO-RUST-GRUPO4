def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
num = int(input("Ingrese un número: "))

if es_primo(num):
    print(f"El número {num} es primo.")
    if es_primo(num - 2):
        print(f"El número {num} es primo gemelo con {num - 2}.")
    elif es_primo(num + 2):
        print(f"El número {num} es primo gemelo con {num + 2}.")
    else:
        print(f"El número {num} no tiene un primo gemelo.")
else:
    print(f"El número {num} no es primo.")