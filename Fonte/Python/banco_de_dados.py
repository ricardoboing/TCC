import pymysql

DATABASE_HOST = "localhost"
DATABASE_USER = "boing"
DATABASE_PASSWORD = "boing12345"
DATABASE_NAME = "tcc"

# Le o conteudo recebido em uma conexao socket
def ler_conteudo_conexao(conexao, numeroBytes):
    return str(conexao.recv(numeroBytes).decode('utf-8'))

def banco(query):
    print(query)

    # Conecta ao banco de dados
    conexao = pymysql.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        db=DATABASE_NAME
    )

    try:
        # Insere query ao banco de dados
        with conexao.cursor() as cursor:
            cursor.execute(query)
            retorno = cursor.fetchall()
        conexao.commit()

    finally:
        # Cancela operacao
        conexao.rollback()
    
    conexao.close()

    return retorno