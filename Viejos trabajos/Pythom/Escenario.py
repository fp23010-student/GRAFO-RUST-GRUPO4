beatles=[]
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
for i in range(3,5):
    beatles.append(input("Ingrese el nombre del beatle:"+str(i)+"?"))
print("Los beatles son:",beatles)
del beatles[3]
del beatles[3]
print("Los beatles son:",beatles)
beatles.insert(0,"Ringo Starr")
print("Los beatles son:",beatles)