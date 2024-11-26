import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sistemaclientes"
    )

def execute_transaction(idcliente, valor):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        print("Iniciando transação...")
        cursor.execute("START TRANSACTION;")
        cursor.execute("UPDATE cliente SET saldo = saldo + %s WHERE idcliente = %s;", (valor, idcliente))
        conn.commit()
        cursor.execute("SELECT * FROM cliente WHERE idcliente = %s;", (idcliente,))
        cliente = cursor.fetchone()
        print(f"Cliente atualizado: {cliente}")
    except Exception as e:
        conn.rollback()
        print(f"Erro na transação: {e}")
    finally:
        cursor.close()
        conn.close()

print("Usuário 01:")
execute_transaction(1, 1000)  # Adicionar saldo ao cliente 1

print("Usuário 02:")
execute_transaction(1, -500)  # Reduzir saldo do cliente 1
