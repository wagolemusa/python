#make a function lookup_state that given a US
# state abbreviator, returns the state's name.
#
#We've given you a dictionary with
#abbreviations as keys and state names as values.
#It;s imported for you here.
states = {
     'NY' : 'New York',
     'CA' : 'California'
     }


def lookup_state(abbreviation):
     return states[abbreviation]

print lookup_state("NY")
print lookup_state("CA")
