import sqlite3
import pandas as pd
from pathlib import Path

db_path = Path("database/biblioteca.db")
output_dir = Path(__file__).parent

conn = sqlite3.connect(db_path)

query_autores_piquenique = """
SELECT a.nome, a.pais
FROM Autor a
JOIN LivroAutor la ON la.id_autor = a.id
JOIN Livro l ON l.id = la.id_livro
WHERE l.titulo = 'Piquenique na Estrada';
"""
df_autores_piquenique = pd.read_sql_query(query_autores_piquenique, conn)
df_autores_piquenique.to_json(output_dir / "autores_piquenique.json", orient="records", indent=4)

query_livros_philip = """
SELECT l.titulo, l.isbn, l.genero, l.data_publicacao
FROM Livro l
JOIN LivroAutor la ON la.id_livro = l.id
JOIN Autor a ON a.id = la.id_autor
WHERE a.nome = 'Philip K. Dick';
"""
df_livros_philip = pd.read_sql_query(query_livros_philip, conn)
df_livros_philip.to_json(output_dir / "livros_philip_k_dick.json", orient="records", indent=4)

query_emprestimos_pedro = """
SELECT l.titulo, e.data_emprestimo
FROM Emprestimo e
JOIN Usuario u ON u.id = e.id_usuario
JOIN Livro l ON l.id = e.id_livro
WHERE u.nome = 'Pedro' AND u.sobrenome = 'Vinicius' AND e.data_devolucao IS NULL;
"""
df_emprestimos_pedro = pd.read_sql_query(query_emprestimos_pedro, conn)
df_emprestimos_pedro.to_json(output_dir / "emprestimos_pedro_vinicius.json", orient="records", indent=4)

conn.close()

print("✅ Arquivos JSON exportados no mesmo diretório do script.")
