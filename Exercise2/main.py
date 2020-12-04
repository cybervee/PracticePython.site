#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Give me a number: "))
if(number % 2 == 0):
  print("\nThe number " + str(number) + " is even.")
  if(number % 4 == 0):
    print("It's also a multiple of 4.")
  else:
    print("It's not a multiple of 4.")
else:
  print("\nThe number " + str(number) + " is odd.")

num = int(input("\nGive me another number: "))
check = int(input("And another one: "))
if(check % num == 0):
  print("\n" + str(check) + " divides evenly into " + str(num))
else:
  print("\n" + str(check) + " doesn't divides evenly into " + str(num))
