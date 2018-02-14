#make a function how_many that given a list of number
#and a thing name, returns a grematcally correct sentance
#describing the number of things
#
#>>>>>>how_many([5, "trinket"])
#there are 5 trinkets.
#>>>>>> how_many([1, "king"])
#There is 1 king.

def how_many(the_list):
     if the_list[0] == 1:
          return "There is " + str(the_list[0]) + " " + the_list[1] + "."
     else:
          return "There are " + str(the_list[0]) + " " + the_list[1] + "s."

print how_many([5, "trinket"])
print how_many([1, "king"])
