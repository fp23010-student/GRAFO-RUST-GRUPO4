#include <iostream>
using namespace std;
int main() {
    int numero;
    int conteoDivisores = 0;
    cout << "Ingrese un numero: ";
    cin >> numero;

    if (numero<=0) {
        cout << "el numero debe ser positivo"<< endl;
        return 1;
    }
    cout << "los divisores de" << numero << "son: ";
    for(int i = 1; i <= numero; i++) {
        if (numero % i == 0) {
            cout << i << " ";
        }
    }
    cout << endl;
    cout<<"fin del programa"<< conteoDivisores <<endl;
    if(conteoDivisores==2){
        cout<< numero << "el numero es primo"<<endl;
    } else
        cout<< numero << "el numero no es primo"<<endl;
    return 0;
}