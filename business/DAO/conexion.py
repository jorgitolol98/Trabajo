
import pymysql

class Conexion:
    #Definir un constructor
    def __init__(self,host,user,password,db):
        self.db=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        self.cursor=self.db.cursor()

    def ejecuta_query(self,sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def desconectar(self):
        self.db.close()

    def commit(self):
        self.db.commit()
    
    def rollback(self):
        self.db.rollback()


if __name__ == '__main__':
    host = 'localhost'
    user = 'benjaconnector'
    password = '123456789'
    db = 'poos_juego'
    Conexion(host,user, password, db )
