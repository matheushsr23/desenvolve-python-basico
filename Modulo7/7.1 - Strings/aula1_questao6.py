# Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.
# Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
# Digite a palavra objetivo: amor
# Anagramas: ["amor", "mora", "ramo", "Roma"] 

from collections import Counter

def encontrar_anagramas():
    frase = input('Digite uma frase: ')
    objetivo = input('Digite a palavra objetivo: ')

    palavras = frase.split()
    objetivo_counter = Counter(objetivo.lower())
    anagramas = [palavra for palavra in palavras if Counter(palavra.lower()) == objetivo_counter]

    print('Anagramas:', anagramas)

encontrar_anagramas()


