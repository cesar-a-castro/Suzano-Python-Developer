#Desafio Sistema Bancário#

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []
saques = []

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito\n")
        valor = float(input("Digite o valor a ser depositado: "))
        print(f"O valor depositado foi: R$ {valor:.2f}")
        saldo += valor
        depositos.append(valor)

        if valor < 0 :
            print("Valor incorreto, tente novamente")
       
        

    elif opcao == "2":
        print("Saque\n")
        sacar = float(input("Digite o valor a ser sacado:"))
        
        if (sacar <= saldo) and (numero_saques <= LIMITE_SAQUES ) and (sacar <= limite):
            print(f"O valor sacado foi: R$ {sacar:.2f}")
            saldo -= sacar
            saques.append(sacar)
            numero_saques += 1

        if sacar > saldo :
            print("Saldo insuficiente")
        
        if sacar > limite:
            print("Valor acima do limite (Limite : R$: 500,00)")
        
        if numero_saques > LIMITE_SAQUES:
            print("Você ultrapassou seu limite de saques") 
        
           
    elif opcao == "3":
        print("Extrato\n")
        print(f"Saldo atual: R$ {saldo:.2f}")
        formatado = [f"R$ {valor:,.2f}"for valor in depositos]
        print(f"Depósitos: {','.join(formatado)}")
        formatado2 = [f"R$ {valor:,.2f}"for valor in saques]
        print(f"Saques: {','.join(formatado2)}")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
