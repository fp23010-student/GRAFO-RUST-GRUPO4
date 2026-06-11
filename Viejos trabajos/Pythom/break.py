numMax=-99999999
counter=0
while True:
    num=int(input("Enter a number -1 to end: "))
    if num==-1:
        break
    counter+=1
    if num>numMax:
        numMax=num
        if counter !=0:
            print("The maximum number is:",numMax)
        else:
            print("No numbers were entered")