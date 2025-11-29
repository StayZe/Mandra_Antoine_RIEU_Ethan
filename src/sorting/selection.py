import random

n = 100000
list = [random.randint(0, 1000000) for _ in range(n)]


print("Liste non triée :\n", list)

list_selection = list.copy()
n = len(list_selection)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
     if list_selection[j] < list_selection[min_index]:
       min_index = j
  min_value = list_selection.pop(min_index)
  list_selection.insert(i, min_value)

print("\nSelection liste triée :\n" , list_selection)