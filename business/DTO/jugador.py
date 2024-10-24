from DTO.arma import Arma
from utils.validacion_entradas import validar_entrada

class Jugador(Arma):

    def _validar_experiencia(self, experiencia):
        
        experiencia_valida = True
        if not isinstance(experiencia, int):
            print("El valor de la experiencia debe ser numérico")
            experiencia_valida = False
        
        if not 0 < experiencia < 20:
            print("La experienca debe estar entre 0 y 20")
            experiencia_valida = False
        
        return experiencia_valida

    def _validar_salud(self, salud):

        salud_valida = True
        if not isinstance(salud, int):
            print("El valor de la salud debe ser numérico")
            salud_valida = False
        
        if not 0 < salud < 100:
            print("La salud debe estar entre 0 y 100")
            salud_valida = False
        
        return salud_valida

    def _validar_nivel(self, nivel):

        nivel_valido = True
        if not isinstance(nivel, int):
            print("El valor del nivel debe ser numérico")
            nivel_valido = False

        if not 1 < nivel < 10:
            print("El nivel debe estar entre 1 y 10")
            nivel_valido = False
    
        return nivel_valido

    def __init__(self, nombre, nivel, salud, experiencia, id_arma):
        experiencia_valida = self._validar_experiencia(experiencia)
        if not experiencia_valida:
            experiencia = validar_entrada(self._validar_experiencia, 'experiencia')
        
        salud_valida = self._validar_salud(salud)
        if not salud_valida:
            salud = validar_entrada(self._validar_salud, 'salud')
        
        nivel_valido = self._validar_nivel(nivel)
        if not nivel_valido:
            nivel = validar_entrada(self._validar_nivel, 'nivel')

        self.nombre =  nombre
        self.nivel = nivel
        self.salud = salud
        self.experiencia = experiencia
        self.id_arma = id_arma

    def __str__(self):
        return f"Jugador: {self.nombre}"

    def dispararArma(self, arma: str):
        print(f"{arma} fue disaprada")

    def cargarArma(self, arma: str):
        print(f"{arma} fue cargada")


if __name__ == '__main__':
    jugador1 = Jugador('ProPlayer', 1, 100, 890402920, 1)
    print(jugador1)

