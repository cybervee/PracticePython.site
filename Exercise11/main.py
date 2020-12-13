#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

def get_number():
  return int(input("Give me a number: "))

def prime_number(number):
  list_of_divisors = []
  i = 1
  while i <= number:
    if number % i == 0:
      list_of_divisors.append(i)
      i += 1
    else:
      i += 1
  if len(list_of_divisors) == 2:
    print("Prime number!")
  else:
    print("Not a prime number!")

number = get_number()
prime_number(number)