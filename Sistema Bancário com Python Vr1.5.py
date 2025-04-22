#Desafio Sistema Bancário#

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Cliente
[5] Criar Conta
[6] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []
saques = []
usuarios = []
contas = []
AGENCIA = "0001"
numero_contas = 0

def deposito(valor,saldo,depositos,/):
    if valor > 0:
        print(f"O valor depositado foi: R$ {valor:.2f}")
        saldo += valor
        depositos.append(valor)
    else :
        print("Valor incorreto, tente novamente")
    return saldo, depositos

def saque(*, sacar, saldo, saques, numero_saques, limite, limite_saques):
    excedeu_saldo = sacar > saldo
    excedou_limite = sacar > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Operação falhou, você não tem saldo.")
    
    elif excedou_limite:
        print("Operação falhou, o valor excede o limite de saque.")

    elif excedeu_saques:
        print("Operação falhou, número máximo de saques excedido.")

    elif valor > 0:

        saldo -= sacar
        print(f"O valor sacado foi: R$ {sacar:.2f}")
        saques.append(sacar)
        numero_saques += 1

    else:
        print("Operação falhou, valor inválido.")
    return saldo, saques

def extrato(saldo, /, *, depositos):
    print(f"Saldo atual: R$ {saldo:.2f}")
    formatado = [f"R$ {valor:,.2f}"for valor in depositos]
    print(f"Depósitos: {','.join(formatado)}")
    formatado2 = [f"R$ {valor:,.2f}"for valor in saques]
    print(f"Saques: {','.join(formatado2)}")

def criar_usuario(usuarios):    
    cpf = input("Insira seu CPF (somente números):")
    filtrar_usuario(cpf,usuarios)
    if filtrar_usuario(cpf, usuarios):
        return
    
    nome = input("Insira seu nome:")
    data_nascimento = input("Insira sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso")

def filtrar_usuario(cpf,usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Usuário já existe")
            return True
    return False
                    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
        
    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    
    print("Usuário não encontrado")
    

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito\n")
        valor = float(input("Digite o valor a ser depositado: "))

        saldo, depositos = deposito(valor, saldo, depositos)

    elif opcao == "2":
        print("Saque\n")
        sacar = float(input("Digite o valor a ser sacado:"))
        
        saldo, saques = saque(
             saldo=saldo,
             saques=saques,
             sacar=sacar,
             limite=limite,
             numero_saques=numero_saques,
             limite_saques=LIMITE_SAQUES,
        )
               
    elif opcao == "3":
        print("Extrato\n")
        extrato(saldo, depositos=depositos)

    elif opcao == "4":
        print("Cadastrar cliente:")
        criar_usuario(usuarios)
   
    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

         
    elif opcao == "6":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
