arreglo=[7,1,2,5,4]
print("arreglo original:",arreglo)
for i in range(len(arreglo)):
    for j in range(len(arreglo)-1):
        if arreglo[j]>arreglo[j+1]:
            temp=arreglo[j]
            arreglo[j]=arreglo[j+1]
            arreglo[j+1]=temp
            print("arreglo ordenado:",arreglo)
print("arreglo ordenado:",arreglo)

#arreglo=[7,1,2,5,4]
#print("arreglo original:",arreglo)
#for i in range(len(arreglo)):
 #   for j in range(len(arreglo)-1):
  #      if arreglo[j]>arreglo[j+1]:
   #         arreglo[j],arreglo[j+1]=arreglo[j+1],arreglo[j]
            #temp=arreglo[j]
            #arreglo[j]=arreglo[j+1]
            #arreglo[j+1]=temp
    #        print("arreglo ordenado:",arreglo)