import random

n = 1000
list = [random.randint(0, 1000000) for _ in range(n)]
print("Liste non triée :\n", list)

list_bubble = list.copy()
n_bubble = len(list_bubble)
for i in range(n_bubble-1):
  for j in range(n_bubble-i-1):
    if list_bubble[j] > list_bubble[j+1]:
      list_bubble[j], list_bubble[j+1] = list_bubble[j+1], list_bubble[j]

print("\nBubble liste triée :\n" , list_bubble)