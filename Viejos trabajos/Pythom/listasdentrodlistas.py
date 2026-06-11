row=[]
for i in range(8):
    row=[empty for i in range(8)]
    board.appent(row)
    row.append(PEON_BLANCO)
    row=[PEON_BLANCO for i in range(8)]
    square= [x**2 for i in range(8)]
    two= [x**2 for i in range(8)]
    odds= [x for x in range(8) if x%2 !=1]
    board=[[empty for i in range(8)] for j in range(8)]
