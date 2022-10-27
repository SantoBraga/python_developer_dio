# Integrando Python com SQLite e MongoDB e Criando uma API com Flask no Ambiente COLAB 

## Integrando Python com SQLite e MongoDB: 

- Implementando um Banco de Dados Relacional com SQLAlchemy: 

  - Implementar uma aplicação de integração com SQLite com base em um esquema relacional disponibilizado. Sendo assim, utilize o esquema dentro do contexto de cliente e conta para criar as classes de sua API. Essas classes irão representar as tabelas do banco de dados relacional dentro da aplicação. 
  
   ![Esquema Relacional](https://github.com/bccalegari/python_developer_dio/blob/main/Integra%C3%A7%C3%A3o%20com%20Python%20e%20Frameworks/sqlite_schema.png)
   
  - Entregáveis: 
    - Aplicação com a definição do esquema por meio das classes usando SQLAlchemy 
    - Inserção de um conjunto de dados mínimo para manipulação das informações 
    - Execução de métodos de recuperação de dados via SQLAlchemy 


- Implementando um Banco de Dados NoSQL com Pymongo: 

  - Você irá implementar um banco NoSQL com mongodb para fornecer uma visão agregada do modelo relacional. Sendo assim, as informações de cliente e contas existentes estão contidas dentro de documentos de acordo com cliente.

  - Execute as operações:

    - Conecte ao mongo atlas e crie um banco de dados
    - Defina uma coleção bank para criar os documetos de clientes
    - Insira documentos com a estrutura mencionada
    - Escreve instruções de recuperação de informações com base nos pares de chave e valor como feito em aula


## Arquivos: 

- O script está com o nome de *'sistema_bancario_v2.py'* 

## Ferramentas Utilizadas: 

- Python 3.10.4
- MongoDB Atlas 6.0
