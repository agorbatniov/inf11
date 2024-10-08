#include <iostream>
using namespace std;

int main() {   
    int i = 0;
    while (i < 6) {
        i++;
        if (i == 3) {
            continue;
        }
        cout << i << endl;
    }
}