#include <iostream>
using namespace std;

int main() {
    string nombre = "Luis";
    char base = nombre[0];
    int asciiBase = int(base);

    cout << "Construccion del nombre: " << nombre << endl;
    cout << "Base: " << base << " (ASCII " << asciiBase << ")\n" << endl;

    for (int i = 0; i < nombre.length(); i++) {
        char letra = nombre[i];
        int asciiLetra = int(letra);
        int diferencia = asciiLetra - asciiBase;

        if (diferencia == 0) {
            cout << base << " (" << asciiBase << ") = " << letra << endl;
        } else if (diferencia > 0) {
            cout << base << " (" << asciiBase << ") + " << diferencia 
                 << " = " << letra << " (" << asciiLetra << ")" << endl;
        } else {
            cout << base << " (" << asciiBase << ") - " << -diferencia 
                 << " = " << letra << " (" << asciiLetra << ")" << endl;
        }
    }

    return 0;
}