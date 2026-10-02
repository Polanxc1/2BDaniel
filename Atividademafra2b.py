# Lista global para armazenar os dados de todos os alunos
alunos = []

def adicionar_aluno():
    nome = input("Escreva o nome do aluno: ")
    
    # Validação da idade 
    while True:
        try:
            idade = int(input(''' Digite a idade do aluno: '''))
            if idade > 0: 
                break
            print(''' A idade tem de ser um valor positivo.''')
        except ValueError:
            print(''' Erro: a idade não corresponde aos requisitos de cadastro.''')                     

    # Validação da nota (0 a 10) conforme os requisitos técnicos
    while True:
        try:
            nota = float(input(''' Digite a nota do aluno (0 a 10): '''))
            if 0 <= nota <= 10:
                break
            else:
                print(''' Erro: A nota tem de estar entre 0 e 10. ''')
        except ValueError:
            print(''' Erro: Por favor, Digite um número válido de 0 a 10. ''')

    # Guardar dados num dicionário e adicionar à lista
    novo_aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(novo_aluno)
    print(f'''Sucesso: O aluno '{nome}' foi adicionado!''')

def listar_alunos():
    if not alunos:
        print(''' Ainda não há alunos registados no sistema. ''')
        return
        
    print('''--- Lista de Alunos ---''')
    for aluno in alunos:
        print(f''' Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']} ''')

def buscar_aluno():
    nome_busca = input('''Qual é o nome do aluno que pretendes procurar? ''')
    
    for aluno in alunos:
        if aluno['nome'].lower() == nome_busca.lower():
            print("\n--- Aluno Encontrado ---")
            print(f'''Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}''')
            return
            
    print('''Erro: Aluno não encontrado na base de dados.''')

def remover_aluno():
    nome_remover = input('''Qual é o nome do aluno que pretendes remover? ''')
    
    for aluno in alunos:
        if aluno['nome'].lower() == nome_remover.lower():
            alunos.remove(aluno)
            print(f"\nSucesso: O aluno '{aluno['nome']}' foi removido da lista.")
            return
            
    print(''' Aviso: Esse aluno não existe na lista.''')

def mostrar_media():
    if not alunos:
        print(''' Não é possível calcular a média porque não há alunos registados.''')
        return
        
    soma_notas = sum(aluno['nota'] for aluno in alunos)
    media = soma_notas / len(alunos)
    print(f''' A média geral das notas de todos os alunos é: {media:.2f}''')

def menu_principal():
    # Loop principal (while True) para manter o programa a correr
    while True:
        print('''=== SISTEMA DE CADASTRO DE ALUNOS ===''')
        print("1. Adicionar aluno")
        print("2. Listar todos os alunos")
        print("3. Buscar aluno pelo nome")
        print("4. Remover aluno")
        print("5. Mostrar média geral das notas")
        print("6. Sair")
        
        opcao = input('''digite um numero de 1-6: ''')
        
        if opcao == '1':
            adicionar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            mostrar_media()
        elif opcao == '6':
            print('''A encerrar o sistema. Até logo!''')
            break
        else:
            print('''Opção inválida. Por favor, escolhe um número entre 1 e 6.''')

# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal() 
