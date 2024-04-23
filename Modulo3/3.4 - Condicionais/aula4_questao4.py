weight = float(input('Digite o peso do pacote: '))
distance = float(input('Digite a distância que será percorrida em km: '))

if distance < 100:
    frete = 1 * weight 
    if weight > 10:
        frete =  frete + 10
    print(f'O valor do frete é: R$ {frete}')

elif 100 <= distance < 300:
    frete = 1.50 * weight 
    if weight > 10:
        frete = frete + 10
    print(f'O valor do frete é: R$ {frete}')

elif distance >= 300:
    frete = 2 * weight 
    if weight > 10:
        frete = frete + 10
    print(f'O valor do frete é: R$ {frete}')
