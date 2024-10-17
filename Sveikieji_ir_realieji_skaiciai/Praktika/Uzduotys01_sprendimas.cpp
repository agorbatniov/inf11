#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Įveskite pirmą sveikąjį skaičių: ";
    cin >> a;
    cout << "Įveskite antrą sveikąjį skaičių: ";
    cin >> b;

    int suma = a + b;
    int skirtumas = a - b;
    int sandauga = a * b;

    cout << "Suma: " << suma << endl;
    cout << "Skirtumas: " << skirtumas << endl;
    cout << "Sandauga: " << sandauga << endl;

    return 0;
}
