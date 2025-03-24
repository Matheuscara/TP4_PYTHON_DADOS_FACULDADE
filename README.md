# 📚 Sistema de Gerenciamento de Biblioteca

Este projeto foi desenvolvido como parte da disciplina **Fundamentos de Dados**, com o objetivo de implementar um sistema para gerenciar **empréstimos e devoluções de livros** de uma biblioteca.

## 🔍 Descrição

O sistema permite:
- Cadastro de **livros**, **autores** e **usuários**.
- Registro de **empréstimos** e **devoluções**.
- Consultas como:
  - Autores de um determinado livro.
  - Livros escritos por um autor específico.
  - Empréstimos ativos de um usuário.

Os dados são lidos a partir de arquivos **CSV** e armazenados em um banco de dados **SQLite**, utilizando o pacote **Pandas** para manipulação.

## 🛠️ Tecnologias

- Python 3.11
- Pandas
- SQLite
- Docker + Docker Compose

## 📦 Organização do Projeto

- `src/`
  - `main.py`: Inicializa o banco.
  - `database.py`: Cria o banco de dados e as tabelas.
  - `seed.py`: Popula o banco com dados dos arquivos CSV.
  - `queries.py`: Realiza consultas e exporta arquivos JSON.

- `data/`: Contém os arquivos CSV com os dados.
- `database/`: Armazena o banco `biblioteca.db`.

## 🚀 Como executar

```bash
docker compose up -d --build
```

## 📄 Resultado

Ao final da execução, são gerados três arquivos JSON com os resultados das consultas, no mesmo diretório do script `queries.py`.

## 👨‍🏫 Informações

- **Aluno:** Matheus Dias Cara  
- **Projeto de Bloco:** Fundamentos de Dados  
- **Professor:** LP Maia  
- **Instituição:** INFNET - Rio de Janeiro  
- **Ano:** 2024