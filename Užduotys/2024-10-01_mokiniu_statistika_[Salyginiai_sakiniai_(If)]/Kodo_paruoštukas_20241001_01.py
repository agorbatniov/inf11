def ar_berniukas(mokinys):
    return True

mokiniai = ['Degutis Edvardas', 'Stankevičius Egidijus', 'Poskevičius Algirdas', 
'Žardeckas Nedas', 'Lukoševičiūtė Vygantė', 'Navickienė Skaiva', 'Sokolnikienė Irma']
mergaites = []

for mokinys in mokiniai:
    if not ar_berniukas(mokinys):
        mergaites.append(mokinys)
        
    
print(mergaites) 