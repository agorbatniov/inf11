def sub(a, b):
    return a - b

def sum(a, b):
    return (a + b)


try:
    assert sum(2, 3) == 5, f"Klaida vykdant funkciją 'sum()'. Atsakymas turi būti {5}" 
    assert sub(17, 10) == 7, f"Klaida vykdant funkciją 'sub()'. Atsakymas turi būti {7}" 
    print(f'Visi testai yra sėkmingi')
except AssertionError as klaida:
    sekmingi = False
    print(f"Testas: {klaida}")



