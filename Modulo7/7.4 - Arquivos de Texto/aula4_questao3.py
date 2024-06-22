import re

with open("estomago.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Primeiras 25 linhas:")
for line in lines[:25]:
    print(line.strip())

print(f"\nNúmero de linhas: {len(lines)}")

max_length_line = max(lines, key=len)
print(f"\nLinha com maior número de caracteres: {max_length_line.strip()}")

nonato_count = sum(len(re.findall(r'\bNonato\b', line, re.I)) for line in lines)
iria_count = sum(len(re.findall(r'\bÍria\b', line, re.I)) for line in lines)
print(f"\nNúmero de menções a 'Nonato': {nonato_count}")
print(f"Número de menções a 'Íria': {iria_count}")
