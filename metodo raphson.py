import math
import re
import random

# =======================================
# MÉTODO DE NEWTON-RAPHSON AUTOMÁTICO
# =======================================

def limpiar_expresion(expr):
    """Corrige expresiones del tipo 3x -> 3*x, 2(x+1) -> 2*(x+1)."""
    expr = expr.replace('^', '**')
    expr = re.sub(r'(\d)(x)', r'\1*\2', expr)        # 3x -> 3*x
    expr = re.sub(r'(\d)\(', r'\1*(', expr)          # 2(x+1) -> 2*(x+1)
    expr = re.sub(r'(x)\(', r'\1*(', expr)           # x(x+1) -> x*(x+1)
    return expr

def evaluar(expr, x):
    """Evalúa f(x) de forma segura usando math."""
    try:
        return eval(expr, {"x": x, "math": math, "__builtins__": {}})
    except Exception as e:
        print(f"❌ Error al evaluar la función en x={x}: {e}")
        exit()

def derivada_numerica(expr, x, h=1e-6):
    """Aproximación de la derivada mediante diferencia central."""
    return (evaluar(expr, x + h) - evaluar(expr, x - h)) / (2 * h)

def newton_raphson_auto(f_expr):
    # Parámetros automáticos
    tol = 1e-6
    max_iter = 1000
    x0 = random.uniform(-5, 5)  # valor inicial aleatorio

    print("\n=== MÉTODO DE NEWTON-RAPHSON ===")
    print(f"Función: f(x) = {f_expr}")
    print(f"Valor inicial automático x0 = {x0:.4f}")
    print(f"Tolerancia = {tol}, iteraciones máximas = {max_iter}")
    print(f"\n{'Iteración':>10} | {'x_n':>15} | {'f(x_n)':>15}")
    print("-" * 45)

    for i in range(1, max_iter + 1):
        fx = evaluar(f_expr, x0)
        dfx = derivada_numerica(f_expr, x0)

        if dfx == 0:
            # Si la derivada es cero, intenta un nuevo valor inicial aleatorio
            x0 = random.uniform(-5, 5)
            continue

        x1 = x0 - fx / dfx
        f1 = evaluar(f_expr, x1)

        print(f"{i:10d} | {x1:15.8f} | {f1:15.8f}")

        if abs(x1 - x0) < tol:
            print(f"\n✅ Raíz aproximada encontrada: {x1:.8f}")
            print(f"🔁 Iteraciones realizadas: {i}")
            return x1

        x0 = x1

    print("\n⚠️ No se alcanzó la tolerancia después del número máximo de iteraciones.")
    return None


# =======================================
# PROGRAMA PRINCIPAL
# =======================================
print("=== MÉTODO DE NEWTON-RAPHSON (Automático sin Sympy) ===")
print("Puedes escribir la función como: 3x^3 + 2x + 2 o math.sin(x)-x/2")

expr_usuario = input("Ingresa la función f(x): ")
expr_limpia = limpiar_expresion(expr_usuario)

newton_raphson_auto(expr_limpia)
