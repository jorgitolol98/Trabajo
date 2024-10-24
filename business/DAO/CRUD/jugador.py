from DAO.conexion import Conexion

host = 'localhost'
user = 'admin'
password = 'admin'
db = 'poos_juego'

def agregar(c):#acá C es un objeto
    try:
        #Paso 1: Crear un objeto de tipo Conexion
        con=Conexion(host,user,password,db)
        #Paso 2: Crear la Query
        sql="Insert Into jugador set nombre='{}', nivel='{}',"\
        "salud='{}', experiencia={}, id_arma={}".format(c.nombre,c.nivel,c.experiencia,c.id_arma)
        #Paso 3: Damos la orden de ejecución de la Query
        con.ejecuta_query(sql)
        #Paso 4: Actualizamos
        con.commit()
        #Paso 5: Opcional- Enviamos mensaje para saber si insertop con éxito
        input("\n\nDatos Ingresados con Éxito :) \n Presiona Enter para Continuar")
        #Paso 6: Lo más importante.... Desconectarseeeeeeeeeeeeeeeeee
        con.desconectar()
    except Exception as e:
        con.rollback()
        print("La Excepción fue en la Inserción:{}".format(e))

def modificar(c):# Acá c es una lista
    try:
        #Paso 1: 
        con=Conexion(host,user,password,db)
        #Paso 2:
        sql="Update jugador set id_jugador='{}', nombre='{}', nivel={}, experiencia='{}', id_arma{}".format(c[1],c[2],c[3],c[4],c[0],)
        #Paso 3:
        con.ejecuta_query(sql)
        #Paso 4:
        con.commit()
        #Paso 5: Opcional
        input("\n\n Edición realizada con Éxito :)\n\nPresiones Enter para continuar")
        #Paso 6: 
        con.desconectar()
    except Exception as e:
        con.rollback()
        print("Error en la Edición: {}".format(e))

def eliminar(id_juagdor):
    try:
        con=Conexion(host,user,password,db)
        sql="Delete from Cliente where id_cliente={}".format(id_juagdor)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Eliminación realizada con Éxito :)\n\nPresiones Enter para continuar")
        con.desconectar()
    except Exception as e:
        con.rollback()
        print("Error en la Eliminación: {}".format(e))

def mostrarTodos():
    try:
        #Paso 1: Crear un objeto de tipo conexion
        con=Conexion(host,user,password,db)
        #Paso 2: Crear la Query
        sql="Select * From jugador"
        #Paso 3: Solicitar la ejecución y almacenaremos el resultado
        cursor=con.ejecuta_query(sql)
        #Paso 4: Bajar los datos del limbo a una lista
        datos=cursor.fetchall()
        #Paso 5: Desconectarse
        con.desconectar()
        #Paso 6: Retorno de quien nos pida los datos
        return datos
    except Exception as e:
        print("Error en la Consulta General: {}".format(e))

def consultaParcial(cantidad):
    try:
        con=Conexion(host,user,password,db)
        sql="Select * From jugador"
        #Solicitar la ejecución y almacenaremos el resultado
        cursor=con.ejecuta_query(sql)
        #Bajar los datos del limbo a una lista
        datos=cursor.fetchone(size=cantidad)
        con.desconectar()
        #Retorno de quien nos pida los datos
        return datos
    except Exception as e:
        print("Error en la Consulta General: {}".format(e))

def mostrarAlgunos(id_jugador):
    try:
        con=Conexion(host,user,password,db)
        sql="Select * From jugador whre id_jugador={}".format(id_jugador)
        #Solicitar la ejecución y almacenaremos el resultado
        cursor=con.ejecuta_query(sql)
        #Bajar los datos del limbo a una lista
        datos=cursor.fetchmany()
        con.desconectar()
        #Retorno de quien nos pida los datos
        return datos
    except Exception as e:
        print("Error en la Consulta General: {}".format(e))
