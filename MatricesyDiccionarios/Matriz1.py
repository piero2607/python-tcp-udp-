continuar=True
while continuar:
    filas=int(input("ingresa el numero de filas:\n"))
    columnas=int(input("ingresa ek numero de columnas:\n"))
    if filas==columnas:
        continuar=False
    else:
        print("filas y columnas deben ser iguales:\n")
matriz=[]
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        if i==j or i+j==filas-1:
            matriz[i].append("x")
        else:
            matriz[i].append("0")
for mt in matriz:
    print(mt)