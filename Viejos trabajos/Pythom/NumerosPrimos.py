print("divisor de un numero")
cuentaresiduos = 0
pares = 0
impares = 0
rango =0
num = int(input("ingrese un numero: "))
if num < 0:
	print("El número no es valido, debe ser positivo")
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
print("hay", rango, "divisores entre 5 y 20")
print("hay", pares, "divisores pares")
print("hay", impares, "divisores impares")
if cuentaresiduos == 2:
	print("el numero es primo")
else:
	print("el numero no es primo")	