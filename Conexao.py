import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='admin',
    database='recomendacao'
)
cursor = conexao.cursor()

com_sql = "INSERT INTO USUARIO(IDUSUARIO, NOME_USUARIO, EMAIL, SENHA_USUARIO, NOTA) VALUES (%s, %s, %s, %s, %s)"
valor = ('18', 'DIANA', 'DIANA@EMAIL.COM', '*****', '2,4')
cursor.execute(com_sql, valor)

conexao.commit()
print(cursor.rowcount, "Inserido com sucesso")
