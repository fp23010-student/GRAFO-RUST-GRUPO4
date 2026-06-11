#include <iostream>
using namespace std;

bool esPalindromo(const string& palabra) {
    int inicio = 0;
    int fin = palabra.length() - 1;

    while (inicio < fin) {
        if (palabra[inicio] != palabra[fin]) {
            return false; // No es un palíndromo
        }
        inicio++;
        fin--;
    }
    return true; // Es un palíndromo
}

int main(){
    string palabra;
    cout << "Ingrese una palabra: ";
    cin >> palabra;
    if(esPalindromo(palabra)){
        cout << "La palabra '" << palabra << "' es un palíndromo." << endl;
    } else {
        cout << "La palabra '" << palabra << "' no es un palíndromo." << endl;

    }

}