# BankApp

BankApp é um sistema bancário simples, construído com Flask, onde os usuários podem criar contas, fazer login, depositar, transferir e visualizar extratos. Ele simula transações bancárias, proporcionando uma experiência básica de gerenciamento financeiro com funcionalidades como registro de contas, autenticação de usuários e manipulação de saldo e extrato.

## Funcionalidades

- **Criação de conta**: Permite ao usuário criar uma conta com CPF, e-mail, nome, sobrenome, data de nascimento e senha.
- **Login**: Autenticação do usuário via e-mail e senha.
- **Depósito**: Realização de depósitos para incrementar o saldo da conta.
- **Transferência**: Envio de dinheiro de um usuário para outro.
- **Extrato**: Exibe o extrato de transações realizadas pelo usuário.
- **Logout**: Desconecta o usuário do sistema.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **Flask-Login**: Gerenciamento de sessões de usuário.
- **Flask-Bcrypt**: Criptografia de senhas.
- **PostgreSQL**: Banco de dados utilizado para persistência de dados.

## Requisitos

- Python 3.7+
- Dependências:
  - Flask
  - Flask-Login
  - Flask-SQLAlchemy
  - Flask-Bcrypt
  - WTForms
  - psycopg2

## Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/Samuel-Gaudencio/bankapp.git
cd bankapp
```

### 2. Crie um ambiente virtual e ative-o:

```bash
python3 -m venv venv
source venv/bin/activate  # Para sistemas UNIX (Linux/Mac)
venv\Scripts\activate     # Para Windows
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados:
- O app utiliza um banco de dados PostgreSQL. 
- Certifique-se de ter uma instância do PostgreSQL rodando.

### 5. Execute o aplicativo:

```bash
flask run
```

## Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
