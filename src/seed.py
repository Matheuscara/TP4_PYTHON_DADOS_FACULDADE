import pandas as pd
import sqlite3
from pathlib import Path

def seedar_banco():
    csv_dir = Path("data")
    db_path = Path("database/biblioteca.db")

    conn = sqlite3.connect(db_path)

    arquivos_tabelas = {
        "autor.csv": "Autor",
        "livro.csv": "Livro",
        "livro_autor.csv": "LivroAutor",
        "usuario.csv": "Usuario",
        "emprestimo.csv": "Emprestimo"
    }

    for arquivo, tabela in arquivos_tabelas.items():
        csv_path = csv_dir / arquivo
        if csv_path.exists():
            df = pd.read_csv(csv_path)
            df.to_sql(tabela, conn, if_exists="append", index=False)
            print(f"Dados da tabela {tabela} inseridos com sucesso!")

    conn.close()
