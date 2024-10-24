from DAO.conexion import Conexion

host = 'localhost'
user = 'admin'
password = 'admin'
db = 'poos_juego'

def agregar(c):
    try:
        #Paso 1: Crear un objeto de tipo Conexion
        con=Conexion(host,user,password,db)
        #Paso 2: Crear la Query
        sql="Insert Into arma set tipo_arma='{}', danio='{}',"\
        "minucion={}".format(c.tipo_arma,c.danio,c.municion)
        #Paso 3: Damos la orden de ejecución de la Query
        con.ejecuta_query(sql)
        #Paso 4: Actualizamos
        con.commit()
        #Paso 5: Lo más importante.... Desconectarseeeeeeeeeeeeeeeeee
        con.desconectar()
    except Exception as e:
        con.rollback()
        print("La Excepción fue en la Inserción:{}".format(e))

def modificar(c):
    try:
         #Paso 1: 
        con=Conexion(host,user,password,db)
        #Paso 2:
        sql="Update arma set tipo_arma='{}', municion={}, danio={}, whre id_arma={}".format(c[1],c[2],c[3],c[0])
        #Paso 3:
        con.ejecuta_query(sql)
        #Paso 4:
        con.commit()
        #Paso 5: 
        con.desconectar()
    except Exception as e:
        con.rollback()
        print("Error en la Edición: {}".format(e))

def eliminar(id_arma):
    try:
        con=Conexion(host,user,password,db)
        sql="Delete from arma where id_arma={}".format(id_arma)
        con.ejecuta_query(sql)
        con.commit()
        con.desconectar()
    except Exception as e:
        con.rollback()
        print("Error en la Eliminación: {}".format(e))

def mostrarTodos():
    try:
        #Paso 1: 
        con=Conexion(host,user,password,db)
        #Paso 2: 
        sql="Select * From arma"
        #Paso 3: 
        cursor=con.ejecuta_query(sql)
        #Paso 4: 
        datos=cursor.fetchall()
        #Paso 5: 
        con.desconectar()
        #Paso 6: 
        return datos
    except Exception as e:
        print("Error en la Consulta General: {}".format(e))

def mostrarParcial(cantidad):
    try:
        con=Conexion(host,user,password,db)
        sql="Select * From arma"
        #Solicitar la ejecución y almacenaremos el resultado
        cursor=con.ejecuta_query(sql)
        #Bajar los datos del limbo a una lista
        datos=cursor.fetchmany(size=cantidad)
        con.desconectar()
        #Retorno de quien nos pida los datos
        return datos
    except Exception as e:
        print("Error en la Consulta General: {}".format(e)) 

def mostrarUno(id_arma):
    try:
        con=Conexion(host,user,password,db)
        sql="Select * From usuario where id_usuario='{}'".format(id_arma)
        #Solicitar la ejecución y almacenaremos el resultado
        cursor=con.ejecuta_query(sql)
        #Bajar los datos del limbo a una lista
        datos=cursor.fetchmany()
        con.desconectar()
        #Retorno de quien nos pida los datos
        return datos
    except Exception as e:
        print("Error en la Consulta General: {}".format(e))
          