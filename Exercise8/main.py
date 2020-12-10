#quit = input('Type "enter" to quit:' )
#while quit != "enter":
#  quit = input('Type "enter" to quit:' )

#a = 5
#while (a > 0):
#  print(a)
#  a -= 1

#while True: 
#  usr_command = input("Enter your command: ")
#  if usr_command == "quit":
#    break
#  else: 
#    print("You typed " + usr_command)

#for element in range(1, 6):
#  print(element)

#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

command = input("Welcome to ROCK PAPER SCISSORS! Type 'play' to begin a new game: ")
while command != "quit":
  player_1 = input("Player 1, make your move: ")
  player_2 = input("Player 2, make your move: ")
  if player_1 == "rock":
    if player_2 == "scissors":
      print("Player 1 wins!")
    elif player_2 == "paper":
      print("Player 2 wins!")
    elif player_2 == "rock":
      print("Tie!")
  if player_1 == "scissors":
    if player_2 == "paper":
      print("Player 1 wins!")
    elif player_2 == "rock":
      print("Player 2 wins!")
    elif player_2 == "scissors":
      print("Tie!")
  if player_1 == "paper":
    if player_2 == "rock":
      print("Player 1 wins!")
    elif player_2 == "scissors":
      print("Player 2 wins!")
    elif player_2 == "paper":
      print("Tie!")
  command = input("Type 'play' to begin a new game or 'quit' to exit: ")

  