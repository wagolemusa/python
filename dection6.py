inventory = {
     'glod' : 500,
     'pouch' : ['fint','twine','gemstone'],
     'backpack' :['xylophone','dagger','bedroll','bread loaf']
     }

#adding a key burlap and assinging a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three toed sloth']

#Sorting the list found under the  key pouch
inventory['pouch'].sort()

# your code
inventory['pocket'] = ['seahell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['glod'] = inventory['glod'] + 50

print inventory

print inventory['pouch'].sort()
