def clinic():
     print "You've just entered the clinic!"
     print"Do you take the door on the right or the left?"
     answer = raw_input("Type left or right and hit 'Enter',").lower()
     if answer == "left" or answer == "l":
          print"This is the verbal Abouse Room, you heep of dropping!"
     elif answer == "right" or answer == "r":
          print "of this the roow that i was telling you!"
     else:
          print "You did'nt pick left or right"
          clinic()
clinic()
