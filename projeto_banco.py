def menu():

    menu = """\n
    =============== MENU ===============
    [1]: Depositar
    [2]: Sacar
    [3]: Extrato
    [4]: Nova Conta
    [5]: Listar Contas
    [6]: Novo usuario
    [0]: Sair
    =====================================
"""
    print(menu)
    return input("Informe a opçao desejada: ")



def depositar(saldo,valor,extrato,/):
    if valor >0:
            saldo+=valor
            extrato += f"Deposito:R$ {valor:.2f}\n"
            print(" O valor foi depositado!")
    else:
            print("valor invalido, tente novamente!")   

    return saldo, extrato



def sacar(*,saldo,valor,extrato,limite,numero_saques,limites_saques):
    exceder_limite = valor > limite
    exceder_saldo = valor > saldo
    exceder_saques = numero_saques >= limites_saques
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
            print("O saque foi realizado!")
        
    else:
            print("Houve falha na operação, o valor que foi informado é invalido!")
    return saldo, extrato,numero_saques


def exibir_extrato(saldo,/,*,extrato):
        print("<========== EXTRATO ==========>")
        print(f"Não foram feitas operações"if not extrato.strip() else extrato)
        print(f"\nSaldo:R${saldo:.2f}")
        print("<============================>")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente número): ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
          print("Já existe um usuaruio com este CPF!")
          return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouro,num-bairro-cidade/estado): ")

    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})

    print("Usuário criado!")


def filtrar_usuario(cpf,usuarios):
      usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]== cpf]
      return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia,usuarios,numero_conta):
      cpf = input("Informe o CPF do usuário: ")
      usuario = filtrar_usuario(cpf,usuarios)
      if usuario:
            print("Conta criada!")
            return{"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
      print("Usuário nao encontrado,criação de conta encerrada!")




def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:{conta["agencia"]}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """

        print("=" * 100)
        print(linha)

      


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "1":
            valor = float(input("digite o valor que será depositado: "))
            saldo,extrato = depositar(saldo,valor,extrato)
        
        elif opcao == "2":
            valor = float(input("digite o valor que será sacado: "))
            saldo,extrato,numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limites_saques = LIMITE_SAQUES,
                )
            
        elif opcao == "3":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,usuarios,numero_conta)

            if conta:
                contas.append(conta)
              
        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break
        
        else:
            print("Essa operação é invalida ou não existe, por favor tente novamente.")     
              

main()
        