#include <iostream>
using namespace std;

void add(int a) {
    a += 10;
}

void add(int &a) {
    a += 10;
}

void greet(string name = "student") {
    cout << "Hello, " + name << endl;
}

int main() {
    int number = 100;
	
	add(number);
	cout << number << endl;
	
	add(number);
	cout << number << endl;
	
	greet();
	
    return 0;
}
