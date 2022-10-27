# Importações

import pymongo
import datetime
import pprint

# Realizando conexão com o pymongo


client = pymongo.MongoClient("mongodb+srv://pymongo:pymongodio@cluster0.y5m9uok.mongodb.net/?retryWrites=true&w=majority")

# Definindo nome do database

db = client.pymongo

# Bulk Insert - Contas dos Clientes

new_accounts = [{
    "client_name": "Gabriel Oliveira",
    "person": "Natural Person",
    "account_type": "Checking Account",
    "agency": "0001",
    "account_number": 1,
},
    {
        "client_name": "Gabriel Pontes",
        "person": "Legal Person",
        "account_type": "Savings Account",
        "agency": "0001",
        "account_number": 2,
    },
    {
        "client_name": "Beatriz Moraes",
        "person": "Legal Person",
        "account_type": "Checking Account",
        "agency": "0001",
        "account_number": 3,
    },
    {
        "client_name": "Gabriela Medeiros",
        "person": "Natural Person",
        "account_type": "Savings Account",
        "agency": "0001",
        "account_number": 4,
    }
]

accounts = db.accounts
accounts.insert_many(new_accounts)

# Bulk Insert - Inserindo operações realizadas pelos clientes

new_operations = [{
    "client_id": f"{db.accounts.find_one({'account_number': 1})}", # "Foreign Key" para a conta do cliente
    "operation_type": "Deposit",
    "value": 50.00,
    "operation_success": True,
    "date": datetime.datetime.utcnow()
},
    {
        "client_id": f"{db.accounts.find_one({'account_number': 2})}",
        "operation_type": "Withdraw",
        "value": 25.20,
        "operation_success": False,
        "date": datetime.datetime.utcnow()
    },
    {
        "client_id": f"{db.accounts.find_one({'account_number': 1})}",
        "operation_type": "Received Transaction",
        "value": 105.63,
        "operation_success": True,
        "date": datetime.datetime.utcnow()
    },
    {
        "client_id": f"{db.accounts.find_one({'account_number': 2})}",
        "operation_type": "Transaction Made",
        "value": 105.63,
        "operation_success": True,
        "date": datetime.datetime.utcnow()
    }
]

operations = db.operations
operations.insert_many(new_operations)

# Realizando um join entre o documento de conta dos clientes e suas operações realizadas

account_operations = db.operations.aggregate([{'$lookup':
                                     {'from': 'operations',
                                      'localField': '_id',
                                      'foreignField': 'client_id', 'as': 'fromAccounts'}
                                 },
                                {'$replaceRoot':
                                     {'newRoot':
                                          {'$mergeObjects':
                                               [{'$arrayElemAt': ['$fromAccounts', 0]}, '$$ROOT']}}},
                                {'$project': {'fromAccounts': 0}}])

print("\nClientes e suas operações:\n")
for result in account_operations:
    print(f"{result}\n")

#Recuperando todas as contas

print("\nContas:")
for result in accounts.find():
    pprint.pprint(result)
