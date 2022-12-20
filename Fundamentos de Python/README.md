# Criando um Sistema Bancário com Python

- Objetivo Geral: Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

## Escopo:
 
- Depósito:  
  - Deve ser possível depositar valores positivos para a minha conta bancária.
  - Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
  
- Saque:  
  - O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
  - Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
  - Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
  
- Extrato:  
  - Essa operação deve listar todos os depósitos e saques realizados na conta.
  - No fim da listagem deve ser exibido o saldo atual da conta.
  - Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
  - Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45  

## Arquivos:

- O script está com o nome de *'sistema_bancario_v1.py'*

## Ferramentas Utilizadas:

- Python 3.10.4
