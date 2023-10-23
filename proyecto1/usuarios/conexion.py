import mysql.connector

def conectar():
    """ CONECCCION CON LA BASE DE DATOS """
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="master_python",
        port=3306
    )

    """ HACER VARIAS CONSULTAS USANDO EL MISMO CURSOR """
    cursor = database.cursor(buffered=True)

    return[database, cursor]