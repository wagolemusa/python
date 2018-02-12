def tax(bill):
     """and %8 tax to restourant bill"""
     bill *= 1.08
     print "With tax: %f" % bill
     return bill
def tip(bill):
     """Add %15 tips to the restourant bill"""
     bill *=1.15
     print "With tip: %f" %bill
     return
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
