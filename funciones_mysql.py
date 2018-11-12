import mysql.connector
from mysql.connector import Error

def retornar_precio(producto):
    precio = -1
    
    db = {
        'user' : 'root',
        'password' : 'facilito',
        'database' : 'lista_precios',
        'host' : '127.0.0.1'
    }  

    conexion = mysql.connector.connect(** db)
    sql_select_query = "SELECT * FROM lista"
    cursor =  conexion.cursor()
    cursor.execute(sql_select_query)
    lista = cursor.fetchall()

    for row in lista:
        if row[0] == producto:
            precio = row [1]

    conexion.close()
    return precio

