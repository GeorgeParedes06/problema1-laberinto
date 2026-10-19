
N = 9
PUNTOS_MINIMOS = 23

laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3,   0, 0, 1, 0, 1, 0, 0, 1],
    [1,   1, 0, 1, 1, 1, 1, 0, 1],
    [0,   1, 0, 1, 0, 0, 1, 0, 1],
    [1,   1, 1, 1, 1, 1, 3, 1, 1],
    [3,   0, 1, 0, 0, 0, 1, 0, 1],
    [1,   1, 1, 1, 3, 1, 1, 1, 1],
    [1,   0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1],
]

INICIO = (8, 0)   # I
FIN = (0, 0)      # F

MOVIMIENTOS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def valor(f, c):
    """Devuelve el puntaje de una celda (I y F valen 1)."""
    v = laberinto[f][c]
    if v == 'I' or v == 'F':
        return 1
    return v


def imprimir_laberinto(matriz):
    for fila in matriz:
        print(" ".join(f"{str(x):>2}" for x in fila))


def es_valido(f, c, visitado):
    return (0 <= f < N and 0 <= c < N
            and valor(f, c) != 0
            and not visitado[f][c])


def resolver(f, c, puntos, visitado, camino):
    """Backtracking: devuelve los puntos si llega a F con >= 23, sino None."""
    visitado[f][c] = True
    camino.append((f, c))
    puntos += valor(f, c)

    if (f, c) == FIN:
        if puntos >= PUNTOS_MINIMOS:
            return puntos

        visitado[f][c] = False
        camino.pop()
        return None

    for df, dc in MOVIMIENTOS:
        nf, nc = f + df, c + dc
        if es_valido(nf, nc, visitado):
            resultado = resolver(nf, nc, puntos, visitado, camino)
            if resultado is not None:
                return resultado

   
    visitado[f][c] = False
    camino.pop()
    return None


def main():
    print("LABERINTO ORIGINAL")
    imprimir_laberinto(laberinto)
    print()

    visitado = [[False] * N for _ in range(N)]
    camino = []
    total = resolver(INICIO[0], INICIO[1], 0, visitado, camino)

    if total is not None:
        print("EXITO: el raton logro salir del laberinto!")
        print(f"Puntos acumulados: {total} (minimo requerido: {PUNTOS_MINIMOS})")
        print(f"Pasos dados: {len(camino) - 1}")
        print("\nCamino (fila, columna):")
        print(" -> ".join(str(p) for p in camino))

        solucion = [["." if valor(f, c) != 0 else "#" for c in range(N)] for f in range(N)]
        for (f, c) in camino:
            solucion[f][c] = "*"
        solucion[INICIO[0]][INICIO[1]] = "I"
        solucion[FIN[0]][FIN[1]] = "F"
        print("\nMATRIZ SOLUCION (* = camino, # = pared):")
        imprimir_laberinto(solucion)
    else:
        print("FRACASO: no existe un camino que sume 23 o mas puntos.")


main()