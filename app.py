import os
import mysql.connector
from datetime import datetime

# Configurações do banco
db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

def create_table():
    """Cria tabela se não existir"""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            preco DECIMAL(10,2),
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_product(nome, preco):
    """Insere um novo produto"""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco))
    conn.commit()
    conn.close()

def list_products():
    """Lista todos os produtos"""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

if __name__ == "__main__":
    create_table()
    
    
    # Operações de exemplo
    insert_product("Notebook", 4500.90)
    insert_product("Mouse", 89.90)
    
    print("\nProdutos cadastrados:")
    for produto in list_products():
        print(f"{produto['id']} - {produto['nome']} (R${produto['preco']})")

def interactive_menu():
    """Menu interativo para testes"""
    while True:
        print("\n1. Listar produtos")
        print("2. Adicionar produto")
        print("3. Sair")
        opcao = input("Opção: ")
        
        if opcao == "1":
            produtos = list_products()
            for p in produtos:
                print(f"{p['id']} - {p['nome']} (R${p['preco']})")
        
        elif opcao == "2":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            insert_product(nome, preco)
            print("Produto adicionado!")
        
        elif opcao == "3":
            break

# Mude o __main__ para:
if __name__ == "__main__":
    create_table()
    interactive_menu()