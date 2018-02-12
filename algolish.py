n = ["Refuge", "Wise"]
#Add your function here

def join_string(words):
     result = ''
     for word in words:
          result = result + word + ' '
     return result

print join_string(n)
