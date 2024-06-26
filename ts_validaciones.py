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

import os
from datetime import(
    datetime
)

from ts_manupulacion_archivos import(
    pasar_lista_csv
)

def limpiar_consola():
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: 
        os.system('cls')   


def validar_entero(numero_str: str, minimo: int, maximo: int) -> (bool):
    """
    Valida si una cadena representa un número entero dentro de un rango específico.
    Args:
        numero_str (str): Cadena que se desea validar.
        minimo (int): Valor mínimo aceptado.
        maximo (int): Valor máximo aceptado.
    Returns:
        bool: True si la cadena representa un número entero dentro del 
        rango especificado, False en caso contrario.
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
        bool: True si la cadena representa caracteres alfanumericos dentro 
        del rango especificado, False en caso que sean solo alfabeticos.
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
        datetime: Devuelve objeto de tipo datetime o None en caso de no ingresar los datos
        correctamente.
    """
    dia = input("\nIngrese dia (dd): ")
    mes = input("Ingrese mes (mm): ")
    anio = input("Ingrese anio (aaaa): ")
    
    fecha = None
    if validar_entero(dia, 1, 31) and validar_entero(mes, 1, 12)\
        and validar_entero(anio, 1800, 3000):
            formato = f"{int(dia):02d}/{int(mes):02d}/{anio}"
            
            try:
                fecha = datetime.strptime(formato, '%d/%m/%Y')
                print("\nFecha correcta")
            except:
                print("\nLa fecha ingresada no es válida.")
    
    else:
        print("\nEl dato ingresado no es numerico o no respeta el formato pedido (dd)(mm)(aaaa)")
    
    return fecha


def validador_fechas(fecha_1, fecha_2) -> (bool):
    """
    Funcion encargada de validar que fecha_1 sea menos a fecha_2
    Args:
        fecha_1 (datetime): Ojeto de tipo fecha 
        fecha_2 (datetime): Ojeto de tipo fecha 
    Returns:
        bool: True si fecha_1 es menor que fecha_2, de lo contrario False.
    """
    validado_ok = False
    
    try:
        validado_ok = fecha_2 > fecha_1
    except TypeError:
        print("\n¡¡¡No se ingreso una o las dos fechas!!!")
    
    return validado_ok


def estado_proyecto() -> (str):
    """
    Se asigna por defecto el valor Activo, pero el usuario puede elegir
    asignar el estado Cancelado o Filanizado
    Returns:
        (str): Retorna una cadena de caracteres
    """
    estado = {"1":"Activo", "2":"Cancelado", "3":"Finalizado"}
    estado_ok = estado["1"]
    print("\nPor defecto se asigna el estado de Activo al proyecto")
    opcion = input("Presione ENTER para continuar o Ingrese 2 para 'Cancelado' o 3 para 'Filanizado' si desea cambiar el estado: ")
    
    if validar_entero(opcion, 1, 3) and (int(opcion) == 2 or int(opcion) == 3):
        estado_ok = estado.get(opcion)
        print(f"\nEstado se cambio correctamente a: {estado_ok}")
    else:
        print(f"\nSe asigna estado: {estado_ok}")
    
    return estado_ok


def bucar_proyecto(proyectos: list[dict], clave: str, valor: str) -> (bool):
    """
    Busca por clave y valor si el elemnto esta en la lista de diccionarios
    retorna un True 
    Args:
        proyectos (list[dict]): Lista de diccionarios de proyectos
        calve (str): calve a buscar
        valor (str): valor a comparar
    Returns:
        (bool): Retorna un True si se encuantra el valor o por defecto retorna un False
    """
    buscar_ok = False
    for proyecto in proyectos:
        if proyecto.get(clave) == valor:
            buscar_ok = True
    
    return buscar_ok


def verificador_formato_fecha(valor: str, formato: str= '%d/%m/%Y') -> (str):
    """
    Verifica si una fecha esta en el formato requerido. Si no, la formatea al formato
    especificado.
    Args:
        valor (str): La fecha a verificar.
        formato (str): El formato deseado. Por defecto es '%d/%m/%Y'.
    Returns:
        str | datetime: La fecha en el formato especificado.
    """
    formato_ok = ""
    try:
        # En caso que sea un objeto datetime
        if isinstance(valor, datetime):
            formato_ok = valor.strftime(formato)
        # En caso que sea un strin y tenga formato d/m/a
        else:
            fecha = datetime.strptime(valor, '%d-%m-%Y')
            formato_ok = fecha.strftime(formato)
    
    except ValueError:
        try:
            # En caso que sean un valor distinto a los anteriores
            datetime.strptime(valor, formato)
            formato_ok = valor
        
        except ValueError:
            # No es ninguno de los tres.
            raise ValueError(f"La fecha '{valor}' no está en un formato válido.")
    
    return formato_ok


def fecha_hoy() -> (datetime):
    """
    Obtiene la fecha actual y la devuelve como un objeto datetime.
    
    Returns:
        datetime: La fecha actual como un objeto datetime.
    """
    hoy = datetime.now()
    
    return hoy


def normalizar_frase(frase: str) -> (str):
    """
    Capitaliza las palabras de más de tres caracteres en una frase.
    Args:
        frase (str): Cadena de caracteres a normalizar.
    Returns:
        str: Frase normalizada con palabras de más de tres caracteres
        capitalizadas.
    """
    frase = frase.split()
    list_aux = []
    
    for palabra in frase:
        if len(palabra) > 3:
            palabra = palabra.capitalize()
        list_aux.append(palabra)
    
    frase_hecha = ' '.join(list_aux)
    
    return frase_hecha


def rango_fechas(fecha_inicio: tuple, fecha_fin: tuple, fecha: datetime) -> (bool):
    """
    Verifica si una fecha está dentro de un rango específico.
    Args:
        fecha_inicio (tuple): Tupla con el año, mes y día de la fecha de inicio (ej. (2020, 3, 1)).
        fecha_fin (tuple): Tupla con el año, mes y día de la fecha de fin (ej. (2021, 12, 31)).
        fecha (datetime): La fecha a verificar.  
    Returns:
        bool: True si la fecha está en el rango, False de lo contrario.
    """
    fecha_ok = False
    try: 
        inicio = datetime(fecha_inicio[0], fecha_inicio[1], fecha_inicio[2])
        fin = datetime(fecha_fin[0], fecha_fin[1], fecha_fin[2])
        fecha_ok = inicio <= fecha <= fin
    except (IndexError, ValueError) as falla:
        print(f"\nError al crear las fechas: {falla}. Verifique el ingreso de las fecha a comparar.")
    
    return fecha_ok


def validar_salida(proyectos: list[dict]) -> (None):
    """
    Valida que el usuario quiera salir y guardar o no cambios en lista de proyectos
    Args:
        proyectos (list[dict]): Lista de proyectos a guardar
    """
    guardar = True
    while guardar:
        eleccion = input("\n¿Desea guardar los cambios? (s/n): ").lower()
        if validar_caracteres(eleccion, 1):
            if eleccion == 's':
                pasar_lista_csv('Proyectos.csv', proyectos)
                guardar = False
            elif eleccion == 'n':
                print("\nNo se hace cambios en lista de proyectos")
                guardar = False
            else:
                print("\n¡Debe elegir entre 's' y 'n' para poder salir del parcial!")
        else:
            print("\n¡Debe elegir entre 's' y 'n' para poder salir del parcial!")
