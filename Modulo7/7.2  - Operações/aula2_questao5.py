# De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas, contanto que a primeira e a última letra estejam no lugar correto. Implemente uma função chamada embaralhar_palavras() para ajudar a testar a hipótese do Matt Davis. Sua função vai receber uma frase, embaralhar as letras internas de cada palavra e retornar a frase modificada. Dica: use a biblioteca random.

# Complete o seguinte código:
# def embaralhar_palavras(frase):
#     #### Escreva a função

# # Exemplo de uso:
# frase = "Python é uma linguagem de programação"
# resultado = embaralhar_palavras(frase)
# print(resultado)
# # Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"

import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    for i in range(len(palavras)):
        if len(palavras[i]) > 3:
            palavra = list(palavras[i][1:-1])
            random.shuffle(palavra)
            palavras[i] = palavras[i][0] + ''.join(palavra) + palavras[i][-1]
    return ' '.join(palavras)

frase = input('Digite uma frase: ')
resultado = embaralhar_palavras(frase)
print(resultado)
