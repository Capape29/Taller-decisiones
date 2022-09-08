# Elaborar un programa para resolver una ecuación de primer grado
print("la formula de una ecuación de primer grado es --> ax + b = 0")

# Input
a = int(input("Digite el valor de la variable 'a':"))
b = int(input("Digite el valor de la variable 'b':"))

# Processing
if a == 0:
    if b > 0:
        print("No tiene solución")
    else:
        print("la ecuación tiene infinitas soluciones")
else:
    x1 = -b / a

# Output
print("La solución es:", x1)