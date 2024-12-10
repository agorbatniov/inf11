#include <iostream>
#include <assert.h>

int sum(int a, int b) {
    return a + b;
}

void testCalculator() {
    // Test addition
    assert(sum(3, 2) == 5 && "Klaida vykdant funkciją 'sum()'. Atsakymas turi būti '5'");
    
    std::cout<<"Visi testai sėkmingi";
}

int main()
{
    testCalculator();
    return 0;
}