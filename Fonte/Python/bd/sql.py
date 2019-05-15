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

def sql_insert(campos, tabela, dados):
    query = "INSERT INTO %s(%s) VALUES(%s);" %(campos, tabela, dados)
    banco(query)

def sql_select(campos, tabela, condicao):
    query = "SELECT %s FROM %s WHERE %s;" %(campos, tabela, condicao)
    banco(query)

def sql_select_all(campos, tabela):
    query = "SELECT %s FROM %s;" %(campos, tabela)
    banco(query)

def sql_update(campos, tabela, condicao):
    query = "UPDATE %s SET %s WHERE %s;" %(campos, tabela, condicao)
    banco(query)

def sql_delete_where_in(tabela, campo, valoresIn):
    query = query = "DELETE FROM %s WHERE %s in (%s);" %(tabela,campo,valoresIn)
    banco(query)