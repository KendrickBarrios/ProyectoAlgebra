import funciones
from sympy import symbols, sympify, diff
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def metodoNewtonRaphson(funcion, derivada, inicial, maxIteraciones, error):
    mensaje = []
    ancho = 15
    raiz = None
    relleno = "-"*16

    mensaje.append(f"Funcion ingresada {str(funcion)}\n")
    mensaje.append(f"Derivada de la funcion: {str(derivada)}\n")
    mensaje.append(f"Valor inicial: {inicial}\n")
    mensaje.append(f"Tolerancia: {error}\n")
    it, xi, xi1, eA, fxi, dfxi = "Iteracion", "xi", "xi+1", "eA", "f(xi)", "f'(xi)"
    mensaje.append(f"{it:^{ancho}} | {xi:^{ancho}} | {xi1:^{ancho}} | {eA:^{ancho}} | {fxi:^{ancho}} | {dfxi:^{ancho}}")
    mensaje.append(f"{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}")

    actual = inicial
    for i in range(maxIteraciones):
        fxi = funciones.evaluarFuncion(funcion, actual)
        dfxi = funciones.evaluarFuncion(derivada, actual)

        if abs(dfxi) < 1e-10:
            sActual = "{:.6f}".format(actual)
            sSiguiente = "---"
            sfxi = "{:.6f}".format(fxi)
            sdfxi = "{:.6f}".format(dfxi)
            mensaje.append(f"{str(i+1):^{ancho}} | {sActual:^{ancho}} | {sSiguiente:^{ancho}} | {sfxi:^{ancho}} | {sdfxi:^{ancho}}")
            mensaje.append("\nValor de la derivada muy pequeño, posible division por cero. Metodo detenido.\n")
            break

        siguiente = actual-(fxi/dfxi)
        errorAbs = abs(funciones.evaluarFuncion(funcion, siguiente))

        sActual = "{:.6f}".format(actual)
        sSiguiente = "{:.6f}".format(siguiente)
        sErrorAbs = "{:.6f}".format(errorAbs)
        sfxi = "{:.6f}".format(fxi)
        sdfxi = "{:.6f}".format(dfxi)
        mensaje.append(f"{str(i+1):^{ancho}} | {sActual:^{ancho}} | {sSiguiente:^{ancho}} | {sErrorAbs:^{ancho}} | {sfxi:^{ancho}} | {sdfxi:^{ancho}}")

        if errorAbs < error:
            raiz = siguiente
            break

        actual = siguiente
    
    if raiz is not None:
        mensaje.append(f"\nEl metodo converge a {i+1} iteraciones con un error absoluto de {errorAbs}.\n")
        mensaje.append(f"Raiz encontrada: {raiz}\n")
    else:
        mensaje.append(f"\nNo se encontro una raiz con el valor inicial {inicial} en {maxIteraciones} iteraciones.")

    return raiz, mensaje