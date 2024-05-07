import random 

n = random.randint(1,10)

while True:
    ans = int(input(('Adivinhe o número: ')))
    
    if ans > n:
        print('Muito alto')
    if ans < n:
        print('Muito baixo')
    if ans == n:
        break

print('Você adivinhou o numero')