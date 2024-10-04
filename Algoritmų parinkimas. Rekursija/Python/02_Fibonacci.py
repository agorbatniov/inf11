# The Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
#                         1  2  3  4  5  6  7   8   9   10  11  12

def fibonacci(n):
    # Fibonacio sekos pirmi du skaičiai yra 1. Todėl, jei prašome pirmo (n = 1) arba antro (n = 2) Fibonacio sekos skaičiaus, atsakymas yra 1
    if n <= 2:
        return 1
    else:
        # Jei prašome trečio ar vėlesnio elemento, Fibonacio sekos skaičius apskaičiuojamas pagal formulę: F(n) = F(n-1) + F(n-2)
        return fibonacci(n-1) + fibonacci(n-2)

fibo = fibonacci(8)
print(fibo)