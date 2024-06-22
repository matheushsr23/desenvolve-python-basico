import re

def validador_senha(senha):
    if len(senha) < 8:
        return False
    elif not re.search("[a-z]", senha):
        return False
    elif not re.search("[A-Z]", senha):
        return False
    elif not re.search("[0-9]", senha):
        return False
    elif not re.search("[@#$]", senha):
        return False
    else:
        return True

# Exemplo de uso:
senha1 = input('Digite uma senha: ')
senha2 = input('Digite mais uma senha: ')
senha3 = input('Digite uma última senha: ')
print(validador_senha(senha1)) 
print(validador_senha(senha2))  
print(validador_senha(senha3))  




