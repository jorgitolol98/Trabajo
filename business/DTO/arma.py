
from business.DTO.utils.validacion_entradas import validar_entrada

class Arma:

    def _validar_municion(self, municion):
        
        municion_valida = True
        if not isinstance(municion, int):
            print("El valor de la munición debe ser numérico")
            municion_valida = False

        if not (1 < municion < 500):
            print("La munición debe estar entre 1 y 500")
            municion_valida = False
        
        return municion_valida
    
    def _validar_danio(self, danio):
        
        danio_valido = True
        if not isinstance(danio, int):
            print("El valor del daño debe ser numérico")
            danio_valido = False
        
        if not 0 < danio < 100:
            print("El daño debe estar entre 0 y 100")
            danio_valido = False
        
        return danio_valido
    
    def __init__(self, tipo_arma, danio, municion, nombre):
        municion_valida = self._validar_municion(municion)
        print(municion_valida)
        if not municion_valida:
            municion = validar_entrada(self._validar_municion, 'municion')

        danio_valido = self._validar_danio(danio)
        if not danio_valido:
            danio = validar_entrada(self._validar_danio, 'daño')
    
        self.tipo_arma = tipo_arma
        self.danio = danio
        self.municion = municion
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} - {self.tipo_arma}"


if __name__ == '__main__':
    arma1 = Arma('SMG', 15, 300000, 'MP7')
    print(arma1)
