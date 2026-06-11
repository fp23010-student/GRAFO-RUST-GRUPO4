arreglo = [7,1,2,5,4]
print("Arreglo original:",arreglo)
for i in range(len(arreglo)):
    for j in range(len(arreglo)-1):
        if arreglo[j]<arreglo[j+1]:  #Cambiar el signo para ordenar en forma descendente
            temp=arreglo[j]
            arreglo[j]=arreglo[j+1]
            arreglo[j+1]=temp
            print("Arreglo Descendente:",arreglo)
print("Arreglo Descendente:",arreglo)
