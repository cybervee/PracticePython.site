#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#Extras:

#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def list_list(list):
  c = []
  for element in list: #percorre a lista a
    if element not in c: #se o elemento não está dentro de c, adiciona. se ele já estiver, não adiciona. desse jeito não terá 2 números 1 (1, 1)
      c.append(element)
  return c

def list_set(list):
  c = set(list) #retorna a lista a como set, já que não aceita duplicação
  return c

def common_elements(list1, list2):
  list1 = set(list1) #converte lista 1 em set
  list2 = set(list2) #converte lista 2 em set
  list3 = list1.union(list2) #utiliza o método union de set para unir os dois sem item duplicado
  return list3

print(list_list(a))
print(list_set(a))
print(common_elements(a, b))

names = ["Michele", "Robin", "Sara", "Michele"]
names = set(names)
print(names)
names = list(names)
print(names)