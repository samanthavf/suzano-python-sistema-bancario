"""
Sistema bancário: DEPÓSITO, SAQUE, EXTRATO

1.DEPÓSITO: depositar valores positivos para conta, todos os depósitos devem ser armazenados numa
variável e exibidos na operação de extrato.

2.SAQUE: só deve permitir 3 saques diários com limite máximo de R$500,00 por saque. Caso o utilizador não
tenha saldo em conta deve exibir uma mensagem que não será possível realizar saque por falta de saldo,
todos os saldos devem ficar armazenados numa variável e serem exibidos na operação de extrato.

3;EXTRATO: deve listar todos os depósitos e saques realizados na conta e no fim da listagem deve ser exibido
o saldo final da conta.
Exemplo de valores: R$ xxx.xx

variáveis globais:
-limite_valor_saque
-LIMITE_SAQUES
-números_saques
-saldo
-extrato_conta: lista

funções:
-menu
-saque
-depósito
-extrato
"""
from filecmp import cmpfiles


class Usuario:
    def __init__(self, nome,data_nascimento,cpf,endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f'{self.nome} (CPF: {self.cpf})'



class Conta:

    def __init__(self,numero_conta,ususario):
        self.numero_conta = numero_conta
        self.usuario = ususario
        self.saldo = 0.0
        self.agencia = 1

    def __str__(self):
        return f'Conta: {self.numero_conta} \nTitular: {self.usuario} \nSaldo: {self.saldo}'

usuarios = []
contas= []

def cadastrar_cliente():
    nome = input('Nome : ')
    data_nascimento = input('Data de nascimento: ')
    cpf = input('CPF: ')
    endereco = input("Informe o seu endereço: ")

    for u in usuarios:
        if u.cpf == cpf:
            print('Usuário já cadastrado com este CPF!')
            return
    novo_usuario = Usuario(nome,data_nascimento,cpf,endereco)
    usuarios.append(novo_usuario)
    print(f'Usuário {nome} cadastrado!')


def criar_conta():
    cpf = input('Informe o cpf do titular: ')
    usuario = next((u for u in usuarios if u.cpf == cpf), None)
    if not usuario:
        print(f'Usuário não encontrado.')
        return

    numero_conta = len(contas)+1
    nova_conta = Conta(numero_conta, usuario)
    contas.append(nova_conta)
    print(f'onta criada para {nova_conta.usuario.nome}, CPF: {nova_conta.usuario.cpf} - Número conta: {nova_conta.numero_conta} - Agência: {nova_conta.agencia} - Saldo: {nova_conta.saldo}')

def listar_conta():
    print('-----Contas Cadastradas-----')
    for conta in contas:
        print(conta)

saldo=0
limite_valor_saque=500
LIMITE_SAQUES=3
numeros_saques=0
extrato_conta=[]

def sair():
    print('---Encerrando Programa...---')
    exit()

def extrato():
    print('\n--- EXTRATO ---')
    if not extrato_conta:
        print('Nenhuma movimentação registrada.')
    else:
        for item in extrato_conta:
            print(item)
    print(f'Saldo atual: R$ {saldo:.2f}\n')

def saque():
    global  saldo,numeros_saques
    valor= float(input('Digite o valor que deseja sacar: '))
    if valor <= 0:
        print('Valor inválido para saque.')
    elif valor > saldo:
        print('Saldo insuficiente.')
    elif numeros_saques >= LIMITE_SAQUES:
        print('Limite de saques diário ultrapassado.')
    elif valor > limite_valor_saque:
        print(f'Valor excede o limite por saque (R$ {limite_valor_saque:.2f}).')
    else:
        saldo-=valor
        numeros_saques+=1
        extrato_conta.append(f'Saque: R$ {valor:.2f}')
        print(f'Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}')


def deposito():
    global saldo
    valor= float(input('Digite o valor que deseja depositar: '))
    if valor > 0:
        saldo+=valor
        extrato_conta.append(f'Depósito: R$ {valor:.2f}')
        print(f'Depósito realizado com sucesso!')
    else:
        print('Valor inválido para depósito.')


def entrar_conta():
    cpf = input('Informe o cpf do titular: ')
    usuario = next((u for u in usuarios if u.cpf == cpf), None)
    if not usuario:
        print('Usuário não encontrado.')
        return

    encontrar_conta = int(input('Informe o número da conta: '))
    conta_cadastrada = next((c for c in contas if c.numero_conta == encontrar_conta), None)
    if not conta_cadastrada:
        print('Conta não encontrada.')
        return
    menu_conta()

caixa = {
        "1": cadastrar_cliente,
        "2": criar_conta,
        "3": entrar_conta,
        "4": listar_conta,
        "5": sair
}

def menu_principal():
    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar usuário")
        print("2. Criar Conta")
        print("3. Entrar em uma conta")
        print("4. listar contas")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        funcao = caixa.get(escolha)
        if funcao:
            funcao()
        else:
            print("Opção inválida.")


opcoes_menu={
    "1": deposito,
    "2": saque,
    "3": extrato,
    "4": menu_principal
}

def menu_conta():
    while True:
        print("\n=== MENU ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Voltar")
        escolha = input("Escolha uma opção: ")

        funcao = opcoes_menu.get(escolha)
        if funcao:
            funcao()
        else:
            print("Opção inválida.")


menu_principal()



















