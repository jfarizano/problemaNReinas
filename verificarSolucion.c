/*
		Trabajo práctico final - Programación 2
        Problema de las N Reinas - Programa en C (Verificación de la solución)
		Farizano, Juan Ignacio
        
        Representamos la posición de una reina en un tablero de ajedrez mediante dos enteros, x e y.
        El tamaño del tablero y la cantidad de reinas colocadas se representa mediante un entero
        N, es decir: el tablero es de tamaño NxN reinas, y en él se encuentran N reinas.
*/

#include <stdio.h>

int leerYVerificarPosiciones(FILE *archivo, int N){
    /*
        leerYVerificarPosiciones(): file int -> int
        Dado un archivo y N, lee las N líneas del archivo siguientes a la primera, las cuales contienen las posiciones de
        las reinas. A medida que se van leyendo las líneas, se verifica que la posición de la línea actual esté dentro
        del tablero, si es así, se verifica que no se "ataque" con las reinas en las posiciones ya verificadas, si
        estas condiciones se cumplen, la posición se almacena en los arrays xPosicionesReinas e yPosicionesReinas.
        Si la solución es correcta, la función devuelve 1 (True), en caso de que una posición esté fuera del tablero,
        o una reina se "ataca" con otra, devuelve 0 (False).
    */

    int solucionCorrecta = 1, cantidadReinasColocadas = 0;
    int xPosicionesReinas[N], yPosicionesReinas[N]; // Arrays para almacenar las posiciones de las reinas
    int buff[2]; // Buffer para almacenar temporalmente las posiciones de las reinas

    while (fscanf(archivo, "%d %d", &buff[0], &buff[1]) != EOF && cantidadReinasColocadas < N){
        
        int x = buff[0], y = buff[1];
        
        if(x >= 0 && x < N  && y >= 0 && y < N){ //Verifica que la reina esté dentro del tablero
            
            xPosicionesReinas[cantidadReinasColocadas] = x;
            yPosicionesReinas[cantidadReinasColocadas] = y;
            
            for(int i = 0; i < cantidadReinasColocadas; i++){
                
                int x0 = xPosicionesReinas[i], y0 = yPosicionesReinas[i];

                if(x == x0){
                    printf("Las reinas en las posiciones (%d, %d) y (%d, %d) se atacan de forma horizontal.\n", x0, y0, x, y);                 
                    solucionCorrecta = 0;
                }else if(y == y0){
                    printf("Las reinas en las posiciones (%d, %d) y (%d, %d) se atacan de forma vertical.\n", x0, y0, x, y);
                    solucionCorrecta = 0;
                }else if(x - x0 == y - y0 || x0 - x == y -y0){ // Es lo mismo que |x-x0| == |y-y0|
                    printf("Las reinas en las posiciones (%d, %d) y (%d, %d) se atacan de forma diagonal.\n", x0, y0, x, y);
                    solucionCorrecta = 0;
                }
            }

        cantidadReinasColocadas++;

        }else{
            printf("ERROR: La posición (%d,%d) no es válida en un tablero de tamaño %dx%d, finalizando programa.\n", x, y, N, N);
            return 0;
        }
    
    }

    if (cantidadReinasColocadas != N){
        printf("Advertencia: La cantidad de reinas en el tablero no coincide con la cantidad indicada.\n");
    }

    return solucionCorrecta;
}


int main (){
    /*
        main(): none -> int
        Función principal del programa, abre el archivo solucion.txt, lee la primera línea donde
        se encuentra N, verifica que esté en el rango permitido [4,15], se verifican las posiciones
        de las reinas e imprime un mensaje a consola y devuelve 0 si la solución es correcta.
        En caso de que el archivo no exista, N sea inválido o la solución sea incorrecta, se indica
        con un mensaje en pantalla y devuelve -1.
    */

    FILE *archivo;
    int buff[2];

    // Apertura del archivo de entrada
    archivo = fopen("solucion.txt", "r");

    if (archivo != NULL){
        
        // Lectura de la primera línea con el tamaño del tablero/cantidad de reinas
        int N;
        fscanf(archivo, "%d", &N);

        if (N >= 4 && N < 16){

            if (leerYVerificarPosiciones(archivo, N)){
                printf("Solución correcta.\n");
                fclose(archivo);
                return 0;
            }else{
                printf("Solución incorrecta.\n");
                fclose(archivo);
                return -1;
            }

        }else{
            printf("ERROR: Tamaño del tablero/cantidad de reinas (N) inválido, finalizando programa.\n");
            fclose(archivo);
            return -1;
        }

    }else{
        printf("ERROR: Archivo solucion.txt no encontrado, finalizando programa.\n");
        return -1;
    }
}