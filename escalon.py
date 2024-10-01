import matriz

def formaEscalonada(mat):
    filas = len(mat)
    columnas = len(mat[0])

    fila_actual = 0
    for columna in range(columnas - 1):
        fila_pivote = None
        maximo = 0

        # Se encuentra la entrada de mayor valor en la columna, que se usara como pivote
        for f in range (fila_actual, filas):
            if abs(mat[f][columna]) > maximo:
                maximo = mat[f][columna]
                fila_pivote = f
        
        # Si todas las entradas de la columna son 0, se pasa a la siguiente columna
        if fila_pivote is None or maximo == 0:
            continue

        # Si la fila actual no corresponde a la fila pivote, estas se intercambian
        if fila_pivote != fila_actual:
            mensaje = f"f{fila_actual + 1} <-> f{fila_pivote + 1}"
            print(mensaje)
            print("-"*(len(mensaje) - 1), end=">\n\n")
            mat[fila_actual], mat[fila_pivote] = mat[fila_pivote], mat[fila_actual]
            matriz.mostrarMatriz(mat)
        
        # Si el pivote es diferente de 1, se convierte a 1 dividiendo cada entrada de la fila entre el pivote
        if mat[fila_actual][columna] != 1:
            pivote = mat[fila_actual][columna]
            mensaje = f"f{fila_actual + 1} -> f{fila_actual + 1}/({pivote})"
            print(mensaje)
            print("-"*(len(mensaje) - 1), end=">\n\n")
            for c in range(columnas):
                mat[fila_actual][c] /= pivote
            matriz.mostrarMatriz(mat)

        # Se convierten en 0 los valores por debajo del pivote actual
        for f in range (fila_actual + 1, filas):
            if mat[f][columna] != 0:
                factor = mat[f][columna]
                mensaje = f"f{f + 1} -> f{f + 1} - ({factor}f{fila_actual + 1})"
                print(mensaje)
                print("-"*(len(mensaje) - 1), end=">\n\n")
                for c in range(columnas):
                    mat[f][c] -= factor * mat[fila_actual][c]
                matriz.mostrarMatriz(mat)

        # Se pasa a la siguiente fila
        fila_actual += 1

    # Se reduce la matriz a su forma escalonada reducida de ser posible
    for fila in range(filas - 1, -1, -1):
        # Se encuentra el pivote de la fila actual
        columna_pivote = None
        for c in range(columnas - 1):
            if mat[fila][c] != 0:
                columna_pivote = c
                break
            
        # Si la fila no tiene entrada pivote, se busca en la siguiente fila
        if columna_pivote is None:
            continue

        # Se convierten en 0 los valores por encima de la columna actual
        for f in range(fila - 1, -1, -1):
            if mat[f][columna_pivote] != 0:
                factor = mat[f][columna_pivote]
                mensaje = f"f{f + 1} -> f{f + 1} - ({factor})f{fila + 1}"
                print(mensaje)
                print("-"*(len(mensaje) - 1), end=">\n\n")
                for c in range(columnas):
                    mat[f][c] -= factor * mat[fila][c]
                matriz.mostrarMatriz(mat)
        
    # Se verifica si existe una, infinitas o ninguna solucion
    ninguna = False
    infinitas = False

    for fila in range(filas):
        # Se verifica que no existan en consistencias del tipo 0 != 0
        if all(mat[fila][columna] == 0 for columna in range(columnas - 1)) and mat[fila][columnas - 1] != 0:
            ninguna = True
            break

    if not ninguna:
        for fila in range(filas):
            if columnas > (filas + 1) or all(mat[fila][columna] == 0 for columna in range(columnas)):
                infinitas = True
                break
    
    if ninguna:
        matriz.mostrarInconsistente(mat)
    elif infinitas:
        matriz.mostrarInfinitas(mat)
    else:
        matriz.mostrarSistema(mat)