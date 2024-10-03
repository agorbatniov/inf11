#include <iostream>
using namespace std;

int main() {
	int n, suma = 0;
	cout << "Įveskite skaičių n: ";
	cin >> n;
	for (int i = 1; i <= n; i++) {
		suma += i;
	}
	cout << "Suma: " << suma << endl;

    return 0;
}