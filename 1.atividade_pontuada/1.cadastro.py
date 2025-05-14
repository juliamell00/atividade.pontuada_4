import os
import time
import csv
from dataclasses import dataclass

lista_funcionarios = []

def limpando_terminal():
    os.system ("cls || clear")

def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        return True
    return False

#Criar uma classe chamada Funcionario para representar as informações de cada funcionário solicitando: nome, cpf, cargo, salário. Cada objeto na lista de funcionários será uma instância desta classe.
@dataclass
class Funcionario:
    nome: str
    cpf: str
    cargo: str
    salario: float

def cadastrando(lista_funcionarios):
    funcionarios = Funcionario(
        nome = input("Digite o nome: "),
        cpf = input("Digite o cpf: "),
        cargo = input("Digite o cargo: "),
        salario = float(input("Digite a Salário: ")))
    
    lista_funcionarios.append(funcionarios)

def listando(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("\nA lista está vazia.")
        return
        
    for funcionarios in lista_funcionarios:
        print(f"-Nome: {funcionarios.nome},\n CPF: {funcionarios.cpf},\n Cargo: {funcionarios.cargo},\n Salário: {funcionarios.salario} ")

def atualizando(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("\nA lista está vazia.")
        return
    nome_antigo = input("Digite o nome que deseja atualizar: ")

    # Buscar o índice do funcionário com base no nome

    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_antigo:
            novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
            novo_cpf = input(f"Digite o novo CPF para {nome_antigo}: ")
            novo_cargo = input(f"Digite o novo cargo para {nome_antigo}: ")
            novo_salario = input(f"Digite o novo salário para {nome_antigo}: ")

            funcionario.nome = novo_nome
            funcionario.cpf = novo_cpf
            funcionario.cargo = novo_cargo
            funcionario.salario = novo_salario

            print(f"\n{nome_antigo} foi atualizado para {novo_nome}.")
            break
    else:
        print(f"\nO nome {nome_antigo} não foi encontrado.")

def excluindo(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("\nA lista está vazia.")
        return
     
    listando(lista_funcionarios)
    funcionario_remove = input("Digite o funcionário que deseja remover: ").strip().lower()

    for i, funcionario in enumerate(lista_funcionarios):
        if funcionario.nome.strip().lower() == funcionario_remove:
            lista_funcionarios[i]
            print(f"\nFuncionário {funcionario.nome} foi removido com sucesso.")
            break
    else:
        print(f"\nO funcionário '{funcionario_remove}' não foi encontrado.")
    
    #Implementar uma função para salvar os dados da lista de funcionários em um arquivo no formato CSV (ex: funcionarios.csv).
def Salvando(lista_funcionarios):
    nome_arquivo = "funcionarios_dendezeiros.csv"
    with open(nome_arquivo, "a") as funcionarios_dendezeiros:
        for funcionario in lista_funcionarios:
            funcionarios_dendezeiros.write(f"""
        == Funcionário ==
        nome: {funcionario.nome} 
        CPf: {funcionario.cpf}   
        Cargo: {funcionario.cargo} 
        Salário: {funcionario.salario}\n""")
            funcionarios_dendezeiros.write

#Implementar uma função para carregar os dados de um arquivo CSV existente ao iniciar o sistema, populando a lista de funcionários em memória.

def Carregando(lista_funcionarios, nome_arquivo="funcionarios.csv"):
    try:
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                if len(linha) == 4:
                    nome, cpf, cargo, salario = linha
                    funcionario = Funcionario(
                        nome=nome.strip(),
                        cpf=cpf.strip(),
                        cargo=cargo.strip(),
                        salario=float(salario.strip())
                    )
                    lista_funcionarios.append(funcionario)
        print("Dados carregados com sucesso do arquivo CSV.")
    except FileNotFoundError:
        #Considerar a inclusão de tratamento de erros básicos (ex: entrada inválida do usuário, arquivo não encontrado ao carregar, etc.).
        print("Arquivo CSV não encontrado. Nenhum dado foi carregado.")
    

#implementar um menu interativo que apresente as opções disponíveis para o usuário (Cadastrar Funcionário, Listar Funcionários, Atualizar Funcionário, Excluir Funcionário, Salvar Dados, Carregar Dados, Sair).
while True:
    #Operações CRUD em Lista: Implementar as seguintes funcionalidades, operando sobre a lista de funcionários:

    #Create (Cadastrar): Adicionar um novo funcionário à lista.

    #Read (Listar): Exibir a lista de todos os funcionários cadastrados ou buscar um funcionário específico.

    #Update (Atualizar): Modificar as informações de um funcionário existente na lista.

    #Delete (Excluir): Remover um funcionário da lista.
    print("""
    - Gerenciador de funcionarios -
    1 - Cadastrar Funcionário
    2 - Listar Funcionário
    3 - Atualizar Funcionário
    4 - Remover Funcionário
    5 - Salvar dados
    6 - Carregar Dados
    7 - Sair
""")
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            cadastrando(lista_funcionarios)
            print("\n Funcionário adicionado com sucesso.") 
            limpando_terminal()
        case 2:
            time.sleep(1)
            listando(lista_funcionarios)
            
        case 3:
            atualizando(lista_funcionarios)
            
        case 4:
            excluindo(lista_funcionarios)
        
        case 5:
            Salvando(lista_funcionarios)
        
        case 6:
            Carregando(lista_funcionarios)

        case 7:
            print("\nSaindo do programa.")

            break
        case _:
            #Considerar a inclusão de tratamento de erros básicos (ex: entrada inválida do usuário, arquivo não encontrado ao carregar, etc.).
            print("\nOpção inválida.\nTente novamente.")
   
    time.sleep(4)