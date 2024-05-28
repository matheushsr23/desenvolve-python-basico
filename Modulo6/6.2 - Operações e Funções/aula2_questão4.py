# Função para obter uma lista de números do usuário
def obter_lista(n):
    lista = []
    for i in range(n):
        elemento = int(input(f"Digite o elemento {i+1} da lista: "))
        lista.append(elemento)
    return lista

# Obter a quantidade de elementos da lista 1
n1 = int(input("Digite a quantidade de elementos da lista 1: "))

# Obter os elementos da lista 1
print(f"Digite os {n1} elementos da lista 1:")
lista1 = obter_lista(n1)

# Obter a quantidade de elementos da lista 2
n2 = int(input("Digite a quantidade de elementos da lista 2: "))

# Obter os elementos da lista 2
print(f"Digite os {n2} elementos da lista 2:")
lista2 = obter_lista(n2)

# Combinar as listas de forma alternada
lista_intercalada = []
i, j = 0, 0

# Intercalar os elementos até o final da menor lista
while i < n1 and j < n2:
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[j])
    i += 1
    j += 1

# Adicionar os elementos remanescentes da lista 1
while i < n1:
    lista_intercalada.append(lista1[i])
    i += 1

# Adicionar os elementos remanescentes da lista 2
while j < n2:
    lista_intercalada.append(lista2[j])
    j += 1

# Imprimir a lista intercalada
print("Lista intercalada: ", lista_intercalada)
5 