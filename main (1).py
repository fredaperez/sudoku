"Freda Maria Perez Novelo"
"Trabajo final"

def es_valido(tablero, fila, col, num):
    """
    Verifica si el número puede colocarse en la celda dada.
    """
    # Verificar fila y columna
    for i in range(9):
        if tablero[fila][i] == num or tablero[i][col] == num:
            return False
    # Verificar subcuadrante
    inicio_fila, inicio_col = 3 * (fila // 3), 3 * (col // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if tablero[i][j] == num:
                return False
    return True

def resolver_sudoku(tablero):
    """
    Resuelve el Sudoku utilizando backtracking.
    """
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:  # Encontrar celda vacía
                for num in range(1, 10):  # Probar números del 1 al 9
                    if es_valido(tablero, fila, col, num):
                        tablero[fila][col] = num
                        if resolver_sudoku(tablero):  # Continuar con la siguiente celda
                            return True
                        tablero[fila][col] = 0  # Retroceso
                return False  # No hay solución válida
    return True

def imprimir_tablero(tablero):
    """
    Imprime el tablero de Sudoku.
    """
    for fila in tablero:
        print(" ".join(str(num) if num != 0 else "." for num in fila))

# Ejemplo de Sudoku
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku inicial:")
imprimir_tablero(sudoku)
if resolver_sudoku(sudoku):
    print("\nSudoku resuelto:")
    imprimir_tablero(sudoku)
else:
    print("No tiene solución.")
