tareas = []
tareas.append(input("Ingresa la tarea 1: "))
tareas.append(input("Ingresa la tarea 2: "))
tareas.append(input("Ingresa la tarea 3: "))
tareas.insert(0, "Reunión importante")
del tareas[1]
print("Lista final de tareas:", tareas)
print("Longitud de la lista:", len(tareas))