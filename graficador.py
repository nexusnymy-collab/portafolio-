# Programa que grafica dos funciones lineales sin usar librerías externas

# Pedir las funciones
f1_str = input("Ingresa la primera función lineal (en términos de x, ej: 2*x+3): ")
f2_str = input("Ingresa la segunda función lineal (en términos de x, ej: -x+5): ")

# Calcular coeficientes aproximados (pendiente y ordenada)
def obtener_coeficientes(f_str):
    a = eval(f_str.replace("x", "(1)")) - eval(f_str.replace("x", "(0)"))
    b = eval(f_str.replace("x", "(0)"))
    return a, b

a1, b1 = obtener_coeficientes(f1_str)
a2, b2 = obtener_coeficientes(f2_str)

# Calcular intersección si existe
if a1 != a2:
    x_int = (b2 - b1) / (a1 - a2)
    y_int = a1 * x_int + b1
    interseccion = (round(x_int, 2), round(y_int, 2))
else:
    interseccion = None

# Crear una "grilla" ASCII
ancho = 41  # columnas (x desde -20 hasta 20)
alto = 21   # filas (y desde -10 hasta 10)
grilla = [[" " for _ in range(ancho)] for _ in range(alto)]

# Función para convertir coordenadas matemáticas a índices de la grilla
def coord_a_ind(x, y):
    col = int(x + ancho // 2)
    fila = int(alto // 2 - y)
    if 0 <= fila < alto and 0 <= col < ancho:
        return fila, col
    return None

# Dibujar ejes
for x in range(-ancho//2, ancho//2):
    pos = coord_a_ind(x, 0)
    if pos:
        grilla[pos[0]][pos[1]] = "-"
for y in range(-alto//2, alto//2):
    pos = coord_a_ind(0, y)
    if pos:
        grilla[pos[0]][pos[1]] = "|"
grilla[alto//2][ancho//2] = "+"  # origen

# Dibujar funciones
for x in range(-20, 21):
    y1 = eval(f1_str)
    y2 = eval(f2_str)
    p1 = coord_a_ind(x, round(y1))
    p2 = coord_a_ind(x, round(y2))
    if p1:
        grilla[p1[0]][p1[1]] = "1"
    if p2:
        grilla[p2[0]][p2[1]] = "2"

# Marcar intersección
if interseccion:
    p = coord_a_ind(interseccion[0], interseccion[1])
    if p:
        grilla[p[0]][p[1]] = "X"

# Mostrar la grilla
print("\nGráfica aproximada (ASCII):")
for fila in grilla:
    print("".join(fila))

# Mostrar información
print(f"\nEcuaciones:")
print(f"f1(x) = {f1_str}")
print(f"f2(x) = {f2_str}")
if interseccion:
    print(f"Punto de intersección: {interseccion}")
else:
    print("Las rectas son paralelas (no se intersectan).")

