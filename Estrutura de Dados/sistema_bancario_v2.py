# Sistema Bancário v2

import sys
from time import sleep
from datetime import datetime

lista_usuarios = []
lista_contas = []
agencia = 0.001
numero_conta = 1
LIMITE_SAQUES = 3
LIMITE = 500


def sistema_bancario():  # Função de inicialização do sistema
    flag = False
    o = None
    o_ver = '123'
    print("\nBem vindo!\n")
    sleep(2)
    print(" Sistema Bancário ".center(30, '#'))
    print()
    while o != 3:
        print(" [1] Fazer Login\n [2] Criar Novo Usuário\n [3] Encerrar Programa")
        o = input('Opção: ')
        while o not in o_ver:
            print("Por favor insira uma opção válida!")
            o = input('Opção: ')
        match int(o):
            case 1:
                if len(lista_usuarios) == 0:
                    print("Ainda não existe nenhum usuário cadastrado no sistema\n")
                else:
                    temp_log = input("Insira seu login: ")
                    for j in lista_usuarios:
                        for i in j:
                            if temp_log == i:
                                temp_pass = input("Insira sua senha: ")
                                for k in lista_usuarios:
                                    for p in k:
                                        if temp_pass == p:
                                            print("Login efetuado com sucesso\n")
                                            __sistema_bancario_conta_corrente(temp_log)
                                print("Senha incorreta!\n")
                                flag = True
                    if flag is False:
                        print("O login inserido não existe!\n")
            case 2:
                __criar_usuario()
                print()
            case 3:
                print("Encerrando...")
                sleep(1)
                break
    print("Volte Sempre!")


def __sistema_bancario_conta_corrente(temp_log):
    usuario_login = temp_log
    o = None
    o_ver = '1234'
    flag = False
    sleep(2)
    print()
    print(f" {usuario_login} ".center(30, '#'))
    print()
    while o != 4:
        print(" Opções ".center(20, '='))
        print(
            " [1] Entrar em Conta Corrente\n [2] Criar Conta Corrente\n [3] Listar Todas as Contas\n [4] Encerrar Programa")
        o = input('Opção: ')
        while o not in o_ver:
            print("Por favor insira uma opção válida!")
            o = input('Opção: ')
        match int(o):
            case 1:
                if len(lista_contas) == 0:
                    print("Você não possui nenhuma conta corrente cadastrada ainda!\n")
                else:
                    temp_agen = input("Insira sua agência: ")
                    for j in lista_contas:
                        for i in j:
                            if temp_agen == i:
                                temp_nconta = input("Insira o número da conta: ")
                                for k in lista_contas:
                                    for p in k:
                                        if temp_nconta == p:
                                            print("Login efetuado com sucesso")
                                            __sistema_bancario_menu_opcoes(temp_agen, temp_nconta)
                    print("A conta informada não existe")
            case 2:
                print("Gerando uma nova conta corrente...\n")
                sleep(2)
                __criar_conta_corrente(usuario_login, agencia, numero_conta)
            case 3:
                if len(lista_contas) == 0:
                    print("Você não possui nenhuma conta corrente cadastrada ainda!\n")
                else:
                    for i in lista_contas:
                        for j in i:
                            if usuario_login == j:
                                print(i[0:2])
            case 4:
                print("Encerrando...")
                sleep(1)
                break
    print("Volte Sempre!")
    sys.exit()


def __sistema_bancario_menu_opcoes(agencia, numero_conta):
    agencia_user = agencia
    n_conta_usuario = numero_conta
    o = None
    o_ver = '12345'
    sleep(2)
    print()
    print(f" {agencia_user} / {n_conta_usuario} ".center(30, '#'))
    print()
    while o != 5:
        print(" Opções ".center(20, '='))
        print(" [1] Depósito\n [2] Saque\n [3] Extrato\n [4] Saldo Atual\n [5] Encerrar Programa")
        o = input('Opção: ')
        while o not in o_ver:
            print("Por favor insira uma opção válida!")
            o = input('Opção: ')
        match int(o):
            case 1:
                __deposito(n_conta_usuario)
            case 2:
                __saque(n_conta=n_conta_usuario)
            case 3:
                __extrato(n_conta_usuario)
            case 4:
                __saldo(n_conta_usuario)
            case 5:
                print("Encerrando...")
                sleep(1)
                break
    print("Volte Sempre!")
    sys.exit()


def __deposito(n_conta, /):
    no_conta = str(n_conta)
    c = 0
    flag = False
    dep = 0
    print("Insira o valor desejado para depósito:")
    while flag is False:
        try:
            dep = float(input('Depósito: '))
            if dep <= 0:
                print("Por favor insira um valor válido!")
            if type(dep) == float and dep > 0:
                flag = True
        except ValueError:
            print("Por favor insira um valor válido!")
    for i in lista_contas:
        for j in i:
            if no_conta == j:
                lista_contas[c][3] += dep
                data = datetime.today().strftime('%d/%M/%Y, %H:%M:%S')
                aux = lista_contas[c][3]
                extrato_temp = [f"[{data}", "Depósito", f"R${aux:.2f}']"]
                lista_contas[c][4] += extrato_temp
        c += 1
    print("Depósito realizado com sucesso!\n")


def __saque(*, n_conta):
    no_conta = str(n_conta)
    saq = None
    c = 0
    for i in lista_contas:
        for j in i:
            if no_conta == j:
                if lista_contas[c][5] < LIMITE_SAQUES:
                    flag = False
                    aux = lista_contas[c][3]
                    print(f"\nSaldo Atual: R${aux:.2f}")
                    print("Insira o valor desejado para o saque: ")
                    while flag is False:
                        try:
                            saq = float(input('Saque: '))
                            if saq <= 0:
                                print("Por favor insira um valor válido!")
                            if saq > 500:
                                print("O limite por saque é de R$500,00")
                            if type(saq) == float and 0 < saq < 501:
                                flag = True
                        except ValueError:
                            print("Por favor insira um valor válido!")
                    if saq > aux:
                        print("Você não possui saldo suficiente para essa operação!\n")
                    else:
                        lista_contas[c][3] -= saq
                        lista_contas[c][5] += 1
                        data = datetime.today().strftime('%d/%M/%Y, %H:%M:%S')
                        extrato_temp = [f"[{data}", "Saque", f"R${saq:.2f}']"]
                        lista_contas[c][4] += extrato_temp
                        print("Saque realizado com sucesso!\n")
                else:
                    print("Você já atingiu seu limite de saque diário!")
        c += 1


def __saldo(n_conta, /):
    no_conta = str(n_conta)
    c = 0
    for i in lista_contas:
        for j in i:
            if no_conta == j:
                print(" SALDO ATUAL ".center(20, '='))
                aux = lista_contas[c][3]
                print(f"R${aux:.2f}\n")
                return
        c += 1


def __extrato(n_conta, /):
    no_conta = str(n_conta)
    c = 0
    c2 = 0
    print(" EXTRATO ".center(15, '='))
    print("\nGerando extrato...")
    sleep(2)
    for i in lista_contas:
        for j in i:
            if no_conta == j:
                if not lista_contas[c2][4]:
                    print("Não foram realizadas movimentações.\n")
                    return
        c2 += 1
    for i in lista_contas:
        for j in i:
            if no_conta == j:
                print(lista_contas[c][4])
                aux = lista_contas[c][3]
                print(f"\n Saldo Atual: R${aux:.2f}\n")
                return
        c += 1


def __login_usuario(login):
    login = input(str("Insira o login desejado: "))
    while login.isalnum() is False or login.isspace() is True or login == "" or login.isnumeric() is True:
        print("Por favor insira um login válido!")
        login = input(str(": "))
    return login.strip()


def __senha_usuario(senha):
    print("Insira uma senha para a sua conta, com no mínimo 8 caracteres, contendo letras e números.")
    senha = input(str("Senha: "))
    while senha.isalnum() is False or senha.isspace() is True or senha == "" or senha.isnumeric() is True \
            or senha.isalpha() is True or len(senha) < 8:
        print("Por favor insira uma senha válida!")
        senha = input(str(": "))
    return senha


def __nome_usuario(nome):
    nome = input(str("Insira o seu nome completo: "))
    while nome.isnumeric() is True or nome.isspace() is True or nome == "":
        print("Por favor insira um nome válido!")
        nome = str(input("Insira o seu nome completo: "))
    return nome.strip().title()


def __data_nascimento_usuario(data):
    data = input("Insira sua data de nascimento: ")
    while ValueError:
        try:
            data = datetime.strptime(data, '%d/%M/%Y')
            data = datetime.strftime(data, '%d/%M/%Y')
            return data
        except ValueError:
            print("Por favor insira uma data válida!")
            data = input(": ")


def __cpf_usuario(cpf):
    while ValueError:
        try:
            cpf = int(input("Insira o seu CPF sem pontos ou traços: "))
            aux = str(cpf)
            if len(list(aux)) != 11:
                raise ValueError
            return str(cpf)
        except ValueError:
            print("Por favor insira um CPF válido, com 11 dígitos numéricos e sem pontos ou traços")
            continue


def __endereco_usuario(endereco):
    print("Insira o seu endereço:")
    endereco1 = input("Logradouro: ").strip()
    while endereco1 == "":
        print("Por favor preencha o campo solicitado!")
        endereco1 = input("Logradouro: ").strip()
    endereco2 = input("Número: ").strip()
    while endereco2 == "":
        print("Por favor preencha o campo solicitado!")
        endereco2 = input("Número: ").strip()
    endereco3 = input("Bairro: ").strip()
    while endereco3 == "":
        print("Por favor preencha o campo solicitado!")
        endereco3 = input("Bairro: ").strip()
    endereco4 = input("Cidade: ").strip()
    while endereco4 == "":
        print("Por favor preencha o campo solicitado!")
        endereco4 = input("Cidade: ").strip()
    endereco5 = input("Sigla do Estado: ").strip()
    while endereco5 == "":
        print("Por favor preencha o campo solicitado!")
        endereco5 = input("Sigla do Estado: ").strip()
    endereco = endereco1 + ", " + endereco2 + " - " + endereco3 + " - " + endereco4 + "/" + endereco5
    return endereco


def __criar_usuario(login=None):
    nome = d_nascimento = cpf = endereco = senha = None
    login = __login_usuario(login)
    senha = __senha_usuario(senha)
    nome = __nome_usuario(nome)
    d_nascimento = __data_nascimento_usuario(d_nascimento)
    cpf = __cpf_usuario(cpf)
    for j in lista_usuarios:
        for i in j:
            while i == cpf:
                print("O CPF inserido já está cadastrado em nosso sistema, por favor insira outro!")
                cpf = __cpf_usuario(cpf)
    endereco = __endereco_usuario(endereco)
    aux = [login, senha, nome, d_nascimento, cpf, endereco]
    return lista_usuarios.append(aux)


def __criar_conta_corrente(login, agencia, numero_conta):
    saldo = 0
    EXTRATO = []
    saque_atual = 0
    if len(lista_contas) == 0:
        numero_conta = str(numero_conta)
        agencia = str(agencia)
        agencia = agencia.replace(".", "")
        aux = [agencia, numero_conta, login, saldo, EXTRATO, saque_atual]
        print(f"Conta criada com sucesso:\nAgência:{agencia}\nNúmero da Conta:{numero_conta}\n")
        return lista_contas.append(aux)
    else:
        numero_conta += 1
        numero_conta = str(numero_conta)
        agencia = str(agencia)
        agencia = agencia.replace(".", "")
        aux = [agencia, numero_conta, login, saldo, EXTRATO, saque_atual]
        print(f"Conta criada com sucesso:\nAgência:{agencia}\nNúmero da Conta:{numero_conta}\n")
        return lista_contas.append(aux)


# Rodar sistema bancário

if __name__ == '__main__':
    sistema_bancario()
