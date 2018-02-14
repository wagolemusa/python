#make a function that change the numbers that ends with ing

#>>>>> gerund_infinutive("building")

# to bulid

#>>>>>>geround_infinitive("build")

#That's not a gerund!

def gerund_intinitive(string):
     if string[-3:] == 'ing':
          return "to " + string[:-3]
     else:
          return "that is not gerund"

print gerund_intinitive(" Challenging")
print gerund_intinitive("build")
