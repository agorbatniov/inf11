#include <iostream>
using namespace std;

int main() {
	for (int i = 0; i < 3; i++) {  // Išorinė ciklo iteracija
		for (int j = 0; j < 2; j++) {  // Vidinė ciklo iteracija
			cout << "i: " << i << ", j: " << j << endl;
		}
	}

    return 0;
}
