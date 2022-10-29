from sqlalchemy import create_engine
import psycopg2
import sqlalchemy

def baseDeDatos (df, tabla):
    try:
        conex = create_engine("postgresql+psycopg2://{}:{}@{}/{}".format("postgres","admin","127.0.0.1","cultura"))
        conexpostgres = conex.connect()
        metadatas = sqlalchemy.MetaData()
        df.to_sql(tabla, conexpostgres, if_exists="append", index=False)
        return "Tabla subida"
    except Exception as ex:
        return ex

def comparar_tablas (df, tabla):
    conex = create_engine("postgresql+psycopg2://{}:{}@{}/{}".format("postgres","admin","127.0.0.1","cultura"))
    conexpostgres = conex.connect()
    consulta2 = conexpostgres.execute("select * from pg_tables where tablename='{}'".format(tabla))

    if consulta2.cursor.rowcount == 0:
        return True

    if consulta2.cursor.rowcount > 0:
        consulta = conexpostgres.execute("select * from {};".format(tabla))
        if df.shape[0] > consulta.cursor.rowcount:
            return True
        else:
            False


def ejecutarSQL ():
    conex = create_engine("postgresql+psycopg2://{}:{}@{}/{}".format("postgres","admin","127.0.0.1","cultura"))
    conexpostgres = conex.connect()
    with open("./scripts.sql", 'r') as ca:
        data = ca.read()
        conexpostgres.execute(data)