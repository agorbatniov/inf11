#include <iostream>
using namespace std;

int main() {   
    // C++ 

    int i = 1;
    while (i < 6) {
        cout << i << endl;
        if (i == 3) {
            break;
        }
        i++;
    }
}