import re

with open("frase.txt", "r") as arquivo:
    frase = arquivo.read()

frase = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕçÇ\s]', '', frase)
palavras = frase.split()

with open("palavras.txt", "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

with open("palavras.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
