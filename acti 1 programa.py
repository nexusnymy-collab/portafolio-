import re

def analizar_expresion(expresion):
    # Buscar variables (letras)
    variables = sorted(set(re.findall(r"[a-zA-Z]\w*", expresion)))
    
    # Buscar operadores matemáticos
    operadores = re.findall(r"[\+\-\*/\^=<>]", expresion)
    operadores_unicos = sorted(set(operadores))

    return variables, operadores_unicos

# 1. Pedir función
funcion = input("Introduce la función: ")

# 2. Preguntar si hay restricciones
tiene_restricciones = input("¿Tienes restricciones? (si/no): ").strip().lower()

restricciones = ""
if tiene_restricciones == "si":
    restricciones = input("Introduce las restricciones (ejemplo: x>=0, y<=10): ")

# 3. Analizar función y restricciones
vars_funcion, ops_funcion = analizar_expresion(funcion)
vars_restr, ops_restr = analizar_expresion(restricciones) if restricciones else ([], [])

# 4. Unir resultados
todas_vars = sorted(set(vars_funcion + vars_restr))
todos_ops = sorted(set(ops_funcion + ops_restr))

# 5. Validar máximo 2 variables
if len(todas_vars) > 2:
    print("\n❌ ERROR: Se detectaron más de 2 variables:", todas_vars)
else:
    # 6. Mostrar resultados
    print("\n--- RESULTADOS ---")
    print(f"Función: {funcion}")
    if restricciones:
        print(f"Restricciones: {restricciones}")
    print(f"Variables detectadas: {todas_vars}")
    print(f"Operadores detectados: {todos_ops}")
