n = int(input('Quantidade de experimentos feitos: '))
cont = 1 
soma_sapo, soma__rato, soma_coelho = 0,0,0

while cont < n:
    quant = int(input(f'Quantidade de cobaias usadas no experimento {cont}: '))
    tipo = input('Digite o tipo da cobaia (Sapo = S, Rato = R, Coelho = C): ')
    if tipo == 's': 
        soma_sapo += quant 
    if tipo == 'r': 
        soma__rato += quant 
    if tipo == 'c': 
        soma_coelho += quant 
    
    print('Total de cobaias: ', soma_coelho + soma__rato + soma_sapo)
    print('Total de sapos', soma_sapo)
    print('Total de ratos', soma__rato)
    print('Total de coelhos', soma_coelho)
    
    cont += 1

