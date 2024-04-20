deposito = 0.0
saldo = 0.0
limite = 500.00
SAQUE_DIARIO = 3
saques_realizados = [] 
depositos_realizados = [] 

# Depositar
def realizarDeposito():
    global saldo
    valor = float(input("Digite o valor a ser depositado: "))
    if valor < 100:
        print("Perdão, mas somente aceitamos depósitos acima de R$100,00")
        voltar_ao_menu()
    else:
        saldo += valor
        depositos_realizados.append(valor)  # Adicione o depósito à lista de depósitos realizados
        print(f"Depósito no valor de R${valor}, realizado com sucesso!")
        voltar_ao_menu()

# Sacar
def realizarSaque():
    global saldo
    global SAQUE_DIARIO
    if SAQUE_DIARIO <= 0:
        print("Limite de saques diários atingido.")
        voltar_ao_menu()
    saque = float(input("Digite o valor a ser sacado: "))
    if saque > saldo:
        print("Saldo insuficiente.")
        voltar_ao_menu()
    saldo -= saque
    saques_realizados.append(saque) 
    SAQUE_DIARIO -= 1
    print(f"Saldo restante: R${saldo}")
    voltar_ao_menu()

# Extrato
def extrato():
    global saldo
    global saques_realizados
    global depositos_realizados
    print("Extrato:")
    print("Saques realizados:")
    for saque in saques_realizados:
        print(f"R${saque}")
    print("Depósitos realizados:")
    for deposito in depositos_realizados:
        print(f"R${deposito}")
    print(f"Saldo atual: R${saldo}")

def voltar_ao_menu():
    opcao = input("Deseja voltar ao menu principal (s/n)? ").lower()
    if opcao == "s":
        menu()
    else:
        print("Obrigado por utilizar o sistema \"Banco da Coréia\"!")
        exit()

def menu():
    print("""
            Bem-vindo(a) ao sistema \"Banco da Coréia\"!

            Escolha uma opção:

            1 - Depositar
            2 - Sacar
            3 - Extrato
            4 - Sair
        """)
    opcao = int(input("R: "))
    if opcao == 1:
        realizarDeposito()
    elif opcao == 2:
        realizarSaque()
    elif opcao == 3:
        extrato()
    elif opcao == 4:
        print("Obrigado por utilizar o sistema \"Banco da Coréia\"!")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menu()

menu()
