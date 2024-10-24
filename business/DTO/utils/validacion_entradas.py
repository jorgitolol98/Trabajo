
# 1. Si el usuario ingresa un valor erróneo, hay que solicitar
# que ingrese un valor correcto

#def preguntar_por_valor(tipo_de_dato: object, valor)

def validar_entrada(funcion_de_validacion, nombre_valor, castear_a=int):
    """
        funcion_de_validacion: funcion que valida el valor ingresado
        nombre_valor: el nombre de la variable o valor que queremos validar
        valor: valor de la variable u objeto que estamos validando 
    """
    
    while True:
        nuevo_valor = input(f"Ingrese un valor correcto para {nombre_valor}: ")
        if not nuevo_valor.isnumeric():
            print("Ingrese un valor numérico!!")
            continue
        nuevo_valor = castear_a(nuevo_valor)
        experiencia_valida = funcion_de_validacion(nuevo_valor)
        if experiencia_valida:
            break
    
    return nuevo_valor