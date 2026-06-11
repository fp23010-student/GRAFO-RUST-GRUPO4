#include <iostream>
using namespace std;

// Nodo de lista simplemente enlazada
class NodoSimple {
public:
    int valor;
    NodoSimple* sig;
    NodoSimple(int v) : valor(v), sig(nullptr) {}
};

// Nodo de lista doblemente enlazada
class NodoDoble {
public:
    int valor;
    NodoDoble* ant;
    NodoDoble* sig;
    NodoDoble(int v) : valor(v), ant(nullptr), sig(nullptr) {}
};

// Lista simplemente enlazada
class ListaSimple {
public:
    NodoSimple* cabeza;
    ListaSimple() : cabeza(nullptr) {}

    // Insertar al final (no recursivo)
    void insertarFinal(int v) {
        NodoSimple* nuevo = new NodoSimple(v);
        if (!cabeza) {
            cabeza = nuevo;
        } else {
            NodoSimple* temp = cabeza;
            while (temp->sig) temp = temp->sig;
            temp->sig = nuevo;
        }
    }

    // Imprimir lista (iterativo)
    void imprimir() {
        NodoSimple* temp = cabeza;
        cout << "Lista simple: ";
        while (temp) {
            cout << temp->valor;
            if (temp->sig) cout << " -> ";
            temp = temp->sig;
        }
        cout << endl;
    }
};

// Función recursiva para convertir e invertir la lista simple en doble
NodoDoble* convertir_Invertir(NodoSimple* cabeza, NodoDoble*& anterior) {
    if (!cabeza) return nullptr;
    NodoDoble* nuevo = new NodoDoble(cabeza->valor);
    NodoDoble* siguiente = convertir_Invertir(cabeza->sig, anterior);
    if (siguiente) {
        siguiente->ant = nuevo;
        nuevo->sig = siguiente;
    }
    anterior = nuevo; // El último nodo creado será el primero de la doble
    return nuevo;
}

// Imprimir lista doblemente enlazada
void imprimirDoble(NodoDoble* cabeza) {
    cout << "Lista doble: ";
    NodoDoble* temp = cabeza;
    while (temp) {
        cout << temp->valor;
        if (temp->sig) cout << " <-> ";
        temp = temp->sig;
    }
    cout << endl;
}

int main() {
    ListaSimple lista;
    // Insertar 5 elementos: 1 -> 2 -> 3 -> 4 -> 5
    for (int i = 1; i <= 5; i++) lista.insertarFinal(i);

    lista.imprimir();

    // Convertir e invertir la lista simple en doble
    NodoDoble* anterior = nullptr;
    NodoDoble* cabezaDoble = convertir_Invertir(lista.cabeza, anterior);

    imprimirDoble(anterior); // anterior apunta al nuevo inicio (5)

    // Liberar memoria de la lista doble
    NodoDoble* temp;
    while (anterior) {
        temp = anterior;
        anterior = anterior->sig;
        delete temp;
    }
    // Liberar memoria de la lista simple
    NodoSimple* tempS;
    while (lista.cabeza) {
        tempS = lista.cabeza;
        lista.cabeza = lista.cabeza->sig;
        delete tempS;
    }
    return 0;
}