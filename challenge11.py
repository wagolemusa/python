def fruit_labeler(thing):
     if type(thing) == str:
          return 'apples'
     elif type(thing) == int:
          return 'oranges'
     else:
          return 'bananas'
     
print fruit_labeler(5.9)
