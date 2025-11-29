import random

n = 100000
list = [random.randint(0, 1000000) for _ in range(n)]


print("Liste non triée :\n", list)

list_insertion = list.copy()
n = len(list_insertion)
for i in range(1,n):
  insert_index = i
  current_value = list_insertion.pop(i)
  for j in range(i-1, -1, -1):
    if list_insertion[j] > current_value:
      insert_index = j
  list_insertion.insert(insert_index, current_value)

print("\nInsertion liste triée :\n" ,list_insertion)