sombrero=[1,2,3,4,5]
sombrero[len(sombrero)//2]=int(input("Ingrse un numero entero para reemplazar el original: "))
print(sombrero)
sombrero.pop()
print("La longitud de la lista ahora es:",len(sombrero))
print(sombrero)
#list.append(value)
#list.insert(index,value)