from DTO.arma import Arma
from DTO.jugador import Jugador


class Usuario:

    def __init__(self, id_usuario, password):
        
        self.id_usuario = id_usuario
        self.password = password
    
    def __str__(self):
        return f"Nombre: {self.id_usuario} {self.password}"
    

