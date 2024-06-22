import os

frase = input('Digite uma frase: ')
with open("frase.txt", "w") as arquivo:
    arquivo.write(frase)

caminho_completo = os.path.abspath("frase.txt")

print('Frase salva em {}'.format(caminho_completo))

