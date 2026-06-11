#include <iostream>
#include "pounter_utils.h"

using namespace std;

int* crearPunter(int valor){
    int* numero = new int(valor);
    return numero;
}

void mostrarPunter(int* punter){
    if(punter != nullptr){
        cout << "El valor del puntero es: " << *punter << endl;
        cout << "La direccion de la variable es: " << punter << endl;
        cout << "La direccion del puntero es: " << &punter << endl;
    }
}
void liberarPunter(int* punter){
    delete punter;
}