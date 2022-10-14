# Sistema Bancário v3

import sys
from abc import ABC, abstractmethod
from datetime import datetime
from time import sleep


class Client:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.c_account = None
        self.s_account = None

    def perform_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        if account.__name__ == 'CheckingAccount':
            if self.c_account:
                return False
            self.c_account = account
            return True
        if account.__name__ == 'SavingsAccount':
            if self.s_account:
                return False
            self.s_account = account
            return True


class NaturalPerson(Client):
    def __init__(self, cpf, name, birth_date, address, login, password):
        super().__init__(login, password)
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date
        self.address = address


class LegalPerson(Client):
    def __init__(self, cnpj, name, birth_date, address, login, password):
        super().__init__(login, password)
        self.cnpj = cnpj
        self.name = name
        self.birth_date = birth_date
        self.address = address


class Account:
    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._record = Records()

    @classmethod
    def new_account(cls, number, client):
        return cls(number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def record(self):
        return self._record

    def withdraw(self, value):
        balance = self.balance

        if value > balance:
            print("\n### Você não possui saldo suficiente para essa operação. ###")

        elif value > 0:
            self._balance -= value
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n### Operação falhou! O valor informado é inválido. ###")

        return False

    def deposit(self, value):
        if value > 0:
            self._balance += value
            print("\n=== Depósito realizado com sucesso! ===")
            return True

        print("\n### Operação falhou! O valor informado é inválido. ###")
        return False


class CheckingAccount(Account):
    def __init__(self, number, client, limit=1000, withdraw_limit=6, deposit_limit=1500):
        super().__init__(number, client)
        self.limit = limit
        self.withdraw_limit = withdraw_limit
        self.deposit_limit = deposit_limit

    def __str__(self):
        return f'Tipo de Conta: Conta Corrente\n Agência: {self.agency}\n C/C: {self.number}\n Titular: {self.client.name}'

    @property
    def account_name(self):
        return self.__class__.__name__

    def withdraw(self, value):
        withdraw_number = len(
            [transaction for transaction in self.record.transactions if transaction["type"]
             == Withdraw.__name__])

        if value > self.limit:
            print("\n### Operação falhou! O valor do saque excede o limite. ###")

        elif withdraw_number >= self.limit:
            print("\n### Operação falhou! Número máximo de saques excedido. ###")

        else:
            return super().withdraw(value)

        return False

    def deposit(self, value):
        if value > self.deposit_limit:
            print("\n### Operação falhou! O valor do depósito excede o limite. ###")
            return False

        return super().deposit(value)


class SavingsAccount(Account):
    def __init__(self, number, client, limit=500, withdraw_limit=3, deposit_limit=1000):
        super().__init__(number, client)
        self.limit = limit
        self.withdraw_limit = withdraw_limit
        self.deposit_limit = deposit_limit

    def __str__(self):
        return f'Tipo de Conta: Conta Poupança\n Agência: {self.agency}\n C/C: {self.number}\n Titular: {self.client.name}'

    @property
    def account_name(self):
        return self.__class__.__name__

    def withdraw(self, value):
        withdraw_number = len(
            [transaction for transaction in self.record.transactions if transaction["type"]
             == Withdraw.__name__])

        if value > self.limit:
            print("\n### Operação falhou! O valor do saque excede o limite. ###")

        elif withdraw_number >= self.limit:
            print("\n### Operação falhou! Número máximo de saques excedido. ###")

        else:
            return super().withdraw(value)

        return False

    def deposit(self, value):
        if value > self.deposit_limit:
            print("\n### Operação falhou! O valor do depósito excede o limite. ###")
            return False

        return super().deposit(value)


class Records:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        if transaction.__class__.__name__ == 'Deposit':
            self._transactions.append(
                {
                    "type": 'Depósito',
                    "value": transaction.value,
                    "data": datetime.now().strftime('%d/%M/%Y, %H:%M:%S'),
                }
            )
        if transaction.__class__.__name__ == 'Withdraw':
            self._transactions.append(
                {
                    "type": 'Saque',
                    "value": transaction.value,
                    "data": datetime.now().strftime('%d/%M/%Y, %H:%M:%S'),
                }
            )


class Transaction(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    @classmethod
    @abstractmethod
    def register(self, account):
        pass


class Withdraw(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        transaction = account.withdraw(self.value)

        if transaction:
            account.record.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        transaction = account.deposit(self.value)

        if transaction:
            account.record.add_transaction(self)


class BankSystem:
    def __init__(self):
        self._clients = []
        self._accounts_number = 0

    @property
    def clients(self):
        return self._clients

    @property
    def accounts_number(self):
        return self._accounts_number

    def deposit(self, client, account):
        value = float(input("Informe o valor do depósito: "))
        transaction = Deposit(value)
        client.perform_transaction(account, transaction)

    def withdraw(self, client, account):
        value = float(input("Informe o valor do saque: "))
        transaction = Withdraw(value)
        client.perform_transaction(account, transaction)

    def statement(self, account):
        statement = ""
        transactions = account.record.transactions
        if not transactions:
            statement = "### Não foram realizadas movimentações. ###\n"
            print(statement)
        else:
            print("\n================ EXTRATO ================")
            for transaction in transactions:
                statement += f"\n{transaction['type']}:\n\t{transaction['data']}\n\tR$ {transaction['value']:.2f}"
            print(statement)
            print(f"\nSaldo Atual: R${account.balance:.2f}")
            print("==========================================\n")

    def balance(self, account):
        transactions = account.record.transactions
        if not transactions:
            print("### Não foram realizadas movimentações. ###\n")
        else:
            print("\n================ Saldo Atual ================")
            print(f"\nR${account.balance:.2f}\n")
            print("==========================================")

    def new_c_account(self, client):
        self._accounts_number += 1
        account = CheckingAccount.new_account(self._accounts_number, client)
        client.c_account = account

        print("\n=== Conta Corrente criada com sucesso! ===")

    def new_s_account(self, client):
        self._accounts_number += 1
        account = SavingsAccount.new_account(self._accounts_number, client)
        client.s_account = account

        print("\n=== Conta Poupança criada com sucesso! ===")

    def new_n_client(self):
        cpf = self.__client_cpf()
        client = self.__validate(cpf, 0)

        if client:
            print("\n### O CPF inserido já está cadastrado em nosso sistema. ###")
            return

        name = self.__client_name()
        birth_date = self.__client_birth_date()
        address = self.__client_address()
        login = self.__client_login()
        password = self.__client_password()

        client = NaturalPerson(cpf, name, birth_date, address, login, password)

        self._clients.append(client)

        print("\n=== Cliente criado com sucesso! ===\n")
        return client

    def new_l_client(self):
        cnpj = self.__client_cnpj()
        client = self.__validate(cnpj, 1)

        if client:
            print("\n### O CNPJ inserido já está cadastrado em nosso sistema. ###")
            return

        name = self.__client_name()
        birth_date = self.__client_birth_date()
        address = self.__client_address()
        login = self.__client_login()
        password = self.__client_password()

        client = LegalPerson(cnpj, name, birth_date, address, login, password)

        self._clients.append(client)

        print("\n=== Cliente criado com sucesso! ===\n")
        return client

    def __validate(self, value, sort):
        if sort == 0:
            p_validated = [client for client in self._clients if client.__class__.__name__ == 'NaturalPerson']
            validated = [client for client in p_validated if client.cpf == value]
            return validated[0] if validated else None
        if sort == 1:
            p_validated = [client for client in self._clients if client.__class__.__name__ == 'LegalPerson']
            validated = [client for client in p_validated if client.cnpj == value]
            return validated[0] if validated else None
        return False

    def __client_name(self):
        nome = input(str("Insira o seu nome completo: "))
        while nome.isnumeric() is True or nome.isspace() is True or nome == "":
            print("Por favor insira um nome válido!")
            nome = str(input("Insira o seu nome completo: "))
        return nome.strip().title()

    def __client_birth_date(self):
        data = input("Insira sua data de nascimento: ")
        while ValueError:
            try:
                data = datetime.strptime(data, '%d/%M/%Y')
                if (datetime.today().year - data.year) < 18:
                    raise ValueError
                data = datetime.strftime(data, '%d/%M/%Y')
                return data
            except ValueError:
                print("Por favor insira uma data válida!")
                data = input(": ")

    def __client_cpf(self):
        while ValueError:
            try:
                cpf = int(input("Insira o seu CPF sem pontos ou traços: "))
                aux = str(cpf)
                if len(list(aux)) != 11:
                    raise ValueError
                return str(cpf)
            except ValueError:
                print("Por favor insira um CPF válido, com 11 dígitos numéricos e sem pontos ou traços")

    def __client_cnpj(self):
        while ValueError:
            try:
                cnpj = int(input("Insira o seu CNPJ sem pontos ou traços: "))
                aux = str(cnpj)
                if len(list(aux)) != 11:
                    raise ValueError
                return str(cnpj)
            except ValueError:
                print("Por favor insira um CNPJ válido, com 14 dígitos numéricos e sem pontos ou traços")
                continue

    def __client_address(self):
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

    def __client_login(self):
        login = input(str("Insira o login desejado: "))
        while login.isalnum() is False or login.isspace() is True or login == "" or login.isnumeric() is True:
            print("Por favor insira um login válido!")
            login = input(str(": "))
        return login.strip()

    def __client_password(self):
        print("Insira uma senha para a sua conta, com no mínimo 8 caracteres, contendo letras e números.")
        senha = input(str("Senha: "))
        while senha.isalnum() is False or senha.isspace() is True or senha == "" or senha.isnumeric() is True \
                or senha.isalpha() is True or len(senha) < 8:
            print("Por favor insira uma senha válida!")
            senha = input(str(": "))
        return senha


class BankInterface:
    def __init__(self):
        self._bank_system = BankSystem()
        print("\nBem vindo!\n")
        sleep(2)
        print(" Sistema Bancário ".center(30, '#'))
        print()

    @property
    def bank_system(self):
        return self._bank_system

    def welcome_menu(self, bank_system):
        o = None
        o_ver = ['1', '2', '3']
        sleep(2)
        print(" Menu ".center(30, '='))
        while o != 3:
            print(" [1] Fazer Login\n [2] Criar Novo Usuário\n [3] Encerrar Programa")
            o = input('Opção: ')
            while o not in o_ver:
                print("Por favor insira uma opção válida!")
                o = input('Opção: ')
            match int(o):
                case 1:
                    if len(bank_system.clients) == 0:
                        print("### Ainda não existe nenhum usuário cadastrado no sistema ###\n")
                    else:
                        temp_log = input("Insira seu login: ")
                        for i in bank_system.clients:
                            if i.login == temp_log:
                                temp_pass = input("Insira sua senha: ")
                                if temp_pass == i.password:
                                    print("=== Login efetuado com sucesso ===\n")
                                    client = i
                                    self.__client_menu(client, bank_system)
                                else:
                                    print("### Login ou senha incorretos! ###\n")
                case 2:
                    o2_ver = ['0', '1']
                    print("Você é uma pessoa física ou jurídica?\n [0] Pessoa Física\n [1] Pessoa Jurídica")
                    o2 = input('Opção: ')
                    while o2 not in o2_ver:
                        print("Por favor insira uma opção válida!")
                        o2 = input('Opção: ')
                    match int(o2):
                        case 0:
                            bank_system.new_n_client()
                        case 1:
                            bank_system.new_l_client()
                case 3:
                    print("Encerrando...")
                    sleep(1)
                    break
        print("Volte Sempre!")

    def __client_menu(self, client, bank_system):
        o = None
        o_ver = ['1', '2', '3', '4', '5', '6']
        sleep(2)
        print(f"{client.login} ".center(30, '#'), '\n')
        while o != 6:
            print(" Opções ".center(20, '='))
            print(" [1] Entrar em Conta Corrente\n [2] Criar Conta Corrente\n "
                  "[3] Entrar em Conta Poupança\n [4] Criar Conta Poupança\n "
                  "[5] Deslogar do Usuário Atual\n [6] Encerrar Programa")
            o = input('Opção: ')
            while o not in o_ver:
                print("Por favor insira uma opção válida!")
                o = input('Opção: ')
            match int(o):
                case 1:
                    pass
                    if client.c_account is None:
                        print("### Você ainda não possui uma conta corrente! ###\n")
                    else:
                        self.__account_menu(client, bank_system, 0)
                case 2:
                    if client.c_account is None:
                        print("Gerando uma nova conta corrente...\n")
                        bank_system.new_c_account(client)
                    else:
                        print("### Você já possui uma conta corrente! ###\n")
                case 3:
                    if client.s_account is None:
                        print("### Você ainda não possui uma conta poupança! ###\n")
                    else:
                        self.__account_menu(client, bank_system, 1)
                case 4:
                    if client.s_account is None:
                        print("Gerando uma nova conta poupança...\n")
                        bank_system.new_s_account(client)
                    else:
                        print("### Você já possui uma conta poupança! ###\n")
                case 5:
                    return
                case 6:
                    print("Encerrando...")
                    sleep(1)
                    print("Volte Sempre!")
                    sys.exit()

    def __account_menu(self, client, bank_system, sort):
        o = None
        o_ver = ['1', '2', '3', '4', '5', '6']
        sleep(2)
        while o != 6:
            if sort == 1:
                print('\n', client.s_account, '\n')
                print(" Opções ".center(20, '='))
                print(" [0] Ver Rendimento\n [1] Depósito\n [2] Saque\n "
                      "[3] Extrato\n [4] Saldo\n "
                      "[5] Sair da Conta\n [6] Encerrar Programa")
                o_ver = ['0', '1', '2', '3', '4', '5', '6']
            else:
                print('\n', client.c_account, '\n')
                print(" Opções ".center(20, '='))
                print(" [1] Depósito\n [2] Saque\n "
                      "[3] Extrato\n [4] Saldo\n "
                      "[5] Sair da Conta\n [6] Encerrar Programa")
            o = input('Opção: ')
            while o not in o_ver:
                print("Por favor insira uma opção válida!")
                o = input('Opção: ')
            match int(o):
                case 0:
                    if client.s_account.balance == 0:
                        print('O rendimento atual da poupança é de 1,40% ao ano.')
                    else:
                        print(f"O rendimento atual da poupança é de 1,40% ao ano.\n No dia "
                              f"{datetime.now().day} de {datetime.now().month} de {datetime.now().year+1} "
                              f"você terá R${(client.s_account.balance*1.014):.2f}")
                case 1:
                    if sort == 0:
                        bank_system.deposit(client, client.c_account)
                    else:
                        bank_system.deposit(client, client.s_account)
                case 2:
                    if sort == 0:
                        bank_system.withdraw(client, client.c_account)
                    else:
                        bank_system.withdraw(client, client.s_account)
                case 3:
                    if sort == 0:
                        bank_system.statement(client.c_account)
                    else:
                        bank_system.statement(client.s_account)
                case 4:
                    if sort == 0:
                        bank_system.balance(client.c_account)
                    else:
                        bank_system.balance(client.s_account)
                case 5:
                    return
                case 6:
                    print("Encerrando...")
                    sleep(1)
                    print("Volte Sempre!")
                    sys.exit()


def main():
    interface = BankInterface()
    interface.welcome_menu(interface.bank_system)

main()
