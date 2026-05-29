import math

media = float(input("Ingresa la media: "))

desviacion = float(input("Ingresa la desviación: "))

muestra = float(input("Ingresa la muestra: "))

tamaño = float(input("Ingresa el tamaño de la muestra: "))




lim_cent = (muestra-media)/(desviacion/math.sqrt(tamaño))

print(lim_cent)