#my_list=[10,8,6,4,2]
#new_list= my_list[1:-1]
#print(new_list)
#my_list=[10,8,6,4,2]
#new_list= my_list[:3]
#print(new_list)
#my_list=[10,8,6,4,2]
#new_list= my_list[3:]
#print(new_list)
#my_list=[10,8,6,4,2]
#del my_list[1:3]
#print(my_list)
#my_list=[10,8,6,4,2]
#del my_list[:]
#print(my_list)
#my_list=[10,8,6,4,2]
#del my_list
#print(my_list)
#my_list=[17,3,11,5,19,9,7,15,13]
#largest = my_list[0]
#for i in range(1, len(my_list)):
 #   if my_list[i] > largest:
  #      largest = my_list[i]
#print("El número más grande es:", largest)
#my_list=[17,3,11,5,19,9,7,15,13]
#largest = my_list[0]
#for i in my_list:
 #   if i > largest:
  #      largest = i
#print("El número más grande es:", largest)
my_list=[1,2,3,4,5,6,7,8,9,10]
to_find=5
found=False
input("Elemento a buscar:")
for i in range(len(my_list)):
    found=my_list[i]==to_find
    if found:
        break
    if found:
        print("Elemento encontrado en el indice",i)
    else:
        print("Elemento no encontrado")