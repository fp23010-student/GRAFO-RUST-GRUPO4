#include <iostream>
#include <string>
using namespace std;

struct Estudiante {
    int id;
    string nombre;
    float notas[4];
    float notaFinal;
    Estudiante* sig;
};

void insertarFinal(Estudiante*& lista, int id, string nombre, float notas[4]) {
    float suma = 0;
    for (int i = 0; i < 4; i++) suma += notas[i];
    float notaFinal = suma / 4;
    if (!lista) {
        lista = new Estudiante{id, nombre, {notas[0], notas[1], notas[2], notas[3]}, notaFinal, nullptr};
    } else {
        insertarFinal(lista->sig, id, nombre, notas);
    }
}

void mostrarLista(Estudiante* lista) {
    if (lista) {
        cout << "ID: " << lista->id << ", Nombre: " << lista->nombre << ", Notas: ";
        for (int i = 0; i < 4; i++) cout << lista->notas[i] << " ";
        cout << "-> Nota final: " << lista->notaFinal << endl;
        mostrarLista(lista->sig);
    }
}

Estudiante* buscarPorID(Estudiante* lista, int id) {
    if (!lista) return nullptr;
    if (lista->id == id) return lista;
    return buscarPorID(lista->sig, id);
}

void eliminarPorID(Estudiante*& lista, int id) {
    if (!lista) return;
    if (lista->id == id) {
        Estudiante* temp = lista;
        lista = lista->sig;
        delete temp;
    } else {
        eliminarPorID(lista->sig, id);
    }
}

float sumaNotasFinales(Estudiante* lista) {
    if (!lista) return 0;
    return lista->notaFinal + sumaNotasFinales(lista->sig);
}
int contarEstudiantes(Estudiante* lista) {
    if (!lista) return 0;
    return 1 + contarEstudiantes(lista->sig);
}
float promedioGeneral(Estudiante* lista) {
    int total = contarEstudiantes(lista);
    if (total == 0) return 0;
    return sumaNotasFinales(lista) / total;
}

int main() {
    Estudiante* lista = nullptr;
    int opcion;
    int idAuto = 1;
    do {
        cout << "\n--- MENU ---\n";
        cout << "1. Insertar estudiante\n";
        cout << "2. Mostrar todos los estudiantes\n";
        cout << "3. Buscar estudiante por ID\n";
        cout << "4. Eliminar estudiante por ID\n";
        cout << "5. Mostrar promedio general y notas finales\n";
        cout << "0. Salir\n";
        cout << "Seleccione una opcion: ";
        cin >> opcion;
        cin.ignore();

        if (opcion == 1) {
            string nombre;
            float notas[4];
            cout << "Nombre: "; getline(cin, nombre);
            for (int i = 0; i < 4; i++) {
                cout << "Nota " << (i + 1) << ": ";
                cin >> notas[i];
            }
            cin.ignore();
            insertarFinal(lista, idAuto, nombre, notas);
            cout << "Estudiante insertado con ID: " << idAuto << endl;
            idAuto++;
        } else if (opcion == 2) {
            cout << "\nLista de estudiantes:\n";
            mostrarLista(lista);
        } else if (opcion == 3) {
            int id;
            cout << "Ingrese el ID a buscar: "; cin >> id; cin.ignore();
            Estudiante* encontrado = buscarPorID(lista, id);
            if (encontrado) {
                cout << "ID: " << encontrado->id << ", Nombre: " << encontrado->nombre << ", Notas: ";
                for (int i = 0; i < 4; i++) cout << encontrado->notas[i] << " ";
                cout << "-> Nota final: " << encontrado->notaFinal << endl;
            } else {
                cout << "Estudiante no encontrado.\n";
            }
        } else if (opcion == 4) {
            int id;
            cout << "Ingrese el ID a eliminar: "; cin >> id; cin.ignore();
            eliminarPorID(lista, id);
            cout << "Si existía, el estudiante fue eliminado.\n";
        } else if (opcion == 5) {
            cout << "\nLista de estudiantes y sus notas finales:\n";
            mostrarLista(lista);
            cout << "Promedio general de notas finales: " << promedioGeneral(lista) << endl;
        }
    } while (opcion != 0);

    while (lista) {
        Estudiante* temp = lista;
        lista = lista->sig;
        delete temp;
    }
    return 0;
}