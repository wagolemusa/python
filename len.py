pyg = 'ay'
original = raw_input("Enter your Word")
word = original.lower()
first = word[0]
if len(original) > 0 and original.isalpha():
     print original
else:
     print "no"
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]
print new_word
     
