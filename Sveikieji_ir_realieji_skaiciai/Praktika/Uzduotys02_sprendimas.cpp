#include <iostream>
using namespace std;

int main() {
    float a, b;
    cout << "Įveskite pirmą realųjį skaičių: ";
    cin >> a;
    cout << "Įveskite antrą realųjį skaičių: ";
    cin >> b;

    float suma = a + b;
    float skirtumas = a - b;
    float sandauga = a * b;
    float dalmuo = a / b;

    cout << "Suma: " << suma << endl;
    cout << "Skirtumas: " << skirtumas << endl;
    cout << "Sandauga: " << sandauga << endl;
    cout << "Dalmuo: " << dalmuo << endl;

    return 0;
}
