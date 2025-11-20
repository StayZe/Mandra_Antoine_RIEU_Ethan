# Exercice 2 : Structures de données
# 2.1 - Pile (stack)

stack = [1, 2, 3, 4, 5]

def stack_exercice(stack):
    print(stack)

    def stack_push(stack, item):
        stack.append(item)
        return "L'item " + str(item) + " a été ajouté à la pile"

    print(stack_push(stack, 6))
    print(stack)

    def stack_pop(stack):
        return "L'item " + str(stack.pop()) + " a été retiré de la pile"

    print(stack_pop(stack))
    print(stack)

    def stack_peek(stack):
        return "L'élément en haut de la pile est: " + str(stack[-1])
    print(stack_peek(stack))

    def is_stack_empty(stack):
        return "La pile est vide" if len(stack) == 0 else "La pile n'est pas vide"

    print(is_stack_empty(stack))

# 2.2 - File
from collections import deque

queue = deque([])

def queue_exercice(queue):
    print("La file est: " + str(queue))
    def queue_enqueue(queue, item):
        queue.append(item)
        return "L'item " + str(item) + " a été ajouté à la file"
    print(queue_enqueue(queue, 6))
    # print(queue_enqueue(queue, 7))
    print("La file est: " + str(queue))

    def queue_dequeue(queue):
        return "L'item " + str(queue.popleft()) + " a été retiré de la file"
    print(queue_dequeue(queue))
    print("La file est: " + str(queue))

    def queue_is_empty(queue):
        return "La file est vide" if len(queue) == 0 else "La file n'est pas vide"
    print(queue_is_empty(queue))

#2.3 - Heap (Min-Heap)
import heapq

heap = []
heap2 = [5, 3, 7]

def heap_exercice(heap, heap2):
    print("La heap est: " + str(heap))

    def heap_instert(heap, item):
        heapq.heappush(heap, item)
        return "L'item " + str(item) + " a été ajouté à la heap"
    print(heap_instert(heap, 5))
    print(heap_instert(heap, 3))
    print(heap_instert(heap, 7))
    print("La heap est: " + str(heap))

    def extract_min(heap):
        return "L'élément minimum est: " + str(heapq.heappop(heap)) + " a été retiré de la heap"
    print(extract_min(heap))
    print("La heap est: " + str(heap))

    def heapify(heap2):
        print("La heap2 est: " + str(heap2))
        heapq.heapify(heap2)
        return "La heap2 a été heapifiée"
    print(heapify(heap2))
    print("La heap2 est: " + str(heap2))
