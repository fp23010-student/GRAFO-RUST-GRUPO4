#include <iostream>
#include "pounter_utils.h"

using namespace std;
int main(int argc, char const *argv[]){
    int* punter = crearPunter(50);
    mostrarPunter(punter);
    liberarPunter(punter);
    return 0;
}