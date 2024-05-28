import random
from collections import Counter

lista1 = [random.randint(0, 50) for i in range(20)]
lista2 = [random.randint(0, 50) for i in range(20)]

interseccao = []

for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao: 
        interseccao.append(elemento)

interseccao.sort()


print("lista1:", lista1)
print("lista2:", lista2)
print("Interseccao:", interseccao)

print("Contagem: ")
for elemento in interseccao:
    print(f"{elemento}: Lista 1: {lista1.count(elemento)}, Lista 2: {lista2.count(elemento)}")
