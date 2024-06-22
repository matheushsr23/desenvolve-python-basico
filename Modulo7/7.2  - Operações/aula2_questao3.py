import re

def verificar_palindromo():
    while True:
        frase = input('Digite uma frase (digite \'fim\' para encerrar): ')
        if frase.lower() == "fim":
            break
        else:
            frase_limpa = re.sub(r'\W+', '', frase).lower()
            if frase_limpa == frase_limpa[::-1]:
                print("\"{}\" é palíndromo".format(frase))
            else:
                print("\"{}\" não é palíndromo".format(frase))

verificar_palindromo()
