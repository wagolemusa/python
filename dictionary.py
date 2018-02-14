recipes = {'Gilled salmon':['take out the pan', 'turn on the stave']}
#adding item in the dectionary
recipes ['food'] = ['posh', 'rice', 'matooke']

#printing all the recipes
print recipes

for recipe in recipes:
     for step in recipes[recipe]:
          print(step)
