#crear una matriz bidimencioanl
matriz=[[12,14,16,18,20],[22,24,26,28,30],[32,34,36,38,40],[42,44,46,48,50],]
#obtener la primera fila
print(matriz[0])
#obtener la segunda fila
print(matriz[1])
#obtener la tercera fila
print(matriz[2])
#obtener la cuarta fila
print(matriz[3])
for fila in range(0, len(matriz)):
    for columna in range(0, len(matriz[fila])):
        elemento = matriz[fila][columna]
        if elemento == 38:
            print("¡VALOR ENCONTRADO!")
            FILA = columna + 1
            COLUMNA = fila + 1
            print(f"VALOR ENCONTRADO EN LA FILA   ({FILA })")
            print(f"VALOR ENCONTRADO EN LA COLUMNA  ( {COLUMNA})")