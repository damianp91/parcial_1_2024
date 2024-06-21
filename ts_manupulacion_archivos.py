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


import csv
from unidecode import unidecode
from datetime import datetime

def convertir_valor(clave: str, valor: str) -> (datetime | float):
    """
    Convierte el valor de un campo específico a un tipo apropiado.
    Args:
        clave (str): La clave del valor.
        valor (str): El valor a convertir.
    Returns:
        datetime | float: El valor convertido.
    """
    conversion = valor
    
    if clave in ['Fecha de inicio','Fecha de Fin']:
        conversion = datetime.strptime(valor, '%d-%m-%Y')
    
    if clave in ['Presupuesto']:
        conversion = float(valor)
    
    return conversion


def copia_csv_original(nombre_archivo: str) -> (list):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios con los datos del archivo.
    Args:
        nombre_archivo (str): Nombre del archivo CSV a leer.
        
    Returns:
        list: Lista de diccionarios con los datos del archivo CSV.
    """
    lista_aux = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        diccionarios = csv.DictReader(archivo)
        for fila in diccionarios:
            fila_ok = {unidecode(clave): convertir_valor(unidecode(clave), unidecode(valor)) for clave, valor in fila.items()}
            lista_aux.append(fila_ok)
    
    return lista_aux





