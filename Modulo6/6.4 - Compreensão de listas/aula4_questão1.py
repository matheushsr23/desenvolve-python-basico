pares_20_50 = [x for x in range(20, 51) if x % 2 == 0]

quadrados = [x**2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]

paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]

print("Números pares entre 20 e 50:", pares_20_50)
print("Quadrados dos valores de 1 a 9:", quadrados)
print("Números entre 1 e 100 divisíveis por 7:", divisiveis_por_7)
print("Paridade dos valores em range(0, 30, 3):", paridade)
