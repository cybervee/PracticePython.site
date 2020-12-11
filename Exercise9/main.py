#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

a = random.randint(1, 9)
count = 0

command = input("Welcome to the Guessing Game! Type 'play' to begin a new game or 'quit' to exit: ")
while command != "quit":
  count+= 1
  b = int(input("Guess a number: "))
  if a > b:
    print("You guessed too low!")
  elif a < b:
    print("You guessed too high!")
  else:
    print("You win with " + str(count) + " tries!")
    command = input("Type 'play' to play again or 'quit' to exit: ")

