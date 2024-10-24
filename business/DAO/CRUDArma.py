from business.DAO.conexion import Conexion
from business.DTO.arma import Arma

host = 'localhost'
user = 'benjaconnector'
password = '123456789'
db = 'poos_juego'

class CRUDArma:

    @classmethod
    def agregar_arma(cls, arma):
        result = True
        try:
            #Paso 1: Crear un objeto de tipo Conexion
            con=Conexion(host,user,password,db)
            #Paso 2: Crear la Query
            sql="Insert Into arma set tipo_arma='{}', danio='{}',"\
            "municion={}".format(arma.tipo_arma,arma.danio,arma.municion)
            #Paso 3: Damos la orden de ejecución de la Query
            con.ejecuta_query(sql)
            #Paso 4: Actualizamos
            con.commit()
            #Paso 5: Lo más importante.... Desconectarseeeeeeeeeeeeeeeeee
            
        except Exception as e:
            result = False
            con.rollback()
            print("Error al insertar: {}".format(e))
        con.desconectar()
        
        return result

    @classmethod
    def modifica_arma(cls, arma, **nuevos_valores):
        result = True

        tipo_arma = nuevos_valores.get('tipo_arma', arma[1])
        danio = nuevos_valores.get('danio', arma[2])
        municion = nuevos_valores.get('municion', arma[3])

        try:
            #Paso 1: 
            con=Conexion(host,user,password,db)
            #Paso 2:
            sql="UPDATE arma SET tipo_arma='{}', municion={}, danio={} WHERE id_arma={}".format(tipo_arma, municion, danio, arma[0])
            #Paso 3:
            con.ejecuta_query(sql)
            #Paso 4:
            con.commit()
            #Paso 5: 
            
        except Exception as e:
            con.rollback()
            result = False
            print("Error en la Edición: {}".format(e))
        con.desconectar()

        return result

    @classmethod
    def eliminar_arma(cls, id_arma):
        result = True
        try:
            con=Conexion(host,user,password,db)
            sql="Delete from arma where id_arma={}".format(id_arma)
            con.ejecuta_query(sql)
            con.commit()

        except Exception as e:
            con.rollback()
            result = False
            print("Error en la Eliminación: {}".format(e))
        con.desconectar()

        return result

    @classmethod
    def mostrar_todos_arma(cls):
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
            return datos
        except Exception as e:
            print("Error en la Consulta General: {}".format(e))
        con.desconectar()

    @classmethod
    def mostrar_parcial_arma(cls, cantidad):
        try:
            con=Conexion(host,user,password,db)
            sql="Select * From arma"
            #Solicitar la ejecución y almacenaremos el resultado
            cursor=con.ejecuta_query(sql)
            #Bajar los datos del limbo a una lista
            datos=cursor.fetchmany(size=cantidad)
            #Retorno de quien nos pida los datos
            return datos
        except Exception as e:
            print("Error en la Consulta General: {}".format(e))
        con.desconectar()

    @classmethod
    def mostrar_uno_arma(cls, id_arma):
        try:
            con=Conexion(host,user,password,db)
            sql="Select * From usuario where id_usuario={}".format(id_arma)
            #Solicitar la ejecución y almacenaremos el resultado
            cursor=con.ejecuta_query(sql)
            #Bajar los datos del limbo a una lista
            datos=cursor.fetchmany()
            con.desconectar()
            #Retorno de quien nos pida los datos
            return datos
        except Exception as e:
            print("Error en la Consulta General: {}".format(e))


if __name__ == '__main__':
    pass
    #arma1 = Arma('SMG', 15, 300000, 'MP7')
    # arma1 = (1, 'SMG', 15, 300000, 'MP7')
    # try:
    #     #results = agregar(arma1)
    #     result = modificar(arma1, tipo_arma='Rifle de Asalto', danio=50, municion=4000)
    #     if result:
    #         print("Arma actualizada")
    # except Exception as e:
    #     print("Algo salió mal al momento de actualizar el arma: {}".format(e))

    #eliminar(1)