import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

""" CLASE USUARIO """
class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        """ SE LLENAN LOS DATOS """
        fecha = datetime.datetime.now()
        
        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))


        sql = "INSERT INTO usuarios VALUES(NULL, %s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        
        """ ESTE FRAGMENTO ES SUCEPTIBLE A ERRORES ENTONCES DE DEBEN CONTROLAR """
        try:
            """ SE EJECUTA LA CONSULTA SE PASA LA CONSULTA Y LOS PARAMETRO O DATOS """
            cursor.execute(sql, usuario)

            """ PERMITE EJECUCION REL Y QUE SE GUARDE """
            database.commit()

            """ RETORNA UNA RESPUESTA """
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
            return result
        

        """ RETORNA EL OBJETO CON SELF Y LAS COLUMNAS MODIFICADAS """
        return [cursor.rowcount, self]

    def idenificar(self):
        #Consulta a ver si existes y conicide en usuario y contrase;a
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())
        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
        