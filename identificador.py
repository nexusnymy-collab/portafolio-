import re

funcion = input("Introduce una función simple (sin trigonometría, por ejemplo: 3*x**2 + 5*x - 7): ")
funcion = funcion.replace(" ", "")

if re.search(r'[a-zA-Z_]\w*\s*\(', funcion):
    print("\n❌ No se permiten funciones como sin(), cos(), log(), etc.")
else:
    variables = sorted(set(re.findall(r'[a-zA-Z_]\w*', funcion)))
    constantes = re.findall(r'\b\d+\.?\d*\b', funcion)
    simbolos = sorted(set(re.findall(r'[\+\-\*/\^\=\(\)]', funcion)))

    print("\n📘 Análisis de la función:")
    print(f"Función introducida: {funcion}")
    print(f"🔹 Variables: {variables if variables else 'Ninguna'}")
    print(f"🔹 Constantes: {constantes if constantes else 'Ninguna'}")
    print(f"🔹 Símbolos matemáticos: {simbolos if simbolos else 'Ninguno'}")
