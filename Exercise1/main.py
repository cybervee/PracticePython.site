#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:

#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = input("Give me your name: ")
age  = int(input("Give me your age: "))
print("\nYour name is " + name + " and you'll be 100 years old in " + str(((100 - age) + 2020)))
print("Your name is " + name + " and you're " + str(age) + " years old")

number = int(input("\nGive me a number: "))
print(number * ("Your name is " + name + " and you're " + str(age) + " years old"))

print(number * ("\nYour name is " + name + " and you're " + str(age) + " years old"))
