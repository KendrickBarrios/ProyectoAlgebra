import funciones
from sympy import symbols, sympify
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def metodoBiseccion(funcion, intervalo):
    mensaje = []
    ancho = 15
    iteraciones = 0
    evaluaciones = [0, 0, 0]
    error = 0.0001
    a, b, c, fa, fb, fc = "a", "b", "c", "f(a)", "f(b)", "f(c)"
    relleno = "-"*16
    
    mensaje.append(f"Funcion ingresada: {str(funcion)}\n")
    mensaje.append(f"Intervalo: [{intervalo[0]}, {intervalo[1]}]\n")
    mensaje.append(f"{a:^{ancho}} | {b:^{ancho}} | {c:^{ancho}} | {fa:^{ancho}} | {fb:^{ancho}} | {fc:^{ancho}}")
    mensaje.append(f"{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}")


    while True:
        iteraciones += 1

        evaluaciones[0] = funciones.evaluarFuncion(funcion, intervalo[0])
        evaluaciones[1] = funciones.evaluarFuncion(funcion, intervalo[1])
        c = float(intervalo[0] + intervalo[1]) / 2 
        evaluaciones[2] = funciones.evaluarFuncion(funcion, c)

        mensaje.append("")

        for i in range(2):
            valor = "{:.6f}".format(intervalo[i])
            mensaje[len(mensaje)-1] += f"{valor:^{ancho}} | "

        valor = "{:.6f}".format(c)
        mensaje[len(mensaje)-1] += f"{valor:^{ancho}} | "

        for i in range(3):
            valor = "{:.6f}".format(evaluaciones[i])
            mensaje[len(mensaje)-1] += f"{valor:^{ancho}}"
            if i < 2:
                mensaje[len(mensaje)-1] += " | "
        
        if abs(evaluaciones[2]) < error or abs(intervalo[1] - intervalo[0]) < error:
            break
        
        if (evaluaciones[0] * evaluaciones[2]) < 0:
            intervalo[1] = c
        else:
            intervalo[0] = c

    stringRaiz = "{:.6f}".format(c)
    mensaje.append(f"\nRaiz encontrada: {stringRaiz}\n")
    mensaje.append(f"Numero de iteraciones: {iteraciones}")

    return c, mensaje

def metodoBiseccionMultiraiz(funcion, intervalo, subdivisiones=100, error=0.0001):
    mensaje = []
    ancho = 15
    iteraciones_totales = 0
    raices = []
    a, b, c, fa, fb, fc = "a", "b", "c", "f(a)", "f(b)", "f(c)"
    relleno = "-"*16

    mensaje.append(f"Funcion ingresada: {str(funcion)}\n")
    mensaje.append(f"Intervalo: [{intervalo[0]}, {intervalo[1]}]\n")
    mensaje.append(f"{a:^{ancho}} | {b:^{ancho}} | {c:^{ancho}} | {fa:^{ancho}} | {fb:^{ancho}} | {fc:^{ancho}}")
    mensaje.append(f"{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}+-{relleno}")

    # Se divide el intervalo dado en subintervalos mas pequeños
    paso = (intervalo[1] - intervalo[0]) / subdivisiones
    subintervalos = [(intervalo[0] + i * paso, intervalo[0] + (i + 1) * paso) for i in range(subdivisiones)]
    
    for sub_a, sub_b in subintervalos:
        # Evaluar la funcion en los extremos del subintervalo
        fa = funciones.evaluarFuncion(funcion, sub_a)
        fb = funciones.evaluarFuncion(funcion, sub_b)

        # Si hay cambio de signo o si alguno de los extremos es una raiz exacta
        if fa * fb < 0 or abs(fa) < error or abs(fb) < error:
            iteraciones = 0
            a, b = sub_a, sub_b
            while True:
                iteraciones += 1
                iteraciones_totales += 1

                # Punto medio y evaluacion
                c = (a + b) / 2
                fc = funciones.evaluarFuncion(funcion, c)

                # Crear mensaje de la iteracion actual
                mensaje_linea = f"{a:^{ancho}.6f} | {b:^{ancho}.6f} | {c:^{ancho}.6f} | {fa:^{ancho}.6f} | {fb:^{ancho}.6f} | {fc:^{ancho}.6f}"
                mensaje.append(mensaje_linea)

                # Verificar el criterio de convergencia
                if abs(fc) < error or abs(b - a) < error:
                    # Evitar raíces duplicadas
                    if not any(abs(c - r) < error for r in raices):
                        raices.append(c)
                    break
                
                # Actualizar los limites del intervalo
                if fa * fc < 0:
                    b = c  # Actualiza el limite superior
                    fb = fc
                else:
                    a = c  # Actualiza el limite inferior
                    fa = fc

    mensaje.append(f"\nRaices encontradas: {[f'{r:.6f}' for r in raices]}\n")
    mensaje.append(f"Numero total de iteraciones: {iteraciones_totales}")

    return raices, mensaje