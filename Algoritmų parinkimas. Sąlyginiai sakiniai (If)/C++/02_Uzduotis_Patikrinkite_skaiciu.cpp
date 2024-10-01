#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Įveskite skaičių: ";
    cin >> num;
    if (num > 0) {
        cout << "Teigiamas" << endl;
    }
    else if (num == 0) {
        cout << "Nulis" << endl;
    }
    else {
        cout << "Neigiamas" << endl;
    }
}