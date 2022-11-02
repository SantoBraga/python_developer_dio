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


## Criando uma API com Flask no Ambiente COLAB: 

- Integrando um arquivo JSON para um servidor FASTAPI: 

  - Para este projeto o desafio final envolve a entrega de uma API desenvolvida no framework Flask utilizando a Plataforma COLAB. O Objetivo principal está relacionado com a leitura de uma planilha de dados no formato JSON utilizando uma API no ambiente de desenvolvimento colaborativo COLAB.

    - Nosso servidor FastAPI deve trazer a planilha gerada em JSON, assim, como estamos apresentando um “Hello Word” neste exemplo. Para isso, deve ser dado um {Public_URL}/index no navegador para chegar ao nosso endpoint, pois criamos apenas uma rota, ou seja , /index .


## Arquivos: 

- [Integração com SQlite](https://github.com/bccalegari/python_developer_dio/blob/main/Integra%C3%A7%C3%A3o%20com%20Python%20e%20Frameworks/integracao_SQlite.py)

- [Integração com Pymongo](https://github.com/bccalegari/python_developer_dio/blob/main/Integra%C3%A7%C3%A3o%20com%20Python%20e%20Frameworks/integracao_pymongo.py)

- [Integração com FASTAPI](https://github.com/bccalegari/python_developer_dio/blob/main/Integra%C3%A7%C3%A3o%20com%20Python%20e%20Frameworks/fastapi.ipynb)

## Ferramentas Utilizadas: 

- Python 3.10.4
  - Frameworks:
    - SQLite 
    - Pymongo
    - FASTAPI
- MongoDB Atlas 6.0
