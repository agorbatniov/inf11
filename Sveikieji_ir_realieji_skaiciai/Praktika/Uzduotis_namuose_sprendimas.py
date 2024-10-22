# Funkcija, kuri konvertuoja sveikąjį skaičių į realųjį
def int_to_float(n):
    return float(n)

# Funkcija, kuri konvertuoja realųjį skaičių į sveikąjį
def float_to_int(n):
    return int(n)

# Vartotojo įvedimas
sveikas_skaicius = int(input("Įveskite sveikąjį skaičių: "))
realus_skaicius = float(input("Įveskite realųjį skaičių: "))

# Konvertavimas ir rezultatų spausdinimas
print(f"Sveikasis skaičius konvertuotas į realųjį: {int_to_float(sveikas_skaicius)}")
print(f"Realusis skaičius konvertuotas į sveikąjį: {float_to_int(realus_skaicius)}")
