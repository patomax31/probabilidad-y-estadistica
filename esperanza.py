import math

        # 0, 1 , 2
bidi = [[1, 2, 3],       # 0
        [0.3, 0.4, 0.3]] #1

esperanza = 0
varianza = 0

rows = int(input("Filas: "))
cols = int(input("columnas: "))

matrix = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range (cols):
        matrix[i][j] = float(input(f"Ingresa el elemento [{i}][{j}]: " ))
    
print(matrix)
for j in range (cols):
    esp = (matrix[0][j] * matrix[1][j])
    #print(f"esp_{i}: {esp}")
    esperanza += esp

    

for i in range (cols):
    var = (pow((matrix[0][i]-esperanza), 2) * matrix[1][i])
    #print(var)
    varianza += var

desv_est = math.sqrt(varianza)

print("esperanza:", esperanza)
print("Varianza:", varianza)
print("Desviación estandar:", desv_est)