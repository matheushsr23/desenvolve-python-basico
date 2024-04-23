idadeplayer = int(input('Qual sua idade?: '))

numbgames = int(input('Já jogou quantos jogos de tabuleiro?: '))

numbwins = int(input('Já venceu quantos jogos?: '))

verify =(idadeplayer > 15 and idadeplayer < 19 ) and ( numbgames > 2 ) and (numbwins > 0)


print(f"Passe para o clube: {verify}")