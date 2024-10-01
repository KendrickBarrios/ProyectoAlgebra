import os
import vector
import matriz
import fractions

def sumaVectores(titulo, n = None):
    v = []
    e = []
    m = 0
    pase = False
    while not pase:
        pase = True
        try:
            m = int(input("Ingrese el numero de vectores a sumar: "))
        except ValueError:
            pase = False
            input("Debe ingresar un numero entero. Presione ENTER para continuar.")
            continue
        if m <= 1:
            pase = False
            input("El numero de vectores a sumar debe ser mayor o igual a 1. Presione ENTER para continuar.")
            
    if n is None:
        n = vector.leerDimensiones("Ingrese la cantidad de dimensiones de los vectores a sumar: ")

    os.system("cls")
    print(titulo)
    for i in range(m):
        e.append(matriz.validarCoeficiente(f"Ingrese el escalar por el que se multiplicara el vector {i}: "))
        v.append(vector.leerVector(f"Lectura del vector {i}", n))
        print()
    
    os.system("cls")
    print(titulo)
    s = []
    resultado = []
    for i in range(len(v[0])):
        suma = 0
        fila = ""

        for j in range(len(v)):
            suma += (e[j] * v[j][i])
            if i != (int(len(v) / 2)):
                fila += " "*8
            else:
                if j == 0:
                    fila += f" {str(e[j]):^6} "
                else:
                    if e[j] >= 0:
                        fila += f"+ {str(e[j]):^6}"
                    else:
                        fila += f"- {str(abs(e[j])):^6}"
            fila += f"[{str(v[j][i]):^10}] "
        if i != (int(len(v) / 2)):
            fila += " "*10 + f"[{str(suma):^10}]"
        else:
            fila += " "*4 + "=" + " "*5 + f"[{str(suma):^10}]"

        resultado.append(fila)
        s.append(suma)
    
    return v, e, s, resultado

def multVectores(titulo):
    n = vector.leerDimensiones("Ingrese la cantidad de dimensiones de los vectores a multiplicar: ")
    vLineal = vector.leerVector("Lectura del vector lineal", n)
    vColumnar = vector.leerVector("Lectura del vector columnar", n)
    s = []
    if len(vLineal) != len(vColumnar):
        os.system("cls")
        print("Las matrices no pueden multiplicarse pues no tienen el mismo numero de entradas.")
        return
    
    os.system("cls")
    print(titulo)
    print("Vector lineal = [", end=" ")
    for i in range(len(vLineal)):
        print(vLineal[i], end=" ")
        s.append(vLineal[i]*vColumnar[i])
    print("]")

    print("Vector columnar = [", end=" ")
    for i in range(len(vLineal)):
        print(vColumnar[i], end=" ")
    print("]")

    print("\nAx")
    for i in range(len(vLineal)):
        if i < len(vLineal) - 1:
            print(s[i], end=" + ")
        else:
            print(s[i])
    print(f"\nResultado final = {sum(s)}")

def productoMatrizSuma(titulo):
    
    # Lee una matriz Sin columna aumentada
    mat = matriz.leerMatriz("s")
    os.system("cls")
    # Lee los vectores, y calcula su suma
    vectores, escalares, s, resultado = sumaVectores(titulo, len(mat[0]))

    matAuv = []
    proceso1 = []
    maxAncho = 0
    maxAncho2 = 0

    # Determina el ancho maximo de las entradas de la matriz
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if len(str(mat[i][j])) > maxAncho:
                maxAncho = len(str(mat[i][j]))
            if i == 0:
                if len(str(s[j])) > maxAncho2:
                    maxAncho2 = len(str(s[j]))
    
    # Inicia la construccion del mensaje proceso1
    for i in range(len(mat)):
        linea = "["
        for j in range(len(mat[0])):
            linea += f" {str(mat[i][j]).center(maxAncho, ' ')} "
        if i != int(len(mat)/2):
            linea += f"]     [ {str(s[i]).center(maxAncho2, ' ')} ]     "
        else:
            linea += f"]  *  [ {str(s[i]).center(maxAncho2, ' ')} ]  =  "
        proceso1.append(linea)

    # Calcula el producto de la matriz por la suma, y agrega las operaciones a proceso1
    for i in range(len(mat)):
        suma = 0
        linea = ""
        for j in range(len(s)):
            if j == 0:
                linea += f"[ ({str(mat[i][j]).center(maxAncho, ' ')} * {str(s[j]).center(maxAncho, ' ')})"
            elif j == (len(s) - 1):
                linea += f" + ({str(mat[i][j]).center(maxAncho, ' ')} * {str(s[j]).center(maxAncho, ' ')}) ]"
            else:
                linea += f" + ({str(mat[i][j]).center(maxAncho, ' ')} * {str(s[j]).center(maxAncho, ' ')})"
            suma += mat[i][j] * s[j]
        proceso1[i] += linea
        matAuv.append(suma)
    
    # Determina el ancho maximo de las entradas del resultado
    maxAncho3 = 0
    for i in range(len(matAuv)):
        if len(str(matAuv[i])) > maxAncho3:
            maxAncho3 = len(str(matAuv[i]))
    
    # Agrega los resultados finales a proceso1
    for i in range(len(matAuv)):
        if i != int((len(matAuv)/2)):
            proceso1[i] += f"       [ {str(matAuv[i]).center(maxAncho3, ' ')} ]"
        else:
            proceso1[i] += f"   =   [ {str(matAuv[i]).center(maxAncho3, ' ')} ]"

    matAvectores = []
    proceso2 = []
    maxAnchoVectores = []

    # Encuentra el ancho maximo de las entradas de cada vector
    for k in range(len(vectores)):
        maxAnchoVectores.append(0)
        for i in range(len(vectores[k])):
            if len(str(vectores[k][i] * escalares[k])) > maxAnchoVectores[k]:
                maxAnchoVectores[k] = len(str(vectores[k][i] * escalares[k]))

    # Inicia la construccion del mensaje proceso 2
    for k in range(len(vectores)):
        proceso2.append([])
        for i in range(len(mat)):
            linea = "["
            for j in range(len(vectores[k])):
                linea += f" {str(mat[i][j]).center(maxAncho, ' ')} "
            if i != int(len(mat)/2):
                linea += f"]     [ {str(vectores[k][i] * escalares[k]).center(maxAnchoVectores[k], ' ')} ]     "
            else:
                linea += f"]  *  [ {str(vectores[k][i] * escalares[k]).center(maxAnchoVectores[k], ' ')} ]  =  "
            proceso2[k].append(linea)

    # Calcula los productos individuales y agrega las operaciones a las lineas de proceso2
    for k in range(len(vectores)):
        matAvectores.append([])
        for i in range(len(mat)):
            suma = 0
            linea = ""
            for j in range(len(vectores[k])):
                if j == 0:
                    linea += f"[ ({str(mat[i][j]).center(maxAncho, ' ')} * {str(vectores[k][j] * escalares[k]).center(maxAncho, ' ')})"
                elif j == (len(s) - 1):
                    linea += f" + ({str(mat[i][j]).center(maxAncho, ' ')} * {str(vectores[k][j] * escalares[k]).center(maxAncho, ' ')}) ]"
                else:
                    linea += f" + ({str(mat[i][j]).center(maxAncho, ' ')} * {str(vectores[k][j] * escalares[k]).center(maxAncho, ' ')})"
                suma += mat[i][j] * vectores[k][j] * escalares[k]
            proceso2[k][i] += linea
            matAvectores[k].append(suma)
    
    # Se encuentra el ancho maximo de las entradas de cada producto
    maxAnchoProductos = []
    for k in range(len(matAvectores)):
        maxAnchoProductos.append(0)
        for i in range(len(matAvectores[0])):
            if len(str(matAvectores[k][i])) > maxAnchoProductos[k]:
                maxAnchoProductos[k] = len(str(matAvectores[k][i]))

    # Se agregan los resultados a proceso2
    for k in range(len(proceso2)):
        for i in range(len(matAvectores[0])):
            linea = ""
            if i != int(len(matAvectores[0])/2):
                linea += f"     [ {str(matAvectores[k][i]).center(maxAnchoProductos[k], ' ')} ]"
            else:
                linea += f"  =  [ {str(matAvectores[k][i]).center(maxAnchoProductos[k], ' ')} ]"
            proceso2[k][i] += linea
    
    # Se construye el mensaje proceso 3 con la suma de los vectores resultantes
    proceso3 = []
    for k in range(len(matAvectores[0])):
        linea = ""
        for i in range(len(matAvectores)):
            if i != 0:
                if k != int(len(matAvectores[i])/2):
                    linea += f"   [ {str(matAvectores[i][k]).center(maxAnchoProductos[i], ' ')} ]"
                else:
                    linea += f" + [ {str(matAvectores[i][k]).center(maxAnchoProductos[i], ' ')} ]"
            else:
                linea += f"[ {str(matAvectores[i][k]).center(maxAnchoVectores[i], ' ')} ]"
        proceso3.append(linea)
    
    # Se termina la construccion del mensaje proceso3
    for k in range(len(proceso3)):
        if k != int(len(proceso3)/2):
            proceso3[k] += f"     [ {str(matAuv[k]).center(maxAncho3, ' ')} ]"
        else:
            proceso3[k] += f"  =  [ {str(matAuv[k]).center(maxAncho3, ' ')} ]"

    proceso3.append("\nSe cumple la propiedad distributiva.")
    return resultado, proceso1, proceso2, proceso3, matAuv, matAvectores