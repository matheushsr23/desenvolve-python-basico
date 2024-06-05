frase = input("Digite uma frase: ")

vogais = 'aeiouAEIOU'

lista_vogais = sorted([char for char in frase if char in vogais])
lista_consoantes = [char for char in frase if char.isalpha() and char not in vogais]

print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)
