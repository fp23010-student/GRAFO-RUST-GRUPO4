#ifndef PILA_H
#define PILA_H

// Nodo simple para la pila
struct Nodo {
    int valor;
    Nodo* sig;

    Nodo(int v) : valor(v), sig(nullptr) {}
};

class Pila {
private:
    Nodo* tope;

public:
    Pila();
    ~Pila();

    void push(int v);
    int pop();
    bool vacia() const;
};

#endif
