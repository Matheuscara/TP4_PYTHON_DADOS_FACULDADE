from pathlib import Path
import sqlite3
from seed import seedar_banco

db_path = Path("database/biblioteca.db")
db_path.parent.mkdir(exist_ok=True)

if db_path.exists():
    db_path.unlink()
    print("🗑️ Banco de dados existente deletado.")

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Autor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        pais TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Livro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        isbn TEXT NOT NULL UNIQUE,
        genero TEXT,
        data_publicacao DATE,
        paginas INTEGER,
        exemplares INTEGER
    );

    CREATE TABLE IF NOT EXISTS LivroAutor (
        id_livro INTEGER,
        id_autor INTEGER,
        FOREIGN KEY (id_livro) REFERENCES Livro(id),
        FOREIGN KEY (id_autor) REFERENCES Autor(id),
        PRIMARY KEY (id_livro, id_autor)
    );

    CREATE TABLE IF NOT EXISTS Usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        data_nascimento DATE
    );

    CREATE TABLE IF NOT EXISTS Emprestimo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        id_livro INTEGER,
        data_emprestimo DATE NOT NULL,
        data_devolucao DATE,
        FOREIGN KEY (id_usuario) REFERENCES Usuario(id),
        FOREIGN KEY (id_livro) REFERENCES Livro(id)
    );
    """)
    print("✅ Banco de dados criado com sucesso!")

seedar_banco()
