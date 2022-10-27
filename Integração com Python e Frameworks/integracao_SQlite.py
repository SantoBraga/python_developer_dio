# Importações

from time import sleep
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

# Criando classe base para usar a propriedade de herança

Base = declarative_base()


class Client(Base):
    """Classe/Tabela Cliente: Atributos: [id, name, cpf, address]"""

    __tablename__ = "client"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cpf = Column(String(9), nullable=False, unique=True)
    address = Column(String(75), nullable=False)

    # Definindo relacionamento com a tabela de contas

    account = relationship("Account", back_populates="client", cascade="all, delete-orphan")

    # Representação da classe/tabela

    def __repr__(self):
        return f"Client(id={self.id}, name={self.name}, cpf={self.cpf}, address={self.address})"


class Account(Base):
    """Classe/Tabela Conta: Atributos: [id, account_type, agency, account_number, client_id]"""

    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    account_type = Column(String, nullable=False)
    agency = Column(Integer, default="OOO1")
    account_number = Column(Integer, unique=True, nullable=False)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False) #Chave estrangeira para a tabela de usuários

    # Definindo relacionamento com a tabela de usuários

    client = relationship("Client", back_populates="account")

    # Representação da classe/tabela

    def __repr__(self):
        return f"Account(id={self.id}, account_type={self.account_type}, agency={self.agency}, account_number={self.account_number}, client_id={self.client_id})"


# Fazendo conexão com o banco de dados:

engine = create_engine("sqlite://")

# Instanciação das classes como tabelas no banco de dados:

Base.metadata.create_all(engine)


class SQL:
    """Classe para comandos SQL"""

    def __init__(self, engine):
        self.engine = engine
        self.session = Session(self.engine) # Iniciando sessão
        self.account_number = self.account_number_count() # Chamando o método para definir o ínicio da contagem de contas

    # Inserção de registros na tabelas

    def insert(self, name, cpf, address, account_type):
        self.account_number += 1
        register = Client(name=name, cpf=cpf, address=address,
                          account=[Account(account_type=account_type, account_number=self.account_number)])
        with self.session:
            self.session.add(register)
            self.session.commit()

    # Inserção de registros na tabelas possibilitando o usuário ter dois tipos de contas

    def insert_2(self, name, cpf, address, account_type1, account_type2):
        self.account_number += 1
        register = Client(name=name, cpf=cpf, address=address,
                          account=[Account(account_type=account_type1, account_number=self.account_number),
                                   Account(account_type=account_type2, account_number=self.account_number+1)])
        with self.session:
            self.session.add(register)
            self.session.commit()

    # Método para retornar o número de contas existentes no banco

    def account_number_count(self):
        statement = select(func.count('*')).select_from(Account)
        for query in self.session.scalars(statement):
            return query

    # Método para retornar um determinado cliente por cpf

    def select_client(self, cpf):
        statement = select(Client).where(Client.cpf.in_([cpf]))
        for query in self.session.scalars(statement):
            return query

    # Método para retornar uma determinada conta pelo cpf de um cliente

    def select_client_account(self, cpf):
        pre_statement = select(Client.id).where(Client.cpf.in_([cpf]))
        for pre_query in self.session.scalars(pre_statement):
            pre_query = pre_query
        end_statement = select(Account).where(Account.client_id.in_([pre_query]))
        for end_query in self.session.scalars(end_statement):
            return end_query

    # Método para retornar todos os registros do banco

    def select_all(self):
        connection = self.engine.connect()
        results = connection.execute(select(Client, Account).join_from(Account, Client)).fetchall()
        for query in results:
            return query

    # Método para retornar todos os clientes do banco ordenados alfabeticamente do maior para o menor

    def select_all_clients_descname(self):
        statement = select(Client).order_by(Client.name.desc())
        for query in self.session.scalars(statement):
            return query


# Função do Menu

def menu(SQL):
    inspector_engine = inspect(engine)
    print("\nBem vindo!\n")
    sleep(2)
    print(" Sistema de Banco de Dados ".center(31, '#'))
    print()
    op = None
    op_ver = ['1', '2', '3', '4', '5']
    sleep(2)
    print(" Menu ".center(30, '='))
    while op != 5:
        print(" [1] Mostrar Tabelas \n [2] Inserir Cliente\n [3] Procurar Cliente \n [4] Mostrar Registros \n [5] Encerrar Programa")
        op = input('Opção: ')
        while op not in op_ver:
            print("Por favor insira uma opção válida!")
            op = input('Opção: ')
        match int(op):
            case 1:
                print()
                print(inspector_engine.get_table_names())
            case 2:
                print()
                try:
                    name = input("Insira o seu nome: ")
                    while name.isnumeric() is True or name.isspace() is True or name == "":
                        print("Por favor insira um nome válido!")
                        name = str(input("Insira o seu nome completo: "))
                    name = name.strip().title()
                    cpf = input("Insira o seu cpf: ").replace(",", "").replace(".", "").replace("-", "").strip()
                    aux = str(cpf)
                    while aux == "" or len(list(aux)) != 9:
                        print("Por favor insira um cpf válido!")
                        cpf = input("Insira o seu cpf: ").replace(",", "").replace(".", "").replace("-", "").strip()
                        aux = str(cpf)
                    address = input("Insira o seu endereço: ").strip()
                    while address == "":
                        print("Por favor insira um endereço válido!")
                        address = input("Insira o seu endereço: ").strip()
                    print("Qual tipo de conta você deseja:\n[0] Conta Corrente\n[1] Conta Poupança\n[2] Conta Corrente e Poupança ")
                    o = input(": ")
                    o_ver = ['0', '1', '2']
                    while o not in o_ver:
                        print("Por favor insira uma opção válida!")
                        o = input(": ")
                    match int(o):
                        case 0:
                            account_type = "Conta Corrente"
                            SQL.insert(name, cpf, address, account_type)
                        case 1:
                            account_type = "Conta Poupança"
                            SQL.insert(name, cpf, address, account_type)
                        case 2:
                            account_type1 = "Conta Corrente"
                            account_type2 = "Conta Poupança"
                            SQL.insert_2(name, cpf, address, account_type1, account_type2)
                    print("Cliente inserido com sucesso!\n")
                except:
                    print("\nErro na inserção, por favor insira informações válidas, não aceitamos valores nulos e nem o mesmo CPF para dois cadastros\n")
            case 3:
                print()
                if SQL.account_number == 0:
                    print("None")
                else:
                    cpf = input("Insira o cpf do cliente: ")
                    if SQL.select_client(cpf) is None:
                        print("O CPF procurado não existe\n")
                    else:
                        print("\nCliente:")
                        print(SQL.select_client(cpf))
                        print("\nConta:")
                        print(SQL.select_client_account(cpf))
                        print()
            case 4:
                print()
                print(SQL.select_all())
                print()
            case 5:
                print("Encerrando...")
                sleep(1)
                break
    print("Volte Sempre!")


# Rodando o código

if __name__ == '__main__':
    SQL = SQL(engine)
    menu(SQL)
