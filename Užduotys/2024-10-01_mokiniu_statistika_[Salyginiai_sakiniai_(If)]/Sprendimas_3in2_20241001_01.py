# Funkcijos "ar_mergaite" aprašymas
def ar_mergaite(mokinys):
    
    # gauti paskutinę raidę
    ilgis = len(mokinys)
    paskutine_raide = mokinys(ilgis - 1)
    
    # Jeigu vardas baigesi "s", tuomet funkcija grąžina rezultatą False(radome berniuką. Jis yra ne mergaitė. Mergaitė == False)
    if paskutine_raide == "s":
        return False
    else:
        # Jeigu vardas nesibaigesi "s", tuomet nustatome, kad mokinys yra mergaitė - grąžiname True
        return True
    # čia baigėsi funkcija    

# Nuo čia PRASIDĖTA kodo vykdymas >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
mokiniai = ['Degutis Edvardas', 'StankevičiuscEgidijus', 'Poskevičius Algirdas', 
'Žardeckas Nedas', 'Lukoševičiūtė Vygantė', 'Navickienė Skaiva', 'Sokolnikienė Irma']
mergaites = []

for mokinys in mokiniai:
    if ar_mergaite(mokinys):
        # jeigu radome mergaitę, tai įtraukiame mokinį į sąrašą
        mergaites.append(mokinys)
        # 'if' operatoriaus pabaiga
    # čia baigėsi ciklas 'for'        
    
# Parodame kiek įrašų rasta
print(len(mergaites))

# Parodame mergaičių sąrašą
for mergaite in mergaites:
    print(mergaite)