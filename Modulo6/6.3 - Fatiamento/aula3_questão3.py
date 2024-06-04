import random

numb = [random.randint(-10, 10) for i in range(20)]

print("Original:", numb)

iniFatiaMaior, tamFatiaMaior = 0, 0
iniFatiaAtual, tamFatiaAtual = 0, 0

for i in range(len(numb)):
    print(f'Processando {i} ', numb[i])
    if numb[i] < 0: 
        tamFatiaAtual += 1 
        if tamFatiaAtual == 1:
            print('Inicio nova fatia')
            iniFatiaAtual = i 
    else:
        if tamFatiaAtual > tamFatiaMaior: 
            tamFatiaMaior = tamFatiaAtual
            iniFatiaMaior = iniFatiaAtual 
            print('Maior fatia ate agora', tamFatiaMaior)
        tamFatiaAtual = 0 

if tamFatiaAtual > tamFatiaMaior:
    tamFatiaMaior = tamFatiaAtual
    iniFatiaMaior = iniFatiaAtual

print('Maior fatia ate agora', tamFatiaMaior)

del numb[iniFatiaMaior:iniFatiaMaior + tamFatiaMaior]

print("Editada:", numb)
