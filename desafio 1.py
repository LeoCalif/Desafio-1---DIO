import textwrap

def menu():
    menu = """\n
    ======================= MENU ====================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print ("\n=== Deposito realizado===")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print ("\n Operação falhou!!! Voce nao tem saldo suficiente.")

    elif excedeu_limite:
        print ("\nOperação falhou!!! O valor do saque excede o limite")

    elif excedeu_saques:
        print ("\nOperação falhou!!! Número maximo de sques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print ("\nSaque realizado com sucesso!!! ")

    else:
        print (f"\nOperação falhou! Valor informado é invalido!")

        return saldo, extrato
def exibir_extrato(saldo, / ,* , extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
def criar_usuario(usuarios):
    cpf = input("Informe o cpf (Somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("Já existe usuario com esse CPF!!! ")
        return

    nome = input ("informe nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print ("Usuario cadastrado com sucesso!!")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("\nConta criada com sucesso! ")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}

    print ("\nUsuario nao encontrado, fluxo de criação de conta encerrado!!")
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """

        print ("=" * 100)
        print (textwrap.dedent(linha))
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

        if opcao == "d":  #DEPOSITAR
            valor = float(input("Informe o valor do depósito:  "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print ("Operação inválida, por favor selecione novamente a operação desejada.")

main()