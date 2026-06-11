#ifndef EVALUADOR_POSTFIJO_H
#define EVALUADOR_POSTFIJO_H

#include <string>
#include "Pila.h"

class EvaluadorPostfijo {
public:
    int evaluar(const std::string& expresion);

    
    bool huboError = false;

private:
    bool esOperador(char c);
    int aplicarOperacion(int a, int b, char op);
};

#endif
