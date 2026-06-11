#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char miNombre[] = "Luis";
    int miValor[strlen(miNombre)];
    int diferencia;

    char base = miNombre[0];

    for (int i = 0; i < strlen(miNombre); i++) {
        miValor[i] = miNombre[i];          
        diferencia = miValor[i] - base;    
        cout << miNombre[i] << " -> ASCII: " << miValor[i]
             << " | Diferencia con '" << base << "': " << diferencia << endl;
    }

    return 0;
}