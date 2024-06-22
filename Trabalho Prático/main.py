import random
import string
import csv

# Função para gerar um codigo aleatório
def gerar_codigo():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(3))  # Gera um código de confirmação de 3 caracteres

# Dicionário de usuários
usuarios = {
    "001CF": {"nome": "Chefe de Equipe", "funcao": "chefe", "permissoes": ["Adicionar", "Editar", "Ler", "Deletar"]},
    "002EN": {"nome": "Engenheiro", "funcao": "engenheiro", "permissoes": ["Editar", "Ler"]},
    "003PI": {"nome": "Piloto", "funcao": "piloto", "permissoes": ["Editar", "Ler"]},
    "004IM": {"nome": "Imprensa", "funcao": "imprensa", "permissoes": ["Ler"]},
    "005PA": {"nome": "Patrocinador", "funcao": "patrocinador", "permissoes": ["Ler"]},

    #Visitantes serão adicionados pelos Chefes de Equipe logo abaixo:
}

# Adiciona um código de confirmação para cada usuário
for codigo, usuario in usuarios.items():
    usuario["codigo_confirmacao"] = gerar_codigo()

# Exibe os usuários com os códigos de confirmação
for codigo, usuario in usuarios.items():
    print(f"Código: {codigo} | Nome: {usuario['nome']} | Código de Confirmação: {usuario['codigo_confirmacao']}")


#OBS: Antes de Iniciar o login, pegue o codigo de confirmação

# Sistema de login, AHEEE!!!
def fazer_login():
    id_usuario = input('Digite seu ID: ')
    codigo_confirmacao = input('Digite o código de confirmação: ')

    if id_usuario in usuarios:
        usuario = usuarios[id_usuario]
        if codigo_confirmacao == usuario["codigo_confirmacao"]:
            return f"Login efetuado como {usuario['nome']} ({usuario['funcao']})"
        else:
            return "Código de confirmação incorreto."
    else:
        return "Usuário não encontrado. Por favor, registre-se."
print(fazer_login())

#OBS: Com isso a etapa de login foi vencida como o tutorial de um jogo né? Acho que não!! Partiremos então para o HUB DE OPÇÕES.

def HUB(): #Função resposavel pelo direcionamento entre a CL e a CD.
    print('Bem vindo! Escolha sua proxima etapa: ')
    print('1- Central de Login')
    print('2- Central de Dados')
    escolha = input('Digite aqui a sua opção de direcionamento da Phoenix Racing: ')

    if escolha == '1':
        print('Bem vindo a Central de Login')
        # Dicionário de usuários visitantes (inicialmente vazio)
        usuarios_visitantes = {}

        # Função para adicionar um usuário visitante
        def adicionar_usuario():
            nome = input("Digite o nome do usuário visitante: ")
            id_usuario = input("Digite o ID do usuário visitante: ")
            codigo_confirmacao = input("Digite o código de confirmação: ")
            usuarios_visitantes[id_usuario] = {"nome": nome, "codigo_confirmacao": codigo_confirmacao}
            print(f"Usuário {nome} adicionado com sucesso!")

        # Função para exibir a lista de usuários visitantes
        def ver_usuarios():
            print("\nLista de Usuários Visitantes:")
            for id_usuario, usuario in usuarios_visitantes.items():
                print(f"ID: {id_usuario}, Nome: {usuario['nome']}")

        # Função para editar um usuário visitante
        def editar_usuario():
            id_usuario = input("Digite o ID do usuário visitante que deseja editar: ")
            if id_usuario in usuarios_visitantes:
                novo_id = input("Digite o novo ID: ")
                novo_codigo = input("Digite o novo código de confirmação: ")
                usuarios_visitantes[id_usuario]["codigo_confirmacao"] = novo_codigo
                print(f"Usuário {usuarios_visitantes[id_usuario]['nome']} editado com sucesso!")
            else:
                print("Usuário não encontrado.")
            
        # Função para deletar um usuário visitante
        def deletar_usuario():
            id_usuario = input("Digite o ID do usuário visitante que deseja deletar: ")
            if id_usuario in usuarios_visitantes:
                del usuarios_visitantes[id_usuario]
                print("Usuário deletado com sucesso!")
            else:
                print("Usuário não encontrado.")
                
        # Menu principal
        while True:
            print("\nCentral de Login - Opções:")

            # Verifica o tipo de usuário
            tipo_usuario = input('Digite o tipo de usuário (chefe, engenheiro, piloto, imprensa ou patrocinador): ')

            if tipo_usuario == "chefe":
                print("A. Adicionar Usuário Visitante")
                print("B. Ver Usuários Visitantes")
                print("C. Editar Usuários Visitantes")
                print("D. Deletar Usuário Visitante")
                print("E. Sair")
            elif tipo_usuario in ["engenheiro", "piloto"]:
                print("B. Ver Usuários Visitantes")
                print("C. Editar Usuários Visitantes")
                print("E. Sair")
            elif tipo_usuario in ["imprensa", "patrocinador"]:
                print("B. Ver Usuários Visitantes")
                print("E. Sair")
            else:
                print("Tipo de usuário inválido. Tente novamente.")

            opcao = input("Digite o número da opção desejada: ")

            if tipo_usuario == "chefe":
                if opcao == "A":
                    adicionar_usuario()
                elif opcao == "B":
                    ver_usuarios()
                elif opcao == "C":
                    editar_usuario()
                elif opcao == "D":
                    deletar_usuario()
                elif opcao == "E":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            elif tipo_usuario in ["engenheiro", "piloto"]:
                if opcao in ["B", "C"]:
                    ver_usuarios()
                    editar_usuario()
                elif opcao == "E":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            elif tipo_usuario in ["imprensa", "patrocinador"]:
                if opcao == "B":
                    ver_usuarios()
                elif opcao == "E":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
    elif escolha == '2':
        print('Bem vindo a Central de Dados')
        # Função para adicionar um novo registro
        def adicionar_registro():
            nome_gp = input("Digite o nome do Grande Prêmio: ")
            posicao = input("Digite a posição: ")
            melhor_piloto = input("Digite o melhor piloto: ")
            ano = input("Digite o ano: ")

            with open("phoenix.csv", "a", newline="") as arquivo:
                writer = csv.writer(arquivo)
                writer.writerow([nome_gp, posicao, melhor_piloto, ano])
            print("Registro adicionado com sucesso!")

        # Função para visualizar registros
        def visualizar_registros():
            with open("phoenix.csv", newline="") as arquivo:
                reader = csv.reader(arquivo)
                # Ordenar por nome do Grande Prêmio (coluna 0)
                registros_ordenados_por_nome = sorted(reader, key=lambda x: x[0])
                # Ordenar por ano (coluna 3) em ordem decrescente
                registros_ordenados_por_ano = sorted(registros_ordenados_por_nome, key=lambda x: x[3], reverse=True)

            for linha in registros_ordenados_por_ano:
                print(", ".join(linha))

        # Função para editar um registro
        def editar_registro():
            nome_gp = input("Digite o nome do Grande Prêmio a ser editado: ")
            nova_posicao = input("Digite a nova posição: ")

            registros = []
            with open("phoenix.csv", newline="") as arquivo:
                reader = csv.reader(arquivo)
                for linha in reader:
                    if linha[0] == nome_gp:
                        linha[1] = nova_posicao
                    registros.append(linha)

            with open("phoenix.csv", "w", newline="") as arquivo:
                writer = csv.writer(arquivo)
                writer.writerows(registros)
            print("Registro editado com sucesso!")

        # Função para excluir um registro
        def excluir_registro():
            nome_gp = input("Digite o nome do Grande Prêmio a ser excluído: ")

            registros = []
            with open("phoenix.csv", newline="") as arquivo:
                reader = csv.reader(arquivo)
                for linha in reader:
                    if linha[0] != nome_gp:
                        registros.append(linha)

            with open("phoenix.csv", "w", newline="") as arquivo:
                writer = csv.writer(arquivo)
                writer.writerows(registros)
            print("Registro excluído com sucesso!")

        # Menu principal
        def main():
            print("\nCentral de Dados - Opções:")

            # Verifica o tipo de usuário
            tipo_usuario = input('Digite o tipo de usuário (chefe, engenheiro, piloto, imprensa ou patrocinador): ')
            while True:
                if tipo_usuario == "chefe":
                    print("1. Adicionar Registro")
                    print("2. Visualizar Registros")
                    print("3. Editar Registros")
                    print("4. Deletar Registros")
                    print("5. Sair")
                elif tipo_usuario in ["engenheiro", "piloto"]:
                    print("2. Visualizar Registros")
                    print("3. Editar Registros")
                    print("5. Sair")
                elif tipo_usuario in ["imprensa", "patrocinador"]:
                    print("2. Visualizar Registros")
                    print("5. Sair")
                else:
                    print("Tipo de usuário inválido. Tente novamente.")

                escolha = input("Digite o número da opção desejada: ")

                if escolha == '1':
                    adicionar_registro()
                elif escolha == '2':
                    visualizar_registros()
                elif escolha == '3':
                    editar_registro()
                elif escolha == '4':
                    excluir_registro()
                elif escolha == '5':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        if __name__ == "__main__":
            main()


    else:
        print('Serviço indisponivel no momento')
HUB()
