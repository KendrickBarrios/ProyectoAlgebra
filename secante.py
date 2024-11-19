import funciones
from sympy import log, sqrt, denom, symbols, sympify, diff
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def metodoSecante(funcion, anterior, inicial, maxIteraciones, error):
    mensaje = []
    ancho = 15
    raiz = None
    relleno = "-" * 16

    mensaje.append(f"Funcion ingresada {str(funcion)}\n")
    mensaje.append(f"Valores iniciales: x0 = {anterior} | x1 = {inicial}\n")
    mensaje.append(f"Tolerancia: {error}\n")
    it, xiAnt, xi, xi1, eA, fxiAnt, fxi = "Iteracion", "xi-1", "xi", "xi+1", "eA", "f(xi-1)", "f(xi)"
    mensaje.append(f"{it:^{ancho}} | {xiAnt:^{ancho}} | {xi:^{ancho}} | {xi1:^{ancho}} | {eA:^{ancho}} | {fxiAnt:^{ancho}} | {fxi:^{ancho}}")
    mensaje.append(f"{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}")

    actual = inicial
    ant = anterior
    for i in range(maxIteraciones):
        # Verificar dominio de los valores actuales
        if not funciones.validar_dominio(funcion, symbols('x'), ant) and not funciones.validar_dominio(funcion, symbols('x'), actual):
            mensaje.append(f"\nValores fuera del dominio de la función: x0 = {ant}, x1 = {actual}. Método detenido.\n")
            break
        elif not funciones.validar_dominio(funcion, symbols('x'), ant):
            mensaje.append(f"\nValor fuera del dominio de la función: x0 = {ant}. Método detenido.\n")
            break
        elif not funciones.validar_dominio(funcion, symbols('x'), actual):
            mensaje.append(f"\nValor fuera del dominio de la función: x1 = {actual}. Método detenido.\n")
            break

        fxiAnt = funciones.evaluarFuncion(funcion, ant)
        fxi = funciones.evaluarFuncion(funcion, actual)

        # Convertir a flotantes si son válidos
        try:
            fxiAnt = float(fxiAnt.evalf())
            fxi = float(fxi.evalf())
        except TypeError:
            mensaje.append("\nSe encontro un valor complejo durante la evaluación. Método detenido.\n")
            break

        sAnterior = "{:.6f}".format(ant)
        sActual = "{:.6f}".format(actual)
        sfxiAnt = "{:.6f}".format(fxiAnt)
        sfxi = "{:.6f}".format(fxi)

        if abs(fxiAnt - fxi) < 1e-10:
            sSiguiente = "---"
            sErrorAbs = "---"
            mensaje.append(f"{str(i+1):^{ancho}} | {sAnterior:^{ancho}} | {sActual:^{ancho}} | {sSiguiente:^{ancho}} | {sErrorAbs:^{ancho}} | {sfxiAnt:^{ancho}} | {sfxi:^{ancho}}")
            mensaje.append("\nValor del denominador muy pequeño en el calculo del siguiente termino. Posible division entre cero. Metodo detenido.\n")
            break

        siguiente = actual - (fxi * (ant - actual)) / (fxiAnt - fxi)

        # Verifica el dominio de la siguiente iteracion
        if not funciones.validar_dominio(funcion, symbols('x'), siguiente):
            mensaje.append(f"\nEl siguiente valor está fuera del dominio: x = {siguiente}. Metodo detenido.\n")
            break

        errorAbs = abs(funciones.evaluarFuncion(funcion, siguiente).evalf())

        sSiguiente = "{:.6f}".format(siguiente)
        sErrorAbs = "{:.6f}".format(errorAbs)
        mensaje.append(f"{str(i+1):^{ancho}} | {sAnterior:^{ancho}} | {sActual:^{ancho}} | {sSiguiente:^{ancho}} | {sErrorAbs:^{ancho}} | {sfxiAnt:^{ancho}} | {sfxi:^{ancho}}")

        if errorAbs < error:
            raiz = siguiente
            break

        ant = actual
        actual = siguiente
    
    if raiz is not None:
        mensaje.append(f"\nEl metodo converge a {i+1} iteraciones con un error absoluto de {errorAbs}.\n")
        mensaje.append(f"Raiz encontrada: {raiz}\n")
    else:
        mensaje.append(f"\nNo se encontro una raiz con el valor inicial {inicial} en {i+1} iteraciones.\n")

    return raiz, mensaje
