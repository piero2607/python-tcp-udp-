import random

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
        aleatorio=random.randint(0,20)
        matriz[i].append(aleatorio)
for mt in matriz:
    print(mt)
sumafila=0
for i in range(filas):
    sumafila=sum(matriz[i])
    print(f"fila {i+1}: {sumafila}")

for j in range(columnas):
    sumacolumna=0
    for i in range(filas):
        sumacolumna+=matriz[i][j]
    print(f"columna {j+1} {sumacolumna}")