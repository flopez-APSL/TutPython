from collections import deque # lista en forma de cola.
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
print("Handling", d.pop())
print(d)


# manipulación de listas ordenadas.
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

# para trabajar con valores bajos de una lista dada.

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
heappush(data, 0.5)                 # add a new entry
result = [heappop(data) for i in range(4)]  # fetch the four smallest entries

print(result)




