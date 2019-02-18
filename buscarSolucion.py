"""
		Trabajo práctico final - Programación 2
        Problema de las N Reinas - Programa en Python (Búsqueda de la solución)
		Farizano, Juan Ignacio

        Representamos un tablero de ajedrez mediante una lista bi-dimensional de enteros,
        donde cada posición está representada por una tupla de enteros (x,y) y está ocupada
        por un 0 si la misma se encuentra libre o por un 1 si en la misma se encuentra una reina.
        El tamaño del tablero y la cantidad de reinas a ubicar se representa mediante un entero
        N, es decir: el tablero es de tamaño NxN reinas, y en él se colocarán N reinas.
        El tamaño de N debe ser mayor o igual que 4 y menor o igual que 15.
"""

def crearTablero(N):
    """
    crearTablero(): int -> list[list[int]]
    Dado N, devuelve una lista bidimensional o matriz de tamaño NxN cuyos elementos
    son el entero 0 (tablero de ajedrez con ninguna pieza colocada).
    """
    
    tablero = []

    for i in range(0, N):
        tablero += [[0]*N]
        
    return tablero

def empezarResolucion(N):
    """
    empezarResolucion: int -> list[(int,int)]
    Dado N, crea el tablero de tamaño NxN, realiza la primera llamada a la función
    recursiva buscarSolucion y una vez encontrada la solución, devuelve una lista con las
    posiciones de todas las reinas ubicadas en el tablero.
    """
    
    tablero = crearTablero(N)
    solucion = []

    if (buscarSolucion(N, tablero, 0)):

        for i in range(0, N):
            solucion += [(i, tablero[i].index(1))]

    return solucion

def buscarSolucion(N, tablero, filaActual):
    """
    buscarSolucion(): int list[list[int]] int -> boolean
    Dado N, el tablero y un entero que representa la fila actual, resuelve el problema
    de las N reinas recursivamente.
    Una vez encontrada la solución, finaliza la recursión y devuelve True.
    En el rango de N permitido, no es posible que el problema no tenga solución.
    """

    columnaActual = 0
    encontrada = False

    while (encontrada == False and columnaActual < N):
        if posValida(tablero, (filaActual, columnaActual)):
            tablero[filaActual][columnaActual] = 1

            if filaActual == N-1:
                encontrada = True
            elif (buscarSolucion(N, tablero, filaActual+1)):
                    encontrada = True
            else:
                tablero[filaActual][columnaActual] = 0


        columnaActual += 1   

    return encontrada
       
def posValida(tablero, pos):
    """
    posValida(): list[list[int]] (int,int) -> boolean
    Dado el tablero y la posición de una reina en el mismo, verifica que la reina
    en esa posición no se "ataque" con otra ya ubicada previamente, si la posición
    es válida devuelve True, en caso contrario devuelve False.
    """
    
    x = pos[0]
    y = pos[1]
    valida = True
    reinasColocadas = []

    for i in range(0, x):
        reinasColocadas += [(i, tablero[i].index(1))]
    
    for reina in reinasColocadas:
        x0 = reina[0]
        y0 = reina[1]

        if ( (x == x0) or (y == y0) or (abs(x-x0) == abs(y-y0)) ):
            valida = False

    return valida

def salidaAArchivo(N, solucion):
    """
    salidaAArchivo(): int list[(int,int)] -> none
    Dado N y la lista con la solución, realiza la salida al archivo solucion.txt siguiendo
    el formato legible para verificar la solucion mediante el programa escrito en C. El texto
    sigue el formato explicado en el README.
    """
    
    with open("solucion.txt", "w") as archivo:
        archivo.write(str(N) + "\n")
        
        for i in range(0, N):
            x = solucion[i][0]
            y = solucion[i][1]
            posStr = str(x) + " " + str(y) + "\n"
            archivo.write(posStr)

def main():
    """
    main(): none -> int
    Función principal del programa, recibe N mediante un input en consola, verifica que
    el tamaño de N sea válido y empieza la resolucion.
    En caso de que la resolucion sea exitosa se realiza la salida al archivo solucion.txt
    y devuelve 0, en caso de que N sea inválido, se imprime
    un mensaje a consola y devuelve -1.
    """
    
    N = int(input("Ingrese N: "))

    if (N >= 4 and N <= 15):
        solucion = empezarResolucion(N)
        if (len(solucion) != 0):
            print("Se encontró una solución, se encuentra en el archivo de salida solucion.txt")
            salidaAArchivo(N, solucion)
            return 0
        else:
            # Este mensaje no debería verse nunca, ya que para los tamaños de N permitidos 
            # siempre hay solución
            print("No se pudo encontrar una solución.")
            return -1
    else:
        print("N inválido, finalizando programa.")
        return -1

"""
==========================================================
              LLAMADA PARA INICIAR EL PROGRAMA
==========================================================
"""
#main()

"""
==========================================================
                        TESTING
==========================================================
"""

def test_crearTablero():
    assert crearTablero(0) == []
    assert crearTablero(1) == [[0]]
    assert crearTablero(3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def test_empezarResolucion():
    assert empezarResolucion(3) == []
    assert empezarResolucion(4) == [(0, 1), (1, 3), (2, 0), (3, 2)]

def test_buscarSolucion():
    tableroTest = crearTablero(4)
    assert buscarSolucion(4, tableroTest, 0) == True

    tableroTest2 = [[1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert buscarSolucion(6, tableroTest2, 5) == False


def test_posValida():
    tableroTest = crearTablero(4)
    tableroTest[0][0] = 1

    assert posValida([[0]], (0,0)) == True
    assert posValida(tableroTest, (1,0)) == False
    assert posValida(tableroTest, (1,1)) == False
    assert posValida(tableroTest, (1,3)) == True