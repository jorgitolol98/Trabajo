import os

from business.DAO.CRUDArma import CRUDArma
from business.DAO.CRUDJugador import CRUDJugador
from business.DAO.CRUDUsuario import CRUDUsuario
from business.DTO.arma import Arma
from business.DTO.jugador import Jugador
from business.DTO.usuario import Usuario


#Cramos la función para Menu Principal
def menuPrincipal():
    os.system('cls')
    print("====================================")
    print("          MENU PRINCIPAL")
    print("====================================")
    print("      1. (C) INGRESAR")
    print("      2. (C) MOSTRAR")
    print("      3. (C) MODIFICAR")
    print("      4. (C) ELIMINAR")
    print("      5. (E) SALIR")
    print("====================================")

#Crear la Función de Memnu Mostrar
def menuMostrar():
    os.system('cls')
    print("====================================")
    print("          MENU MOSTRAR")
    print("====================================")
    print("      1. MOSTRAR TODOS")
    print("      2. MOSTRAR UNO")
    print("      3. MOSTRAR PARCIAL")
    print("      4. VOLVER")
    print("====================================")


#Crear la función para ingresar Datos 
def ingresarDatos():
    os.system('cls')
    print("====================================")
    print("      INGRESO DATOS USUARIO")
    print("====================================")

#Acá solicitamos todos los datos del usuario y los guardamos en variables
id_usuario=(input("Ingrese ID Usuario: "))
password=input("Ingrese Passwrod: ")
c=Usuario(id_usuario, password)
CRUDUsuario.agregar(c) 

#Creamos la Función para mostrar datos

def mostrar():
    menuMostrar()
    try:
        op2=int(input("Ingrese Opción: "))
        if op2==1:
            CRUDUsuario.mostrarTodos()
        elif op2==2:
            CRUDUsuario.mostrarUno()
        elif op2==3:
            CRUDUsuario.mostrarParcial()
        if op2==4:
            return
        else:
            print("La opción ingresada esta fuera de rango :(")
    except ValueError:
        print("por favor ingrese numero valido.")
    input("\n\nPresione Enter para continuar :)")

#Crear la funcion para modificar los datos de usuario
def modificar():
    listaNuevosdatos=[]
    os.system('cls')
    print("***********************")
    print("Modificar Datos Usuario")
    print("***********************")
    CRUDUsuario.mostrarTodos()
    id_usuarioMOD=int(input("ngrese Id de Usuario a Modificar: "))
    #Debo solicitar los datos del usuario elegido
    dato=CRUDUsuario.mostrarUno(id_usuarioMOD)
    print("ID Usario      :{}".format(dato[0]))
    listaNuevosdatos.append(dato[0])
    print ("Contraseña Usuario    :{}".format(dato[1]))
    listaNuevosdatos.append(dato[1])
    opm.lower("Desea modificar el ID de USuario: ")
    if opm.lower() == "si":
        nuevoID = input("Ingrese el nuevo ID de Usuario: ")
        listaNuevosdatos[0]= nuevoID
    opm = input("Ingrese la nueva contraseña:{} -[SI/NO]".format(dato[0]))

