numbers=[10,5,7,2,1]
print("Contenido de la lista original:",numbers)
numbers[0]=111
print("\nContenido de la lista original:",numbers)
numbers[1]= numbers[4]
print("Contenido de la lista con intercambio:",numbers)
print("\nlongitud de la lista:",len(numbers))
del numbers[1]
print("Longitud de la nueva lista:",len(numbers))
print("\nNuevo contenido de la lista:",numbers)