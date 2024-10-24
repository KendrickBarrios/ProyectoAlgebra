import matriz

def generarIdentidad(mat):
    identidad = []
    for i in range(len(mat)):
        identidad.append([])
        for j in range(len(mat[0])):
            if i == j:
                identidad[i].append(1)
            else:
                identidad[i].append(0)
    return identidad


def calcularInversa(mat, inv):
    filas = len(mat)
    columnas = len(mat[0])
    
    for j in range(filas):
        # Buscar el pivote
        pivote = mat[j][j]
        if pivote == 0:
            # Si el pivote es cero, buscar una fila debajo para intercambiar
            for i in range(j + 1, filas):
                if mat[i][j] != 0:
                    mat[j], mat[i] = mat[i], mat[j]
                    inv[j], inv[i] = inv[i], inv[j]
                    mensaje = f"f{i + 1} <-> f{j + 1}"
                    print(mensaje)
                    print("-"*(len(mensaje) - 1), end=">\n\n")
                    matriz.mostrarMatrizInvertible(mat, inv)
                    pivote = mat[j][j]
                    break
        
        # Hacer que el pivote sea 1
        if pivote != 1:
            mensaje = f"f{j + 1} -> f{j + 1}/({pivote})"
            print(mensaje)
            print("-"*(len(mensaje) - 1), end=">\n\n")
            for k in range(columnas):
                mat[j][k] /= pivote
                inv[j][k] /= pivote
            matriz.mostrarMatrizInvertible(mat, inv)
        
        # Hacer ceros en la columna del pivote
        for i in range(filas):
            if i != j:
                factor = mat[i][j]
                mensaje = f"f{i + 1} -> f{i + 1} - ({factor})f{j + 1}"
                print(mensaje)
                print("-"*(len(mensaje) - 1), end=">\n\n")
                for k in range(columnas):
                    mat[i][k] -= factor * mat[j][k]
                    inv[i][k] -= factor * inv[j][k]
                matriz.mostrarMatrizInvertible(mat, inv)
                
    return inv