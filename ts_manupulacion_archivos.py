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


from csv import (
    DictReader, DictWriter
)
import json
from unidecode import unidecode
from datetime import datetime


def convertir_valor(clave: str, valor: str, formato: str) -> (datetime | int):
    """
    Convierte el valor de un campo específico a un tipo apropiado.
    Args:
        clave (str): La clave del valor.
        valor (str): El valor a convertir.
        formato (str): Formato que se desea.
    Returns:
        datetime | float: El valor convertido.
    """
    conversion = valor
    
    if clave in ['Fecha de inicio','Fecha de Fin']:
        if type(valor) == datetime:
            conversion = valor.strftime(formato)
        else:
            conversion = datetime.strptime(valor, formato)
    
    if clave in ['Presupuesto']:
        conversion = int(valor)
    
    return conversion


def copia_csv_original(nombre_archivo: str) -> (list[dict]):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios con los datos del archivo.
    Args:
        nombre_archivo (str): Nombre del archivo CSV a leer.
        
    Returns:
        list: Lista de diccionarios con los datos del archivo CSV.
    """
    lista_aux = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        diccionarios = DictReader(archivo)
        for fila in diccionarios:
            fila_ok = {unidecode(clave): convertir_valor(unidecode(clave), unidecode(valor), '%d-%m-%Y')\
                for clave, valor in fila.items()}
            lista_aux.append(fila_ok)
    
    return lista_aux


def pasar_lista_csv(nombre_archivo: str, lista_datos: list[dict]) -> (None):
    """
    Escribe una lista de diccionarios en un archivo CSV.
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV a escribir.
        lista_datos (list): Lista de diccionarios con los datos a escribir en el archivo CSV.
    """
    if not lista_datos:
        raise ValueError("La lista de datos está vacía.")
    
    encabezado = lista_datos[0].keys()
    with open(nombre_archivo, 'w', encoding='utf-8', newline='') as archivo:
        diccionatio_csv = DictWriter(archivo, fieldnames= encabezado)
        # Escribir las cabeceras
        diccionatio_csv.writeheader()
        # Escribir los datos
        for diccionario in lista_datos:
            fila = {clave: convertir_valor(clave, valor, '%d-%m-%Y') for clave, valor in diccionario.items()}
            diccionatio_csv.writerow(fila)


def convertir_fecha(elemento):
    """
    Convierte objetos datetime a cadenas de texto con formato 'YYYY-MM-DD'.
    """
    if isinstance(elemento, datetime):
        return elemento.strftime('%Y-%m-%d')


def transformar_proyecto(proyecto):
    """
    Transforma un proyecto para que las fechas de inicio y fin se almacenen en una lista.
    """
    fechas_finalizacion = [
        {
            "fecha_inicio": convertir_fecha(proyecto.get('Fecha de inicio')),
            "fecha_fin": convertir_fecha(proyecto.get('Fecha de Fin'))
        }
    ]
    
    nuevo_proyecto = proyecto.copy()
    nuevo_proyecto['fechas'] = fechas_finalizacion
    
    # Elimino los campos individuales de fecha.
    del nuevo_proyecto['Fecha de inicio']
    del nuevo_proyecto['Fecha de Fin']
    
    return nuevo_proyecto


def proyectos_finalizados_json(proyectos: list[dict]) -> (None):
    """
    Filtra proyectos con estado 'Finalizado' y los guarda en un archivo JSON con fechas en una lista.
    Args:
        proyectos (list[dict]): Lista de diccionarios.
    """
    proyectos_finalizados = [proyecto for proyecto in proyectos if\
        proyecto.get('Estado') == 'Finalizado']
    
    proyectos_normalizados = [transformar_proyecto(proyecto) for proyecto in proyectos_finalizados]
    
    with open('ProyectosFinalizados.json', 'w', encoding= 'utf-8') as finalizados_json:
        json.dump(proyectos_normalizados, finalizados_json, ensure_ascii= False, indent= 4, default=convertir_fecha)
