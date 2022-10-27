# Otimizando o Sistema Bancário com Funções em Python

- Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

## Escopo:

- Depósito:  
  - Positional only.
  
- Saque:  
  - Keyword only.
  
- Extrato:  
  - Positional and Keyword only.

- Criar Usuário:  
  - O programa deve armazenar os usuários em uma lista.
  - Um usuário é composto por: data de nascimento, cpf e endereço.
  - O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado.
  - Deve ser armazenado somente os números do CPF.
  - Não podemos cadastrar dois usuários com o mesmo CPF.

- Criar Conta Corrente:  
  - O programa deve armazenar as contas em uma lista.
  - Uma conta é composta por: agência, número da conta e usuário.
  - O número da conta é sequencial, iniciando em 1.
  - O número da agência é fixo "0001".
  - O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.

## Arquivos:

- O script está com o nome de *'sistema_bancario_v2.py'*

## Ferramentas Utilizadas:

- Python 3.10.4
