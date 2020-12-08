#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

string = input("Write something: ")
if string[::-1] == string[:]:
  print("That's a palindrome!")
else:
  print("That's not a palindrome!")