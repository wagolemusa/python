#make a function aardvark that, gaven a string returns 'aardvark'
#if the string starts with an a. otherwise retirn 'zebra',

#>>>>>aadvark("arg")
#aardvark
#>>>>aardvark("Trinket
#Zebra

def aardvark(string):
     if string[0] == 'a':
          return "aardvark"
     else:
          return "zebra"

print aardvark("arg")
print aardvark("Trinket")
