from business.DAO.conexion import Conexion

host = 'localhost'
user = 'admin'
password = 'admin'
db = 'poos_juego'


class CRUDUsuario:

    def agregar(usuario):
        try:
            #Pas 1: crear un objeto de tipo Conexión
            con=Conexion(host,user,password,db)
            #Pasp 2: Crear la Query
            sql="Insert Into Jugador set id_usuario='{}', password '{}'".format(usuario.id_usuario,usuario.password)
            #Paso 3: Damos la orden de ejecución de la Query
            con.ejecuta_query(sql)
            #Paso 4: Actualizamos
            con.commit()
            #Paso 6: Lo más importante.... Desconectarseeeeeeeeeeeeeeeeee
            con.desconectar()
            print("Usuario agregado con éxito!!:")
        except Exception as e:
            con.rollback()
        print("La Excepción fue en la Inserción:{}".format(e))


    def modificar(usuario, idUsuarioMod): #aca c es una lista
        try:
            #Pas 1: 
            con=Conexion(host, user, password, db)
            #Pasp 2: 
            sql="Update usuario set id_usuario='{}', password '{}' where id_usuario='{}'".format(usuario[0],usuario[1],idUsuarioMod)
            #Paso 3: 
            con.ejecuta_query(sql)
            #Paso 4: 
            con.commit()
            #Paso 6: 
            con.desconectar()
        except Exception as e:
            con.rollback()
        print("La Excepción fue en la Inserción:{}".format(e))

    def eliminar(id_usuario):
        try:
            con=Conexion(host, user, password, db)
            sql="Delete from duenio where id_duenio='{}'".format(id_usuario)
            con.ejecuta_query(sql)
            con.commit()
            con.desconectar()
        except Exception as e:
            con.rollback()
            print("Error en la Eliminación: {}".format(e))

    def mostrarTodos():
        try:
            #Paso 1: Crear un objeto de tipo conexion
            con=Conexion(host,user,password,db)
            input("paso1")
            #Paso 2: Crear la Query
            sql="Select * From usuario"
            #Paso 3: Solicitar la ejecución y almacenaremos el resultado
            cursor=con.ejecuta_query(sql)
            #Paso 4: Bajar los datos del limbo a una lista
            datos=cursor.fetchall()
            #Paso 5: Descinectarse
            con.desconectar()
            #Paso 6: Retorno de quien nos pida los datos
            return datos
        except Exception as e:
            print("Error en la Consulta General: {}".format(e))

    def consultaParcial(cantidad):
        try:
            con=Conexion(host,user,password,db)
            sql="Select * From usuario"
            #Solicitar la ejecución y almacenaremos el resultado
            cursor=con.ejecuta_query(sql)
            #Bajar los datos del limbo a una lista
            datos=cursor.fetchone(size=cantidad)
            con.desconectar()
            #Retorno de quien nos pida los datos
            return datos
        except Exception as e:
            print("Error en la Consulta General: {}".format(e))

    @classmethod
    def mostrarUno(cls, id_usuario):
        try:
            con=Conexion(host,user,password,db)
            sql="Select * From usuario where id_usuario='{}'".format(id_usuario)
            #Solicitar la ejecución y almacenaremos el resultado
            cursor=con.ejecuta_query(sql)
            #Bajar los datos del limbo a una lista
            datos=cursor.fetchmany()
            con.desconectar()
            #Retorno de quien nos pida los datos
            return datos
        except Exception as e:
            print("Error en la Consulta General: {}".format(e))

    @classmethod
    def validarUsuario(cls, id_usuario,password):
        datos=cls.mostrarUno(id_usuario)
        print(datos)

        if datos:
            password = datos [1]
        if password == password:
            return True
        
        return False

    @classmethod
    def validarUsuarioExiste(cls, id_usuario):
        datos=cls.mostrarUno(id_usuario)
        if datos:
            return True
        
        return False
          