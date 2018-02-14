# make a function commafy that, given a list of three or more things
#return a list with commas

#
#>>>>commafy(["trinket", "learing", "fun"])
#>>>>>commafy(["lions", "tigers", "bears"])

#lions, tigers, and bears

def commafy(list):
     list[-1] = "and " + list[-1]
     return ', '.join(list)

print commafy(["trinket", "learing", "fun", "get"])
print commafy(["lions","tigers"])
