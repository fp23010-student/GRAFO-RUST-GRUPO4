#include "EvaluadorPostfijo.h"
#include <cctype>
#include <iostream>

bool EvaluadorPostfijo::esOperador(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

int EvaluadorPostfijo::aplicarOperacion(int a, int b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/':
            if (b == 0) {
                std::cout << "Error: no se puede dividir entre cero.\n";
                huboError = true;
                return 0;
            }
            return a / b;
    }
    return 0;
}

int EvaluadorPostfijo::evaluar(const std::string& expr) {
    huboError = false;
    Pila pila;

    for (char c : expr) {

        // número de un dígito
        if (isdigit(c)) {
            pila.push(c - '0');
            continue;
        }

        // operador
        if (esOperador(c)) {

            if (pila.vacia()) {
                std::cout << "Error: faltan operandos.\n";
                huboError = true;
                return 0;
            }
            int b = pila.pop();

            if (pila.vacia()) {
                std::cout << "Error: faltan operandos.\n";
                huboError = true;
                return 0;
            }
            int a = pila.pop();

            int r = aplicarOperacion(a, b, c);
            if (huboError) return 0;

            pila.push(r);
            continue;
        }

        // caracter no permitido
        std::cout << "Error: caracter no valido.\n";
        huboError = true;
        return 0;
    }

    // al final debe quedar solo un número
    if (pila.vacia()) {
        std::cout << "Error: expresion incompleta.\n";
        huboError = true;
        return 0;
    }

    int resultado = pila.pop();

    if (!pila.vacia()) {
        std::cout << "Error: sobran operandos.\n";
        huboError = true;
        return 0;
    }

    return resultado;
}
