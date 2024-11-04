from sympy import symbols, sympify
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

# Definicion simbolica de la variable
x = symbols('x')

def leerFuncion():
    function_str = input("Ingrese la funcion: ")

    # Convierte terminos como 3x en 3*x
    transformations = (standard_transformations + (implicit_multiplication_application,))

    try:
        # Convierte la cadena en una funcion
        function_expr = parse_expr(function_str, transformations=transformations)
        return function_expr
    except Exception as e:
        print("Error parsing function:", e)
        return None

def evaluarFuncion(function_expr, x_value):
    try:
        # Evalua la funcion
        result = function_expr.subs(x, x_value)
        return result
    except Exception as e:
        print("Error evaluating function:", e)
        return None

def leerIntervalo():
    pase = False
    intervalo = []
    while not pase:
        pase = True
        try:
            inf = float(input("Ingrese el intervalo inferior: "))
            sup = float(input("Ingrese el intervalor superior: "))
        except ValueError:
            print("\nLos valores ingresados deben ser numeros con o sin decimales.")
            input("Presione ENTER para continuar.\n")
            pase = False
    
    intervalo.append(inf)
    intervalo.append(sup)
    return intervalo