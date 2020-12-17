teststring = "this is a test"
result = teststring.split("t")
print(result)

txt = "welcome to the jungle"
x = txt.split("e", 2)
print(x)

listofstrings = ['a', 'b', 'c']
result = "*".join(listofstrings)
print(result)

#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#  My name is Michele
#Then I would see the string:
#  Michele is name My
#shown back to me.

def backwards_list(list):
  y = list.split()
  print(y[::-1])

x = input("Write something: ")
backwards_list(x)