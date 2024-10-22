# Funkcija, kuri konvertuoja sveikąjį skaičių į realųjį
def to_float(n):
    return float(n)

# Funkcija, kuri konvertuoja realųjį skaičių į sveikąjį
def to_int(n):
    return int(n)

# Vartotojo įvedimas
sveikas_skaicius = to_int(input("Įveskite sveikąjį skaičių: "))
realus_skaicius = to_float(input("Įveskite realųjį skaičių: "))

# Konvertavimas ir rezultatų spausdinimas
print(f"Sveikasis skaičius konvertuotas į realųjį: {to_float(sveikas_skaicius)}")
print(f"Realusis skaičius konvertuotas į sveikąjį: {to_int(realus_skaicius)}")


is_vip = True
to_send = to_int(is_vip)
print(to_send)