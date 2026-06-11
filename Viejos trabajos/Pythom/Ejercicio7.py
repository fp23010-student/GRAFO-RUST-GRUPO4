bloques=int(input("Enter the number of blocks: "))
altura=0
bloques_necesarios=1
while bloques>=bloques_necesarios:
    altura+=1
    bloques-=bloques_necesarios
    bloques_necesarios+=1
    print("la altura de la piramide es:",altura)