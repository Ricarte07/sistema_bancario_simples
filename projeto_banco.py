menu = """
    [1]: Depositar
    [2]: Sacar
    [3]: Extrato
    [0]: Sair

"""

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("digite o valor que será depositado: "))

        if valor >0:
            saldo+=valor
            extrato += f"Deposito:R$ {valor:.2f}\n"
        else:
            print("valor invalido, tente novamente!")    


    elif opcao == "2":
        valor = float(input("digite o valor que será sacado: "))
        exceder_limite = valor > limite
        exceder_saldo = valor > saldo
        exceder_saques = numero_saques >= LIMITES_SAQUES

        if exceder_saldo:
            print("Saque não aprovado!O valor que esta sendo sacado é maior que seu saldo, tente novamente.")
        
        elif exceder_limite:
            print("Saque não aprovado!O valor que esta sendo sacado é maior do que o limite da conta,tente novamente.")
        
        elif exceder_saques:
            print("Saque não aprovado!Você ultrapassou o limite de saque diarios, tente novamente amanhã.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Houve falha na operação, o valor que foi informado é invalido!")

            

    elif opcao == "3":
        print("<========== EXTRATO ==========>")
        print(f"Não foram feitas operações"if not extrato else extrato)
        print(f"\nSaldo:R${saldo:.2f}")
        print("<============================>")
    elif opcao == "0":
        break

    else:
        print("Essa operação é invalida ou não existe, por favor tente novamente.")        