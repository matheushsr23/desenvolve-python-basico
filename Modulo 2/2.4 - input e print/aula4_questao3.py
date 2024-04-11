prod1 = input('Digite o nome do produto 1: ')
prod1price = float(input('Digite o preço unitário do produto 1: '))
prod1quant = int(input('Digite a quantidade do produto 1: '))

prod2 = input('Digite o nome do produto 2: ')
prod2price = float(input('Digite o preço unitário do produto 2: '))
prod2quant = int(input('Digite a quantidade do produto 2: '))

prod3 = input('Digite o nome do produto 3: ')
prod3price = float(input('Digite o preço unitário do produto 3: '))
prod3quant = int(input('Digite a quantidade do produto 3: '))

total =  (prod1price * prod1quant) + (prod2price * prod2quant) + (prod3price * prod3quant)

print(f'O total em reais é igual a R${total}')