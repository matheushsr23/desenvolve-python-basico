compm2 =  int(input('Digite o comprimento em m2 do seu terreno: '))

#Armazena o comprimento em m2 em uma variavel do tipo int

largm2 =  int(input('Digite a largura em m2 do seu terreno: '))

#Armazena a largura em m2 em uma variavel do tipo int

precom2 =  float(input('Digite o preço do m2 na sua região: '))

#Armazena o preço do m2 da região em uma variavel do tipo float 

aream2 = compm2 * largm2 

#Calcula a area em m2 com base nos dados anteriormente solicitados

preco_total = aream2 * precom2 

#Calcula o preço total do terreno baseado nos dados anteriormente solicitados

print(f'O terreno possui: {aream2}m2, e custa R$:{preco_total} .')

#Exibe ao usuáro a area do terreno e seu respectivo preço 