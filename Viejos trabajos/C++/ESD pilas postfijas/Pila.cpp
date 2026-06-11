#include "Pila.h"

// Constructor: inicia la pila vacía
Pila::Pila() {
    tope = nullptr;
}

// Destructor: libera todos los nodos
Pila::~Pila() {
    while (!vacia()) {
        pop();
    }
}

// Inserta un elemento en la parte superior
void Pila::push(int v) {
    Nodo* nuevo = new Nodo(v);
    nuevo->sig = tope;
    tope = nuevo;
}

// Elimina y devuelve el elemento superior
int Pila::pop() {
    if (vacia()) {
        return 0; // manejo simple
    }

    Nodo* aux = tope;
    int dato = aux->valor;

    tope = aux->sig;
    delete aux;

    return dato;
}

// Verifica si la pila está vacía
bool Pila::vacia() const {
    return tope == nullptr;
}