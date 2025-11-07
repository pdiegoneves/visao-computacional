from collections import Counter, deque, namedtuple
from operator import itemgetter

fruits = [
    "Maçã",
    "Banana",
    "Uva",
    "Pêra",
    "Banana",
    "Uva",
    "Maça",
    "Laranja",
    "Banana",
    "Abacaxi",
    "Tangerina",
    "Uva",
    "Pêra",
    "Banana",
]

print(fruits)
print(Counter(fruits))

game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa 23", 90.5, 8.5)
g2 = game("Residente Evil 4 Remake", 300, 10.0)

print(g1)
print(g2)

students = {"Pedro": 23, "Ana": 22, "Ronaldo": 26, "Janaína": 25}
a = sorted(students.items(), key=itemgetter(1))
print(a)


deq = deque([20, 40, 60, 80])
deq.appendleft(10)
deq.append(100)
print(deq)