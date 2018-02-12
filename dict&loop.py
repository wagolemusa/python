webster = {
     'glod' : 500,
     'pouch' : ['fint','twine','gemstone'],
     'backpack' :['xylophone','dagger','bedroll','bread loaf']
     }

#adding a key burlap and assinging a list to it
webster['burlap bag'] = ['apple', 'small ruby', 'three toed sloth']

for item in webster:
     print(webster[item])
