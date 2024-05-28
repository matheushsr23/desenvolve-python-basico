import random

lista_original = [random.randint(-100, 100) for _ in range(20)]

lista_ordenada = sorted(lista_original)

indice_maior_valor = lista_original.index(max(lista_original))

indice_menor_valor = lista_original.index(min(lista_original))

print("Lista ordenada:", lista_ordenada)
print("Lista original:", lista_original)
print("Índice do maior valor:", indice_maior_valor)
print("Índice do menor valor:", indice_menor_valor)
