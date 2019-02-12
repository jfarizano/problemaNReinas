def crearTablero(N):
    tablero = []

    for i in range(0, N):
        tablero += [[0]*N]

    return tablero

def empezarResolucion(N):
    tablero = crearTablero(N)
    solucion = []

    buscarSolucion(N, tablero, 0)

    for i in range(0, N):
        solucion += [(i, tablero[i].index(1))]

    return solucion

def buscarSolucion(N, tablero, filaActual):
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
    x0 = pos[0]
    y0 = pos[1]
    valida = True
    reinasColocadas = []

    for i in range(0, x0):
        reinasColocadas += [(i, tablero[i].index(1))]
    
    for reina in reinasColocadas:
        x1 = reina[0]
        y1 = reina[1]

        if ( (x0 == x1) or (y0 == y1) or (abs(x1-x0) == abs(y1-y0)) ):
            valida = False

    return valida

def salidaAArchivo(N, solucion):
    with open("solucion.txt", "w") as archivo:
        archivo.write(str(N) + "\n")
        
        for i in range(0, N):
            x = solucion[i][0]
            y = solucion[i][1]
            posStr = str(x) + " " + str(y) + "\n"
            archivo.write(posStr)

def main():
    N = int(input("Ingrese N: "))

    if (N >= 4 and N < 16):
        solucion = empezarResolucion(N)
        if (len(solucion) != 0):
            print("Se encontró una solución, se encuentra en el archivo de salida solucion.txt")
            salidaAArchivo(N, solucion)
        else:
            print("No se pudo encontrar una solución.")
    else:
        print("N inválido, finalizando programa.")
        return -1
        
main()