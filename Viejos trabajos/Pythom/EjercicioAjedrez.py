temps=[[0,0 for i in range(24)] for j in range(31)]
total=0.0
for day in temps:
    total+=day[11]
    average=total/31
print("La temperatura promedio es:",average)