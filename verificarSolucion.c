/*
		Trabajo práctico final - Programación 2
        Problema de las N Reinas - Programa en C (Verificación de la solución)
		Farizano, Juan Ignacio
        
*/

#include <stdio.h>

int leerYVerificarPosiciones(FILE *archivo, int N){

    int solucionCorrecta = 1, cantidadReinasLeidas = 0;
    int xPosicionesReinas[N], yPosicionesReinas[N]; // Arrays para almacenar las posiciones de las reinas
    int buff[2]; // Buffer para almacenar temporalmente las posiciones de las reinas

    while (fscanf(archivo, "%d %d", &buff[0], &buff[1]) != EOF && cantidadReinasLeidas <= N){
        
        int x0 = buff[0], y0 = buff[1];
        
        if(x0 >= 0 && x0 < N  && y0 >= 0 && y0 < N){ //Verificar que la reina esté dentro del tablero
            
            xPosicionesReinas[cantidadReinasLeidas] = x0;
            yPosicionesReinas[cantidadReinasLeidas] = y0;
            
            for(int i = 0; i < cantidadReinasLeidas; i++){
                
                int x1 = xPosicionesReinas[i], y1 = yPosicionesReinas[i];

                if(x0 == x1){
                    printf("Solución incorrecta: La reina en la posición (%d, %d) colisiona de forma horizontal con la reina en la posición (%d, %d).\n", x0, y0, x1, y1);                 
                    solucionCorrecta = 0;
                }else if(y0 == y1){
                    printf("Solución incorrecta: La reina en la posición (%d, %d) colisiona de forma vertical con la reina en la posición (%d, %d).\n", x0, y0, x1, y1);
                    solucionCorrecta = 0;
                }else if(x1 - x0 == y1 - y0 || x1 - x0 == y0 -y1){ // Es lo mismo que |x1-x0| == |y1-y0|
                    printf("Solución incorrecta: La reina en la posición (%d, %d) colisiona de forma diagonal con la reina en la posición (%d, %d).\n", x0, y0, x1, y1);
                    solucionCorrecta = 0;
                }
            }

        cantidadReinasLeidas++;

        }else{
            printf("ERROR: La posición (%d,%d) no es válida en un tablero de tamaño %d, finalizando programa.\n", x0, y0, N);
            return 0;
        }
    
    }

    if (cantidadReinasLeidas != N){
        printf("Advertencia: La cantidad de reinas en el tablero no coincide con la cantidad indicada.\n");
    }

    return solucionCorrecta;
}


int main (){

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
                printf("Solución válida.\n");
                fclose(archivo);
                return 0;
            }else{
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