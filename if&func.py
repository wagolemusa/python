def count_small(numbers):
     total = 0
     for n in numbers:
          if n < 16:
               total = total + 1
     return total
lost = [4,8,15,23,42]
small = count_small(lost)

print (small)
