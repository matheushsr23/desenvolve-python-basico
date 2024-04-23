classe = input('Escolha sua classe (warrior, mage, archer): ')
strength = int(input('Digite sua força: '))
magic = int(input('Digite sua magia: '))

if classe == 'mage' and strength < 11 and magic >= 15:
    print('Pontos de atributos consistentes com a classe escolhida:', classe)
elif classe == 'warrior' and strength >= 15 and magic < 11:
    print('Pontos de atributos consistentes com a classe escolhida:', classe)
elif classe == 'archer' and 5 < strength < 15 and 5 < magic < 15:
    print('Pontos de atributos consistentes com a classe escolhida:', classe)
else:
    print('Os pontos de atributos não são consistentes com a classe escolhida.')
