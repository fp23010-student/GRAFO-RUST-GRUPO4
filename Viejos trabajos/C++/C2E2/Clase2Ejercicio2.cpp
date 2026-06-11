#include <iostream>
using namespace std;
int main() {
    int num= 42;
    int* pnum;
    pnum = &num; // Asignar la dirección de num a pnum
    cout << "Valor de num: " << num << endl;
    cout << "Dirección de num: " << &pnum << endl;
    cout << "Valor de pnum: " << pnum << endl;
    cout << "Valor apuntado por pnum: " << *pnum << endl;
    *pnum = 100; // Cambiar el valor de num a través del puntero
    cout << "Nuevo valor de num: " << num << endl;
    return 0; 
}