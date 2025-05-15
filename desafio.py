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


opcoes_menu={
    "1": deposito,
    "2": saque,
    "3": extrato,
    "4": sair
}

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        funcao = opcoes_menu.get(escolha)
        if funcao:
            funcao()
        else:
            print("Opção inválida.")

menu()




















