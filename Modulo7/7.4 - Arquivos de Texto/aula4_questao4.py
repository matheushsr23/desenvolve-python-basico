# Vamos fazer o jogo da forca! Antes de programar crie e salve os seguintes arquivos na mesma pasta onde você vai programar a solução: 
# Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.
# Baixe o arquivo "gabarito_enforcado.txt": https://github.com/camilalaranjeira/python-basico-exercicios/blob/main/modulo7/gabarito_enforcado.txt
# Escreva um programa em Python para executar o jogo, de acordo com as definições:
# Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
# Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
# No início exiba o número de letras da palavra sorteada como underscores;
# Permita que o jogador insira letras para adivinhar a palavra;
# Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
# Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
# Limite o número de tentativas para 6 (as partes do enforcado).

import random

def imprime_enforcado(erros):
    with open('gabarito_enforcado.txt', 'r') as arquivo:
        enforcado = arquivo.readlines()
    print(enforcado[erros])

def get_valid_input():
    while True:
        palpite = input('Digite uma letra: ').upper()
        if len(palpite) == 1 and palpite.isalpha():
            return palpite
        else:
            print("Por favor, digite apenas uma letra alfabética.")

with open('gabarito_forca.txt', 'r') as arquivo:
    palavras = arquivo.read().splitlines()

palavra_secreta = random.choice(palavras).upper()
acertos = ['_' for letra in palavra_secreta]
tentativas = 6
erros = 0

while erros < tentativas and '_' in acertos:
    print(' '.join(acertos))
    palpite = get_valid_input()

    if palpite in palavra_secreta:
        print("Acertou!")
        for indice, letra in enumerate(palavra_secreta):
            if letra == palpite:
                acertos[indice] = palpite
    else:
        print("Errou!")
        erros += 1
        imprime_enforcado(erros)

if '_' not in acertos:
    print(f'Parabéns! Você acertou a palavra: {palavra_secreta}')
else:
    print(f'Que pena! Você foi enforcado. A palavra era: {palavra_secreta}')

