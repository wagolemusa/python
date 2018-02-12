from random import randint

random_number = randint(1, 10)

guesses = 3
#start you game
while guesses > 0:
     guess = int(raw_input("please enter your Guess: "))
     if guess == random_number:
          print("You Wins!")
          break
     guesses -= 1
else:
     print("You have loses") 
