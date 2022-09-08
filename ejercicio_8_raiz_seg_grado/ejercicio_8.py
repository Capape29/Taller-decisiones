#  Elaborar un programa que obtenga las raíces de una ecuación de segundo grado.
from math import sqrt
print("la Formula cuadratica es --> ax² + bx + c = 0")
# Input
a = int(input("digite el valor de la variable a:"))
b = int(input("digite el valor de la variable b:"))
c = int(input("digite el valor de la variable c:"))

# Processing
if ((b ** 2)-4 * a * c) < 0:
    print("No hay solucion en los numeros reales porque el discriminante es negativo y las raices negativas son umeros imaginarios.")
else:
    x1 = (-b + sqrt((b ** 2)- 4 * a * c) ) / (2 * a)
    x2 = (-b - sqrt((b ** 2)- 4 * a * c) ) / (2 * a)

# Output    
print("las soluciones de la cuadratica son:", x1, "y", x2)
