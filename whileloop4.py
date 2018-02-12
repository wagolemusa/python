import random

print("Lucky Numbers! 3 number will be generated.")
print("If one of the them is a '5' you lose")

count = 0

while count < 3:
     num = random.randint(1, 6)
     print(num)
     if num == 4:
          print("Sorry, you lose!")
          break
     count += 1
else:
     print("You win")
