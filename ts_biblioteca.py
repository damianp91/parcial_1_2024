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
from ts_validaciones import(
    validar_caracteres, validador_fechas, validar_entero, 
    ingreso_fecha, estado_proyecto
    )
from ts_menus import menu_modificar


def limpiar_consola():
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: 
        os.system('cls')   
# 1. Ingresar proyecto: Pedirá los datos necesarios y dará de alta a un nuevo proyecto, asignando
#     un ID autoincremental.
def ingreso_datos() -> (list):
    """
    Encargado de dar vingreso a nuevos datos siempre y cuando se sigan las reglas de validacion \
        informadas para cada caso.
    Returns:
        (list): Devuelve listado con datos recopilados en si formato especficado
    """
    aux_list = []
    
    # Nombre proyecto
    nombre_proyecto = input("Ingrese nombre de proyecto (que no exceda los 30 caracteres): ")
    if validar_caracteres(nombre_proyecto, 30):
        aux_list.append(nombre_proyecto)
        print("Nombre correctamente agregado.")
    else:
        print(f" EL nombre {nombre_proyecto} excede los 30 caracteres o no es alfabetico (a-z)")
    
    # Descripcion proyecto
    descripcion = input("Ingrese descripcion de proyecto (que no exceda los 200 caracteres): ")
    if validar_caracteres(descripcion, 200, True):
        aux_list.append(descripcion)
        print("Descripcion correctamente agregada.")
    else:
        print(f" La descripcion excede los 200 caracteres o no es alfanumerico")
    
    # Fecha de inicio y fin
    fecha_1 = ingreso_fecha()
    fecha_2 = ingreso_fecha()
    if validador_fechas(fecha_1, fecha_2):
        fecha_final_1 = fecha_1.strftime('%d/%m/%Y')
        fecha_final_2 = fecha_2.strftime('%d/%m/%Y')
        aux_list.append(fecha_final_1)
        aux_list.append(fecha_final_2)
        print("Fechas válidas y agregadas.")
    else:
        print("Fechas no corresponden al formato (dd/mm/aaaa) o fecha fin es menor a fecha inicio")
    
    # Presupuesto
    presupuesto = input("Ingrese presupuesto para el proyecto (Debe ser mayor a 500000 inclusive): ")
    if validar_entero(presupuesto, 500000, 10000000):
        aux_list.append(int(presupuesto))
        print("Presupuesto Ingresado correctamente")
    else:
        print("No se pudo ingresar correctamente presupuesto. Verifique el monto")
    
    # Estado
    aux_list.append(estado_proyecto())
    
    return aux_list


def conteo_elemento_estado(proyectos: list[dict], clave: str, valor: str) -> (int):
    """
    Busca por calve en lista de diccionarios si existe el valor y hace un conteo
    Args:
        proyectos (list[dict]): lista de diccionarios
        clave (str): clave de cada dicionario para buscar
        valor (str): valor de la calve a comparar
    Returns:
        int: por defecto devuelve un cero si no encuentra elementos o la cantidad\
            de elementos encontrados
    """
    conteo = 0
    for proyecto in proyectos:
        if proyecto.get(clave) == valor:
            conteo += 1
    
    return conteo


def ts_ingreso_datos_proyecto(proyectos: list[dict]) -> (None):
    """
    Se encarga de asignar un id de manera autoincremental a cada proyecto ademas de
    agregar diccionarios a la lista ingresada por parametro en la funcion
    Args:
        proyectos (list): Lista con diccionaros o vacia
    """
    if conteo_elemento_estado(proyectos, "Estado", "Activo") < 50:
        id = len(proyectos) + 1
        
        try:
            datos = ingreso_datos()
            proyecto_nuevo = {
                "id":str(id),
                "Nombre del Proyecto":datos[0],
                "Descripcion":datos[1],
                "Fecha de inicio":datos[2],
                "Fecha de Fin":datos[3],
                "Presupuesto":datos[4],
                "Estado":datos[5]}
            
            proyectos.append(proyecto_nuevo)
        
        except IndexError:
            print("No se ingreso datos de proyecto, si desea ingresar un proyecto por favor intente de nuevo siguiendo el formato requerido.")
    else:
        print("El proyecto excede la capacidad maxima (50 proyectos en estado Activo)")

# 2. Modificar proyecto: Permitirá alterar cualquier dato del proyecto excepto su ID. Se usará el ID
#     para identificar al proyecto a modificar. Se mostrará un submenú para seleccionar qué datos
#     modificar. Se indicará si se realizaron modificaciones o no.
# 5. Mostrar todos: Imprimirá por consola la información de todos los proyectos en formato de
#     tabla:
#         | Nombre del Proyecto | Descripción      | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado    |
#         | Innovación AI       | Desarrollo de IA | $1,000,000  | 01/01/2024      | 01/01/2025   | Activo    |
#         | Rediseño Web        | Nueva página web | $300,000    | 15/02/2024      | 30/06/2024   | Cancelado |
def mostrar_proyecto(proyecto: dict) -> (str):
    """
    Muestra por consola diccionario en formato tabla
    Args:
        proyecto (dict): Diccionario a formatear como tabla
    Returns:
        (str): Cadena de caracteres con datos de diccionario
    """
    #presupuesto_formateado = int("${:,.0f}".format(proyecto['Presupuesto']))
    mensaje = f"| {proyecto['Nombre del Proyecto']:40} | {proyecto['Descripcion']:90} | ${proyecto['Presupuesto']:10}\
 | {proyecto['Fecha de inicio']:12} | {proyecto['Fecha de Fin']:12} | {proyecto['Estado']:10} |"
    
    return mensaje


def ts_mostrar_proyectos(proyectos: list[dict]) -> (None):
    """
    Muestra por consola proyectos en formato tabla
    Args:
        proyectos (list[dict]): Lista de diccionarios con proyectos
    """
    print("-----------------------------------------------------------------------------------\
 Presupuestos TechSolutions -----------------------------------------------------------------------------------")
    print(f"| {'Nombre proyecto':^40} | {'Descripcion proyecto':^90} | {'Presupuesto':10} | {'Fecha inicio':10}\
 | {'Fecha Fin':^12} | {'Estado':^10} |")
    print("-------------------------------------------------------------------------------------\
-------------------------------------------------------------------------------------------------------------")
    for proyecto in proyectos:
        print(mostrar_proyecto(proyecto))
    print("--------------------------------------------------------------------------------------\
------------------------------------------------------------------------------------------------------------")


def bucar_proyecto(proyectos: list[dict], clave: str, valor: str) -> (bool):
    """
    Busca por calve y valor si el elemnto esta en la lista de diccionarios
    y lo muestra por pantalla 
    Args:
        proyectos (list[dict]): Lista de diccionarios de proyectos
        calve (str): calve a buscar
        valor (str): valor a comparar
    Returns:
        (bool): Retorna un True si se encuantra el valor o por defecto retorna un False
    """
    buscaror_ok = False
    for proyecto in proyectos:
        if proyecto.get(clave) == valor:
            print(mostrar_proyecto(proyecto))
            buscaror_ok = True
    
    return buscaror_ok


def modificar(proyecto: dict, valor: int) -> (dict):
    """
    Permite modificar un proyecto existente basado en una opción seleccionada.
    Args:
        proyecto (dict): Proyecto a modificar.
        valor (int): Opción seleccionada para modificar.
    Returns:
        dict: Proyecto modificado.
    """
    match valor:
        case 1:
            nombre_proyecto = input("Ingrese nombre de proyecto (que no exceda los 30 caracteres): ")
            if validar_caracteres(nombre_proyecto, 30):
                proyecto['Nombre del Proyecto'] = nombre_proyecto
                print("Nombre correctamente agregado.")
            else:
                print(f" EL nombre {nombre_proyecto} excede los 30 caracteres o no es alfabetico (a-z)")
        case 2:
            descripcion = input("Ingrese descripcion de proyecto (que no exceda los 200 caracteres): ")
            if validar_caracteres(descripcion, 200, True):
                proyecto['Descripcion'] = descripcion
                print("Descripcion correctamente agregada.")
            else:
                print(" La descripcion excede los 200 caracteres o no es alfanumerico")
        case 3:
            presupuesto = input("Ingrese presupuesto para el proyecto (Debe ser mayor a 500000 inclusive): ")
            if validar_entero(presupuesto, 500000, 10000000):
                proyecto['Presupuesto'] = int(presupuesto)
                print("Presupuesto Ingresado correctamente")
            else:
                print("No se pudo ingresar correctamente presupuesto. Verifique el monto")
        case 4:
            fecha_1 = ingreso_fecha()
            if validador_fechas(fecha_1, proyecto['Fecha de Fin']):
                fecha_final = fecha_1.strftime('%d/%m/%Y')
                proyecto['Fecha de inicio'] = fecha_final
                print("Fecha valida y agregada.")
            else:
                print("Fechas no corresponden al formato (dd/mm/aaaa) o fecha fin es menor a fecha inicio")
        case 5:
            fecha_2 = ingreso_fecha()
            if validador_fechas(proyecto['Fecha de inicio'], fecha_2):
                fecha_final = fecha_2.strftime('%d/%m/%Y')
                proyecto['Fecha de Fin'] = fecha_final
                print("Fechas válidas y agregadas.")
            else:
                print("Fechas no corresponden al formato (dd/mm/aaaa) o fecha fin es menor a fecha inicio")
        case 6:
            nuevo_estado = estado_proyecto()
            proyecto['Estado'] = nuevo_estado
        case 7:
            print("Se cancela modificacion.")
        
    return proyecto


def bucar_indice(proyectos: list[dict], clave: str, valor: str):
    """_summary_
    Args:
        proyectos (list[dict]): _description_
        clave (str): _description_
        valor (str): _description_
    Returns:
        _type_: _description_
    """
    indice =  -1
    for ind, diccionario in enumerate(proyectos):
        if diccionario.get(clave) == valor:
            indice = ind
    
    return indice


def ts_modificar_proyecto(proyectos: list[dict]) -> (None):
    """
    Permite modificar un proyecto dentro de la lista de proyectos.
    
    Args:
        proyectos (list[dict]): Lista de diccionarios que representan proyectos.
    """
    buscar = input("Ingrese ID de proyecto a modificar: ")
    if validar_entero(buscar, 1, 500) and bucar_proyecto(proyectos, "id", buscar):
        menu_modificar()
        opcion = input("Ingrese opcion a modificar: ")
        if validar_entero(opcion, 1, 7):
            indice = bucar_indice(proyectos, "id", buscar)
            proyectos[indice] = modificar(proyectos[indice], int(opcion))
            print("Proyecto modificado exitosamente.")
        else:
            print("Opción no válida. Debe ingresar un número entre 1 y 7.")
    else:
        print("No se encontro proyecto")


# 3. Cancelar proyecto: Cancelará un proyecto de la lista original. Se pedirá el ID del proyecto a
#     cancelar.
# 4. Comprobar proyectos: Cambiará el estado de todos los proyectos cuya fecha de finalización
#     ya haya sucedido.
# 6. Calcular presupuesto promedio: Calculará e imprimirá el presupuesto promedio de todos los
#     proyectos.


# 7. Buscar proyecto por nombre: Permitirá al usuario buscar y mostrar la información de un
#     proyecto específico ingresando su nombre.


# 8. Ordenar proyectos: Ofrecerá la opción de ordenar y mostrar la lista de proyectos por nombre,
#     presupuesto, o fecha de inicio de forma ascendente o descendente.
def ordenar_personajes_valor(proyectos: list[dict], key: str, may_men: str) -> (list[dict]):
    """
    Ordena una lista de diccionarios segun criterio
    Args:
        personajes (list[dict]): Lista de diccionarios a ordenar
        key (str): Clave a evaluar
        may_men (str): Opcion de sentido de orde debe ser 'menor' o 'mayor'
    Returns:
        (list[dict]): Lita de diccionarios ordenados
    """
    if len(proyectos) < 2:
        return proyectos
    
    pivot_personaje = proyectos.pop()
    pivot_valor = pivot_personaje[key]
    mayor = []
    menor = []
    
    for personaje in proyectos:
        if may_men == "menor":
            if personaje.get(key) > pivot_valor:
                mayor.append(personaje)
            else:
                menor.append(personaje)
        else:
            if personaje.get(key) < pivot_valor:
                mayor.append(personaje)
            else:
                menor.append(personaje)
    
    return ordenar_personajes_valor(menor, key, may_men) + [pivot_personaje] + ordenar_personajes_valor(mayor, key, may_men)


def ts_mostrar_personajes_ordenados(proyectos: list[dict], key: str, may_men: str):
    """
    Muestra por consola lista de diccionario ordenada segun criterio
    Args:
        personajes (list[dict]): Lista de diccionarios 
        key (str): Clave a evaluar
        may_men (str): Opcion de sentido de orde debe ser 'menor' o 'mayor'
    Returns:
        (int): Devuelve -1 si la lista es uan lista vacio o muestra por consola la lista 
        ordenada segun criterio
    """
    if proyectos:
        personajes_ord = ordenar_personajes_valor(proyectos, key, may_men)
        ts_mostrar_proyectos(personajes_ord)
    else:
        return -1
# 9. Retomar proyecto: Vuelve a dar de alta un proyecto Cancelado, comprobando anteriormente
#    que cumpla todos los requisitos para esto.
# 10. Mostrar todos los proyectos terminados en medio de la cuarentena del COVID 19 (Marzo de 2020
#     hasta el fin del 2021 por ejemplo). En caso de que no haya indicar error
# 11. Realizar un top 3 de los proyectos activos con mayor presupuesto que hayan sido iniciados en la
#     década de los 10’ (1 de Enero de 2010 hasta 31 de Diciembre de 2019). Verificar qué haya la cantidad
#     deseada de proyectos , sino indicar un mensaje de error.
# 12. Salir: Terminará la ejecución del programa.






