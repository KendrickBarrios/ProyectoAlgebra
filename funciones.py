from sympy import symbols, sympify, diff
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

# Definicion simbolica de la variable
x = symbols('x')

def leerFuncion():
    op = input("Desea una explicación de la notación de funciones? (s/n): ").lower()
    if op == "s":
        print("\n=== Instrucciones para ingresar funciones matemáticas en SymPy ===\n")
        # Operaciones Aritméticas Básicas
        print("Símbolos para operaciones aritméticas básicas:")
        print("  Suma: + (ej.: x + 5)")
        print("  Resta: - (ej.: x - 9)")
        print("  Multiplicación: * (ej.: 3*x o bien 3x)")
        print("  División: / (ej.: x / 2)")
        print("  Potencia: ** (ej.: x**2 para x al cuadrado)\n")

        # Funciones Trigonométricas
        print("Funciones trigonométricas:")
        print("  Seno: sin(x)")
        print("  Coseno: cos(x)")
        print("  Tangente: tan(x)")
        print("  Cosecante: csc(x)")
        print("  Secante: sec(x)")
        print("  Cotangente: cot(x)\n")
        print("**Nota:** Las funciones trigonométricas usan radianes como unidad de medida.\n")

        # Funciones Trigonométricas Inversas
        print("Funciones trigonométricas inversas:")
        print("  Arco seno: asin(x)")
        print("  Arco coseno: acos(x)")
        print("  Arco tangente: atan(x)")
        print("  Arco cosecante: acsc(x)")
        print("  Arco secante: asec(x)")
        print("  Arco cotangente: acot(x)\n")

        # Funciones Hiperbólicas
        print("Funciones hiperbólicas:")
        print("  Seno hiperbólico: sinh(x)")
        print("  Coseno hiperbólico: cosh(x)")
        print("  Tangente hiperbólica: tanh(x)")
        print("  Cosecante hiperbólica: csch(x)")
        print("  Secante hiperbólica: sech(x)")
        print("  Cotangente hiperbólica: coth(x)\n")

        # Funciones Exponenciales y Logarítmicas
        print("Funciones exponenciales y logarítmicas:")
        print("  Exponencial: exp(x) para e^x")
        print("  Logaritmo natural: log(x) para ln(x)")
        print("  Logaritmo en base 10: log(x, 10) o log10(x)")
        print("  Logaritmo en cualquier base: log(x, base)\n")

        # Funciones de Redondeo y Valor Absoluto
        print("Funciones de redondeo y valor absoluto:")
        print("  Valor absoluto: Abs(x)")
        print("  Redondeo hacia abajo (piso): floor(x)")
        print("  Redondeo hacia arriba (techo): ceiling(x)\n")

        # Funciones Misceláneas
        print("Otras funciones útiles:")
        print("  Factorial: factorial(x) o x!")
        print("  Parte entera: Integer(x) para forzar un valor entero")
        print("  Parte decimal: frac(x) devuelve la parte decimal de un número\n")

    function_str = input("\nIngrese la funcion: ")

    # Convierte terminos como 3x en 3*x
    transformations = (standard_transformations + (implicit_multiplication_application,))

    try:
        # Convierte la cadena en una funcion
        function_expr = parse_expr(function_str, transformations=transformations)
        return function_expr
    except Exception as e:
        print("Error parsing function:", e)
        return None

def derivar(function_expr, var):
    return diff(function_expr, var)

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

def leerError():
    pase = False
    while not pase:
        pase = True
        try:
            error = float(input("\nIngrese el error a considerar: "))
            if error < 0:
                pase = False
                print("\nEl error ingresado debe ser un numero positivo.")
                input("Presione ENTER para continuar.\n")
        except ValueError:
            print("\nEl error ingresado debe ser un numero entero o decimal.")
            input("Presione ENTER para continuar.\n")
    return error

def leerInicialIteraciones():
    pase = False
    while not pase:
        pase = True
        try:
            valor = float(input("Ingrese el valor inicial a evaluar: "))
            iteraciones = int(input("\nIngrese el numero de iteraciones a realizar: "))
            if iteraciones < 1:
                pase = False
                print("\nEl numero de iteraciones ingresado debe ser mayor o igual a 1.")
                input("Presione ENTER para continuar.\n")
        except ValueError:
            print("\nEl valor inicial ingresado debe ser un numero entero o con decimales.")
            print("El numero de iteraciones debe ser un numero entero.")
            input("Presione ENTER para continuar.\n")
            pase = False

    return valor, iteraciones