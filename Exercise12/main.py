#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
import random

a = [5, 10, 15, 20, 25]
b = random.sample(range(10), 5)

print(a)
print(b)

def list_first_last_elements(list):
  list_first_last_elements = [list[0], list[len(list)-1]]
  print(list_first_last_elements)

list_first_last_elements(a)
list_first_last_elements(b)
