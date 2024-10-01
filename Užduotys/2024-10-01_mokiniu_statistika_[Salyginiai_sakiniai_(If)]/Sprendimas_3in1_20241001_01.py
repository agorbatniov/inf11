# Funkcijos "ar_berniukas" aprašymas
def ar_berniukas(mokinys):
    # gauti paskutinę raidę
    raide = mokinys[-1]

    # Jeigu vardas baigesi S, tuomet mes radome berniuką ir IŠEINAME iš funkcijos
    if raide == "s":
        # Grąžinamas rezultatas True - reiškia radome berniuką
        return True
    
    # Jeigu kodas buvo vykdomas iki pabaigos, tai reiškia, kad berniuką neradome
    # Grąžinamas rezultatas False - neradome berniuką
    return False 
    # čia baigėsi funkcija

# Nuo čia PRASIDĖTA kodo vykdymas >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
mokiniai = ['Degutis Edvardas', 'StankevičiuscEgidijus', 'Poskevičius Algirdas', 
'Žardeckas Nedas', 'Lukoševičiūtė Vygantė', 'Navickienė Skaiva', 'Sokolnikienė Irma']
mergaites = []

for mokinys in mokiniai:
    # 'not' reiškia priešinga reikšme. Pvz. radome berniuką [funkcija ar_berniukas() grąžino True], 
    #                                       tuomet 'not ar_berniukas()' = False. 
    #                                       T.y. not True = False, not False = True
    if not ar_berniukas(mokinys):
        # jeigu ne berniukas, tai reiškia mergaitė. Įtraukiame mokinį į sąrašą
        mergaites.append(mokinys) 
        # 'if' operatoriaus pabaiga
    # čia baigėsi ciklas 'for'

# Parodame kiek įrašų rasta
print(len(mergaites))

# Parodame mergaičių sąrašą
for mergaite in mergaites:
    print(mergaite)