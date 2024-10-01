pavadinimas = ['K', 'a', 'č', 'i', 'a', 'l', 'o', 'v', 'o', ' ', 'g', 'i', 'm', 'n', 'a', 'z', 'i', 'j', 'a'] 
pavadinimas.sort()
# [' ', 'K', 'a', 'a', 'a', 'a', 'g', 'i', 'i', 'i', 'j', 'l', 'm', 'n', 'o', 'o', 'v', 'z', 'č']

kiekis = 0
senaraide = ''
makskiekis = 0
dazniausia_raide = ''

for raide in pavadinimas:
    if senaraide != raide:
        
        if makskiekis < kiekis:
            makskiekis = kiekis
            dazniausia_raide = senaraide
            
        kiekis = 0
        senaraide = raide
        
    kiekis += 1  #  kiekis = kiekis + 1   
    
print("Dažniausiai pasikartuojanti raidė yra '" + dazniausia_raide + "' " + str(makskiekis))    
