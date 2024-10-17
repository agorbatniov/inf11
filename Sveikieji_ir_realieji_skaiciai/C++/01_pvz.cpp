#include <iostream>
using namespace std;

int main() {
    // Sveikieji skaičiai
    int a, b;
    cout << "Įveskite pirmą sveikąjį skaičių: ";
    cin >> a;
    cout << "Įveskite antrą sveikąjį skaičių: ";
    cin >> b;

    int suma = a + b;
    cout << "Suma: " << suma << endl;

    // Realieji skaičiai (float)
    float x, y;
    cout << "Įveskite pirmą realųjį skaičių: ";
    cin >> x;
    cout << "Įveskite antrą realųjį skaičių: ";
    cin >> y;

    float sandauga = x * y;
    cout << "Sandauga: " << sandauga << endl;

    return 0;
}
