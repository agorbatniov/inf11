def berniukas(mokinys):
    return True

mokiniai = ['Degutis Edvardas', 'StankevičiuscEgidijus', 'Poskevičius Algirdas', 
'Žardeckas Nedas', 'Lukoševičiūtė Vygantė', ' Navickienė Skaiva', 'Sokolnikienė Irma']
mergaites = []

for mokinys in mokiniai:
    if berniukas(mokinys):
        mergaites.append(mokinys)
        
    
print(mergaites) 