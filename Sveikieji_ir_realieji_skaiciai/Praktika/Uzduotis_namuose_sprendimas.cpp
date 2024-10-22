#include <iostream>
using namespace std;

// Funkcija, kuri konvertuoja sveikąjį skaičių į realųjį
float int_to_float(int n) {
    return static_cast<float>(n);
}

// Funkcija, kuri konvertuoja realųjį skaičių į sveikąjį
int float_to_int(float n) {
    return static_cast<int>(n);
}

int main() {
    int sveikas_skaicius;
    float realus_skaicius;

    // Vartotojo įvedimas
    cout << "Įveskite sveikąjį skaičių: ";
    cin >> sveikas_skaicius;

    cout << "Įveskite realųjį skaičių: ";
    cin >> realus_skaicius;

    // Konvertavimas ir rezultatų spausdinimas
    cout << "Sveikasis skaičius konvertuotas į realųjį: " << int_to_float(sveikas_skaicius) << endl;
    cout << "Realusis skaičius konvertuotas į sveikąjį: " << float_to_int(realus_skaicius) << endl;

    return 0;
}
