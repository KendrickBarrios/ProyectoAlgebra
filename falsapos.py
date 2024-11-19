import funciones
from sympy import symbols, sympify
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def metodoFalsaPosicion(funcion, intervalo, error):
    mensaje = []
    ancho = 15
    iteraciones = 0
    evaluaciones = [0, 0, 0]
    it, a, b, c, eA, fa, fb, fc = "Iteracion", "a", "b", "c", "eA", "f(a)", "f(b)", "f(c)"
    relleno = "-" * 16

    mensaje.append(f"Funcion ingresada: {str(funcion)}\n")
    mensaje.append(f"Intervalo: [{intervalo[0]}, {intervalo[1]}]\n")
    mensaje.append(f"Tolerancia: {error}\n")
    mensaje.append(f"{it:^{ancho}} | {a:^{ancho}} | {b:^{ancho}} | {c:^{ancho}} | {eA:^{ancho}} | {fa:^{ancho}} | {fb:^{ancho}} | {fc:^{ancho}}")
    mensaje.append(f"{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}")

    while True:
        iteraciones += 1
        c = None

        if not funciones.validar_dominio(funcion, symbols('x'), intervalo[0]) and not funciones.validar_dominio(funcion, symbols('x'), intervalo[1]):
            mensaje.append(f"\nValores fuera del dominio de la función: a = {intervalo[0]}, b = {intervalo[1]}. Método detenido.\n")
            break
        elif not funciones.validar_dominio(funcion, symbols('x'), intervalo[0]):
            mensaje.append(f"\nValor fuera del dominio de la función: a = {intervalo[0]}. Método detenido.\n")
            break
        elif not funciones.validar_dominio(funcion, symbols('x'), intervalo[1]):
            mensaje.append(f"\nValor fuera del dominio de la función: b = {intervalo[1]}. Método detenido.\n")
            break


        # Evaluación en los extremos del intervalo
        evaluaciones[0] = funciones.evaluarFuncion(funcion, intervalo[0])
        evaluaciones[1] = funciones.evaluarFuncion(funcion, intervalo[1])

        # Cálculo del punto intermedio usando la fórmula de Falsa Posición
        c = intervalo[1] - (evaluaciones[1] * (intervalo[0] - intervalo[1])) / (evaluaciones[0] - evaluaciones[1])

        if not funciones.validar_dominio(funcion, symbols('x'), c):
            mensaje.append(f"\nValor fuera del dominio de la función: c = {c}. Método detenido.\n")
            break

        evaluaciones[2] = funciones.evaluarFuncion(funcion, c)

        # Formatear para los mensajes
        sA = "{:.6f}".format(intervalo[0])
        sB = "{:.6f}".format(intervalo[1])
        sC = "{:.6f}".format(c)
        seA = "{:.6f}".format(abs(evaluaciones[2]))
        sfA = "{:.6f}".format(evaluaciones[0])
        sfB = "{:.6f}".format(evaluaciones[1])
        sfC = "{:.6f}".format(evaluaciones[2])

        mensaje.append(f"{str(iteraciones):^{ancho}} | {sA:^{ancho}} | {sB:^{ancho}} | {sC:^{ancho}} | {seA:^{ancho}} | {sfA:^{ancho}} | {sfB:^{ancho}} | {sfC:^{ancho}}")

        # Condición de convergencia
        if abs(evaluaciones[2]) < error or abs(intervalo[1] - intervalo[0]) < error:
            break

        # Actualizar los extremos del intervalo
        if (evaluaciones[0] * evaluaciones[2]) < 0:
            intervalo[1] = c
        else:
            intervalo[0] = c

    # Fuera del ciclo: agregar información final
    if c is None:
        pass
    else:
        sRaiz = "{:.6f}".format(c)
        mensaje.append(f"\nEl metodo converge a {iteraciones} iteraciones con un error absoluto de {seA}.\n")
        mensaje.append(f"\nRaiz encontrada: {sRaiz}\n")
    
    return c, mensaje
