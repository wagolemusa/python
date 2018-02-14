#Make a function abbreviator that, given a string, returns the string
#if the string is less than 5 charactors, Otherwise, return the first
#four characters of the string, followed by a "."

#>>>>>>abbreviator("Trinket")
#Trin.
#>>>>>>>>abbreviator("argh!")
#argh!


def abbreviator(string):
     if len(string) < 5:
          return string
     else:
          return string[0:4] + "."

print abbreviator("Trinket")
print abbreviator("arg")
