n = int(input('Numero de respondentes: '))
cont = 0

soma_idades = 0 
np = 1

while cont < n:
    print(f'Pessoa {np}')
    idades = int(input('Digite a idade: '))
    soma_idades += idades 
    cont += 1 
    np += 1

media = soma_idades // n 

print(f'A media das idades é igual a: {media}')