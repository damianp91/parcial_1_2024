# Licencia MIT
#
# Copyright (c) 2024 [Github](https://github.com/damianp91) Todos los derechos reservados.
#
# Se concede permiso por la presente, de forma gratuita, a cualquier persona que obtenga una copia
# de este software y los archivos de documentación asociados (el "Software"), para usar
# el Software sin restricciones, incluyendo sin limitación los derechos para usar, copiar,
# modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software,
# y para permitir a las personas a quienes se les proporcione el Software hacer lo mismo, 
# sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso se incluirán en todas
# las copias o partes sustanciales del Software.
#
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
# IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIABILIDAD,
# IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS
# AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS
# U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO,
# QUE SURJA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL
# SOFTWARE.


from datetime import datetime


def validar_entero(numero_str: str, minimo: int, maximo: int) -> (bool):
    """
    Valida si una cadena representa un número entero dentro de un rango específico.
    Args:
        numero_str (str): Cadena que se desea validar.
        minimo (int): Valor mínimo aceptado.
        maximo (int): Valor máximo aceptado.
    Returns:
        bool: True si la cadena representa un número entero dentro del rango especificado, False en caso contrario.
    """
    validador_ok = False
    
    if numero_str.isdigit():
        numero = int(numero_str)
        validador_ok = minimo <= numero <= maximo
    
    return validador_ok


def validar_caracteres(texto: str, longitud: int, alfanumerico= False) -> (bool):
    """
    Valida cadena de caracteres si son alfabeticos o alfanumericos segun
    eleccion por parametro
    Args:
        texto (srt): cadena de caracteresa evaluar
        longitud (int): La cantidad de caracteres que se permitira validar
        alfanumerico (bool): por defecto es False, pero si se desea validar
        cadena de caracteres alfanumeroricos puede agregarse True
    Returns:
        (bool): Devuelve un valor de tipo bool si se hizo o no la validacion
    """
    validador_ok = False
    tex_aux = texto.replace(' ', '')
    
    if alfanumerico:
        if len(texto) <= longitud:
            validador_ok = tex_aux.isalnum()
    else:
        if len(texto) <= longitud:
            validador_ok = tex_aux.isalpha()
    
    return validador_ok


def ingreso_fecha() -> (datetime):
    """
    Pide por consola dia, mes, anio para ser validados y formateados como (dd/mm/aaaa)
    Returns:
        datetime: Devuelve objeto de tipo datetime
    """
    dia = input("Ingrese dia (dd): ")
    mes = input("Ingrese mes (mm): ")
    anio = input("Ingrese anio (aaaa): ")
    
    if validar_entero(dia, 1, 31) and validar_entero(mes, 1, 12)\
        and validar_entero(anio, 1800, 3000):
            formato = f"{int(dia):02d}/{int(mes):02d}/{anio}"
            fecha = datetime.strptime(str(formato), '%d/%m/%Y')
            print("Fecha correcta")
    
    else:
        print("El dato ingresado no es numerico o no respeta el formato pedido (dd)(mm)(aaaa)")
    
    return fecha


def validador_fechas(fecha_1, fecha_2) -> (bool):
    """
    Funcion encargada de validar que fecha 1 sea menos a fecha 2
    Args:
        fecha_1 (datetime): Ojeto de tipo fecha 
        fecha_2 (datetime): Ojeto de tipo fecha 
    Returns:
        (bool): Dependiendo si es mayor o menor los valores ingresados
                por parametro
    """
    return fecha_2 > fecha_1


def estado_proyecto() -> (str):
    """
    Se asigna por defecto el valor Activo, pero el usuario puede elegir
    asignar el estado Cancelado o Filanizado
    Returns:
        (str): Retorna una cadena de caracteres
    """
    estado = {"1":"Activo", "2":"Cancelado", "3":"Filanizado"}
    estado_ok = estado["1"]
    print("Por defecto se asigna el estado de Activo al proyecto")
    opcion = input("Presione 1 para continuar o Ingrese 2 para 'Cancelado' o 3 para 'Filanizado' si desea cambiar el estado: ")
    
    if validar_entero(opcion, 1, 3) and (int(opcion) == 2 or int(opcion) == 3):
        estado_ok = estado[opcion]
        print(f"Estado se cambio correctamente a: {estado_ok}")
    else:
        print(f"Se asigna estado: {estado_ok}")
    
    return estado_ok