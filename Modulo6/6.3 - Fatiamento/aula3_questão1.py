numeros = []

quantnum = int(input('Digite a quantidade de números: '))

for i in range(quantnum):
    numero = int(input('Digite um número inteiro: '))
    numeros.append(numero)

print("Lista original:", numeros)

print("Os 3 primeiros elementos:", numeros[:3])

print("Os 2 últimos elementos:", numeros[-2:])

print("Lista invertida:", numeros[::-1])

print("Elementos de índice par:", numeros[::2])

print("Elementos de índice ímpar:", numeros[1::2])