def ar_berniukas(mokinys):
    return True

mokiniai = ['Edvardas Degutis', 'Egidijus Stankevič', 'Algirdas Poška', 
'Nedas Jonas Žardecko', 'Vygantė Lukoševičiūtė', 'Skaiva Navickienė', 'Irma Sokolnikienė']
mergaites = []

for mokinys in mokiniai:
    if not ar_berniukas(mokinys):
        mergaites.append(mokinys)
        
    
print(mergaites) 