n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

m = (n1 + n2 + n3) / 3 

print(m)

if m >= 60:
    print('aprovado')
    print('fim')
elif m >=40:
    print('recuperação')
    print('fim')
else:
    print('reprovado')
    print('fim')