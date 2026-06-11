#include <iostream>
#include "EvaluadorPostfijo.h"

using namespace std;

int main() {
    EvaluadorPostfijo eval;
    string expresion;

    cout << "Ingrese una expresion en notacion postfija: ";
    cin >> expresion;

    int resultado = eval.evaluar(expresion);

    
    if (!eval.huboError) {
        cout << "Resultado: " << resultado << endl;
    }

    return 0;
}