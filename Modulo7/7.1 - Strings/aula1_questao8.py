# Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 
# O primeiro passo é calcular o primeiro dígito verificador. Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2, como no exemplo abaixo:


def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "") 
    if len(cpf) != 11 or not cpf.isdigit():
        return 'Inválido'

  
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    
    if cpf[-2:] == str(digito1) + str(digito2):
        return 'Válido'
    else:
        return 'Inválido'

cpf = input('Digite um CPF na forma XXX.XXX.XXX-XX: ')
print(validar_cpf(cpf))
