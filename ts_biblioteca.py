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


from ts_validaciones import(
    validar_caracteres, validador_fechas, validar_entero, 
    ingreso_fecha, estado_proyecto, verificador_formato_fecha,
    fecha_hoy, normalizar_frase, bucar_proyecto, rango_fechas
    )

from ts_menus import(
    menu_principal, menu_modificar, menu_ornenamiento, menu_menor_mayor
)


# 1. Ingresar proyecto: Pedirá los datos necesarios y dará de alta a un nuevo proyecto, asignando
#     un ID autoincremental.
def ts_menu_principal() -> (int):
    """
    Muestra en cosola menu principal y valida si la opcion ingresada sea correcta
    Returns:
        (int): devuelve -1 si no es un valor numerico o el valor ingresado
    """
    valor = -1
    menu_principal()
    opcion = input("\nIngrese la opcion (1-12): ")
    if validar_entero(opcion, 1, 12):
        valor = int(opcion)
    return valor


def ingreso_datos() -> (dict):
    """
    Encargado de dar vingreso a nuevos datos siempre y cuando se sigan las reglas de validacion
    informadas para cada caso.
    Returns:
        dict: Devuelve un diccionario con datos recopilados en su formato especificado
    """
    aux_list = []
    
    # Nombre proyecto
    nombre_proyecto = input("\nIngrese nombre de proyecto (que no exceda los 30 caracteres): ")
    if validar_caracteres(nombre_proyecto, 30):
        aux_list.append(normalizar_frase(nombre_proyecto))
        print("\nNombre correctamente agregado.")
    else:
        print(f"\nEL nombre {nombre_proyecto} excede los 30 caracteres o no es alfabetico (a-z)")
    
    # Descripcion proyecto
    descripcion = input("\nIngrese descripcion de proyecto (que no exceda los 200 caracteres): ")
    if validar_caracteres(descripcion, 200, True):
        aux_list.append(descripcion.capitalize())
        print("\nDescripcion correctamente agregada.")
    else:
        print(f"\nLa descripcion {descripcion} excede los 200 caracteres o no es alfanumerico")
    
    # Fecha de inicio y fin
    fecha_1 = ingreso_fecha()
    fecha_2 = ingreso_fecha()
    if validador_fechas(fecha_1, fecha_2):
        aux_list.append(fecha_1)
        aux_list.append(fecha_2)
        print("\nFechas válidas y agregadas.")
    else:
        print("\nFechas no corresponden al formato (dd/mm/aaaa) o fecha fin es menor a fecha inicio")
    
    # Presupuesto
    presupuesto = input("\nIngrese presupuesto para el proyecto (Debe ser mayor a 500000 inclusive): ")
    if validar_entero(presupuesto, 500000, 10000000):
        aux_list.append(int(presupuesto))
        print("\nPresupuesto Ingresado correctamente")
    else:
        print("\nNo se pudo ingresar correctamente presupuesto. Verifique el monto")
    
    # Estado
    aux_list.append(estado_proyecto())
    
    try:
        return {"Nombre del Proyecto":aux_list[0],"Descripcion":aux_list[1],"Fecha de inicio":aux_list[2],
                "Fecha de Fin":aux_list[3],"Presupuesto":aux_list[4],"Estado":aux_list[5]}
    except IndexError:
        print("\nNo se pudo ingresar nuevo proyecto, verifique los datos e intente de nuevo.")


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
    if proyectos:
        for proyecto in proyectos:
            if proyecto.get(clave) == valor:
                conteo += 1
    else:
        conteo
    
    return conteo


def asignacion_id(proyectos: list[dict]) -> (int):
    """
    Asigna un nuevo ID autoincremental basado en los IDs existentes en la lista de proyectos.
    Args:
        proyectos (list[dict]): Lista de diccionarios con los proyectos existentes.
    Returns:
        int: El nuevo ID autoincremental.
    """
    id = 1
    if proyectos:
        ultimo_id = max(int(proyecto['id']) for proyecto in proyectos)
        id = ultimo_id + 1 
    
    return id


def ts_ingreso_datos_proyecto(proyectos: list[dict]) -> (None):
    """
    Se encarga de asignar un ID de manera autoincremental a cada proyecto, ademas de
    agregar diccionarios a la lista ingresada por parametro en la funcion
    Args:
        proyectos (list[dict]): Lista con diccionaros o vacia
    """
    if conteo_elemento_estado(proyectos, "Estado", "Activo") < 50:
        id = asignacion_id(proyectos)
        datos = ingreso_datos()
        
        try:
            if len(datos) == 6:
                ingreso_id = {'id': str(id)}
                datos.update(ingreso_id)
                proyectos.append(datos)
                print(f"\nIngreso de nuevo proyecto con ID: {id}.")
            else:
                print("\nNo se ingreso datos de proyecto, si desea ingresar un proyecto por favor intente\
                de nuevo siguiendo el formato requerido.")
        except TypeError:
            print("\nNo ingreso ningun dato, verifique sus dato e intente de nuevo.")
    else:
        print("\nEl proyecto excede la capacidad maxima (50 proyectos en estado Activo).")
# 5. Mostrar todos: Imprimirá por consola la información de todos los proyectos en formato de
#     tabla:
#         | Nombre del Proyecto | Descripción      | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado    |
#         | Innovación AI       | Desarrollo de IA | $1,000,000  | 01/01/2024      | 01/01/2025   | Activo    |
#         | Rediseño Web        | Nueva página web | $300,000    | 15/02/2024      | 30/06/2024   | Cancelado |
def mostrar_proyecto(proyecto: dict) -> (None):
    """
    Muestra por consola diccionario en formato tabla
    Args:
        proyecto (dict): Diccionario a formatear como tabla
    """
    presupuesto_formateado = "${:,.0f}".format(float(proyecto['Presupuesto']))
    fecha_inicio = verificador_formato_fecha(proyecto['Fecha de inicio'])
    fecha_fin = verificador_formato_fecha(proyecto['Fecha de Fin'])
    
    mensaje = f"| {proyecto['Nombre del Proyecto']:40} | {proyecto['Descripcion']:90} | {presupuesto_formateado:>12}\
 | {fecha_inicio:^12} | {fecha_fin:^12} | {proyecto['Estado']:^10} |"
    
    print(mensaje)


def ts_mostrar_proyectos(proyectos: list[dict]) -> (None):
    """
    Muestra por consola proyectos en formato tabla
    Args:
        proyectos (list[dict]): Lista de diccionarios con proyectos
    """
    print("-" * 195)
    print("|\t\t\t\t\t\t\t\t\t\t  Proyectos TechSolutions\t\t\t\t\t\t\t\t\t\t\t  |")
    print("-" * 195)
    print(f"| {'Nombre proyecto':^40} | {'Descripcion proyecto':^90} | {'Presupuesto':12} | {'Fecha inicio':10}\
 | {'Fecha Fin':^12} | {'Estado':^10} |")
    print("-" * 195)
    for proyecto in proyectos:
        mostrar_proyecto(proyecto)
    print("-" * 195)


def mostrar_clave_valor(proyectos: list[dict], clave: str, valor: str) -> (list[dict]):
    """
    Agrega a una lista de retorno el o los diccionarios que cumplan con con el criterio
    de clave y valor
    Args:
        proyectos (list[dict]): Lista de diccionarios
        clave (str): calve de diccionario
        valor (str): valor de la clave
    Returns:
        list: lista de elementos, elemento o lista vacia 
    """
    retorno_lista = []
    if proyectos:
        for proyecto in proyectos:
            if proyecto.get(clave) == valor:
                retorno_lista.append(proyecto)
    
    return retorno_lista
# 2. Modificar proyecto: Permitirá alterar cualquier dato del proyecto excepto su ID. Se usará el ID
#     para identificar al proyecto a modificar. Se mostrará un submenú para seleccionar qué datos
#     modificar. Se indicará si se realizaron modificaciones o no.
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
            nombre_proyecto = input("\nIngrese nombre de proyecto (que no exceda los 30 caracteres): ")
            if validar_caracteres(nombre_proyecto, 30):
                proyecto['Nombre del Proyecto'] = normalizar_frase(nombre_proyecto)
                print("\nNombre correctamente agregado.")
            else:
                print(f"\nEL nombre {nombre_proyecto} excede los 30 caracteres o no es alfabetico (a-z)")
        case 2:
            descripcion = input("\nIngrese descripcion de proyecto (que no exceda los 200 caracteres): ")
            if validar_caracteres(descripcion, 200, True):
                proyecto['Descripcion'] = descripcion.capitalize()
                print("\nDescripcion correctamente agregada.")
            else:
                print(f"\nLa descripcion {descripcion} excede los 200 caracteres o no es alfanumerico")
        case 3:
            presupuesto = input("\nIngrese presupuesto para el proyecto (Debe ser mayor a 500000 inclusive): ")
            if validar_entero(presupuesto, 500000, 10000000):
                proyecto['Presupuesto'] = int(presupuesto)
                print("\nPresupuesto Ingresado correctamente")
            else:
                print("\nNo se pudo ingresar correctamente presupuesto. Verifique el monto")
        case 4:
            fecha_1 = ingreso_fecha()
            if validador_fechas(fecha_1, proyecto['Fecha de Fin']):
                proyecto['Fecha de inicio'] = fecha_1
                print("\nFecha valida y agregada.")
            else:
                print("\nFechas no corresponden al formato (dd/mm/aaaa) o fecha fin es menor a fecha inicio")
        case 5:
            fecha_2 = ingreso_fecha()
            if validador_fechas(proyecto['Fecha de inicio'], fecha_2):
                proyecto['Fecha de Fin'] = fecha_2
                print("\nFechas válidas y agregadas.")
            else:
                print("\nFechas no corresponden al formato (dd/mm/aaaa) o fecha fin es menor a fecha inicio")
        case 6:
            nuevo_estado = estado_proyecto()
            proyecto['Estado'] = nuevo_estado
        case 7:
            print("\nSe cancela modificacion.")
        
    return proyecto


def bucar_indice(proyectos: list[dict], clave: str, valor: str) -> (int):
    """
    Busca un índice dentro de una lista de diccionarios según una clave y un valor específicos.
    Args:
        proyectos (list[dict]): Lista de diccionarios donde buscar.
        clave (str): Clave del diccionario que se utilizará para la búsqueda.
        valor (str): Valor que se está buscando dentro de la clave especificada.
        
    Returns:
        int: Índice del diccionario en la lista donde se encuentra el valor buscado. Si no se encuentra,
            retorna -1.
    """
    indice =  -1
    for i, diccionario in enumerate(proyectos):
        if diccionario.get(clave) == valor:
            indice = i
    
    return indice


def ts_modificar_proyecto(proyectos: list[dict]) -> (None):
    """
    Permite modificar un proyecto dentro de la lista de proyectos.
    Args:
        proyectos (list[dict]): Lista de diccionarios que representan proyectos.
    """
    buscar = input("Ingrese ID de proyecto a modificar: ")
    if validar_entero(buscar, 1, 500):
        indice = bucar_indice(proyectos, "id", buscar)
        if indice != -1 and bucar_proyecto(proyectos, "id", buscar):
            proyecto_modificar = mostrar_clave_valor(proyectos, 'id', buscar)
            ts_mostrar_proyectos(proyecto_modificar)
            menu_modificar()
            opcion = input("Ingrese opcion a modificar: ")
            if validar_entero(opcion, 1, 7):
                if 1 <= int(opcion) <= 6:
                    proyectos[indice] = modificar(proyectos[indice], int(opcion))
                    print("\nProyecto modificado exitosamente.")
                else:
                    print("Se cancela modificacion de proyecto.")
            else:
                print("\nOpción no válida. Debe ingresar un número entre 1 y 7.")
        else:
            print(f"\nEn ID {buscar} no se encontra en lista de proyectos.")
    else:
        print("\nLista de proyectos vacia.")
# 3. Cancelar proyecto: Cancelará un proyecto de la lista original. Se pedirá el ID del proyecto a
#     cancelar.
def ts_cancelar_proyecto(proyectos: list[dict]) -> (None):
    """
    Cancela un proyecto por su ID, cambiando su estado a 'Cancelado' y 
    actualizando la 'Fecha de Fin' a la fecha actual.
    Args:
        proyectos (list[dict]): Lista de proyectos.
    """
    buscar = input("\nIngrese ID de proyecto a cancelar: ")
    if validar_entero(buscar, 1, 500):
        indice = bucar_indice(proyectos, "id", buscar)
        if indice != -1 and bucar_proyecto(proyectos, "id", buscar):
            cancelar = mostrar_clave_valor(proyectos, 'id', buscar)
            ts_mostrar_proyectos(cancelar)
            seleccion = input("\n¿Desea cambiar el estado de este proyecto? (s/n): ").lower()
            if validar_caracteres(seleccion, 1):
                if seleccion == 's':
                    fecha_cancelacion = fecha_hoy()
                    cambio_estado = proyectos[indice]
                    cambio_estado['Estado'] = 'Cancelado'
                    cambio_estado['Fecha de Fin'] = fecha_cancelacion
                    print("\nSe hace cambio de estado con exito.")
                else:
                    print("\nSe cancela cambio de estado.")
            else:
                print("\nNo se pudo cambiar el estado ingreso de respuesta incorrecta\
                    debe ser 's' o 'n'.")
        else:
            print(f"\nNumero {buscar} no se encuentra en la lista de proyectos.")
    else:
        print("\nLista de proyectos vacia.")
# 4. Comprobar proyectos: Cambiará el estado de todos los proyectos cuya fecha de finalización
#     ya haya sucedido.
def ts_comprobar_proyectos(proyectos: list[dict]) -> (None):
    """
    Verifica si la fecha de fin de los proyectos es menor a la fecha actual
    y si el estado del proyecto es 'Activo'. Si es así, cambia el estado a 'Finalizado'.
    Args:
        proyectos (list[dict]): Lista de proyectos.
    """
    if proyectos:
        comprobacion = False
        hoy = fecha_hoy()
        for proyecto in proyectos:
            if proyecto['Fecha de Fin'] < hoy and proyecto.get('Estado') == 'Activo':
                proyecto['Estado'] = 'Finalizado'
                comprobacion = True
        if comprobacion:
            print("\nProyectos verificados y actualizados")
        else:
            print("\nSin proyectos para finalizar.")
    else:
        print("\nLista de proyectos vacia.")
# 6. Calcular presupuesto promedio: Calculará e imprimirá el presupuesto promedio de todos los
#     proyectos.
def ts_promedio_presupuesto(proyectos: list[dict]) -> (None):
    """
    Calcula y muestra el promedio de los presupuestos de los proyectos.
    Args:
        proyectos (list[dict]): Lista de proyectos.
    """
    presupuesto = 0
    if proyectos:
        suma_presupuesto = sum(proyecto['Presupuesto'] for proyecto in proyectos)
        cantidad_proyectos = len(proyectos)
        promedio = suma_presupuesto / cantidad_proyectos
        promedio_final = "$ {:,.0f}".format(promedio)
        print("=" * 60)
        print(f"\nPromedio de presupuestos es: {promedio_final}.")
        print(f"Con un total de {cantidad_proyectos} proyectos.\n")
        print("=" * 60)
    else:
        promedio_final = "$ {:,.0f}".format(presupuesto)
        print("=" * 60)
        print(f"\nPromedio de presupuestos es: {promedio_final}.")
        print("Con un total de 0 proyectos.\n")
        print("=" * 60)
# 7. Buscar proyecto por nombre: Permitirá al usuario buscar y mostrar la información de un
#     proyecto específico ingresando su nombre.
def ts_buscar_proyecto_nombre(proyectos: list[dict]) -> (None):
    """
    Busca y muestra un proyecto por su nombre.
    Args:
        proyectos (list[dict]): Lista de proyectos.
    """
    buscar = input("Escriba el nombre de proyecto a buscar: ")
    if proyectos and validar_caracteres(buscar, 30):
        buscar_ok = normalizar_frase(buscar)
        if bucar_proyecto(proyectos, 'Nombre del Proyecto', buscar_ok):
            encontrado = mostrar_clave_valor(proyectos, 'Nombre del Proyecto', buscar_ok)
            ts_mostrar_proyectos(encontrado)
        else:
            print(f"\nNo se encontro el proyecto: {buscar_ok}.")
    else:
        print(f"\nLista de proyectos vacia.")
# 8. Ordenar proyectos: Ofrecerá la opción de ordenar y mostrar la lista de proyectos por nombre,
#     presupuesto, o fecha de inicio de forma ascendente o descendente.
def ordenar_tabla_valor(proyectos: list[dict], key: str, men_may= True) -> (list[dict]):
    """
    Ordena una lista de diccionarios segun criterio
    Args:
        personajes (list[dict]): Lista de diccionarios a ordenar
        key (str): Clave a evaluar
        may_men (bool): Opcion de sentido por defecto es True si se desea que 
                        el sentido sea de menor a mayor o False en sentido 
                        contrario
    Returns:
        (list[dict]): Lita de diccionarios ordenados
    """
    if len(proyectos) < 2:
        return proyectos
    
    proyectos_copia = proyectos.copy()
    
    pivot = proyectos_copia.pop()
    pivot_valor = pivot.get(key)
    mayor = []
    menor = []
    
    for proyecto in proyectos_copia:
        if men_may:
            if proyecto.get(key) > pivot_valor:
                mayor.append(proyecto)
            else:
                menor.append(proyecto)
        else:
            if proyecto.get(key) < pivot_valor:
                mayor.append(proyecto)
            else:
                menor.append(proyecto)
    
    return ordenar_tabla_valor(menor, key, men_may) + [pivot] + ordenar_tabla_valor(mayor, key, men_may)


def ts_mostrar_tabla_ordenada(proyectos: list[dict]) -> (None):
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
    opciones = {
        '1': "Nombre del Proyecto",
        '2': "Presupuesto",
        '3': "Fecha de inicio", 
    }
    
    if proyectos:
        menu_ornenamiento()
        opcion = input("\nIngrese opcion: ")
        menu_menor_mayor()
        sentido = input("\nIngrese opcion: ")
        
        if validar_entero(opcion, 1, 4) and validar_entero(sentido, 1, 3):
            clave = opciones[opcion]
            if sentido == "1":
                proyectos_ordenados = ordenar_tabla_valor(proyectos, clave)
            else:
                proyectos_ordenados = ordenar_tabla_valor(proyectos, clave, False)
            
            ts_mostrar_proyectos(proyectos_ordenados)
        
        
        elif opcion == '4' or sentido == '3':
            print("\nSe cancela ordenamiento.")
        
        else:
            print("\nEleccion incorrecta se cancela ordenamiento.")
    else:
        print("\nLista de proyectos vacia.")
# 9. Retomar proyecto: Vuelve a dar de alta un proyecto Cancelado, comprobando anteriormente
#    que cumpla todos los requisitos para esto.
def ts_retomar_proyecto(proyectos: list[dict]) -> (None):
    """
    Retoma proyecto que anteriormente habia sido Cancelado dendole un estado de Activo. 
    Args:
        proyectos (list[dict]): Lista de proyectos a modificar.
    """
    if proyectos:
        cancelados = mostrar_clave_valor(proyectos, 'Estado', 'Cancelado')
        ts_mostrar_proyectos(cancelados)
        retomar = input("\nIngrese nombre de proyecto que desea retomar: ")
        if validar_caracteres(retomar, 30):
            retomar_ok = normalizar_frase(retomar)
            indice = bucar_indice(proyectos, 'Nombre del Proyecto', retomar_ok)
            if indice != -1:
                print("Ingrese fechas de inicio y fin.")
                fecha_1= ingreso_fecha()
                fecha_2= ingreso_fecha()
                if validador_fechas(fecha_1, fecha_2):
                    proyecto = proyectos[indice]
                    proyecto['Estado'] = 'Activo'
                    proyecto['Fecha de inicio'] = fecha_1
                    proyecto['Fecha de Fin'] = fecha_2
                print("\nSe retoma proyecto con exito.")
            else:
                print("\nNo se encuestra proyecto.")
        else:
            print(f"\nEl nombre {retomar} no se encuentra en lista de proyectos.")
    else:
        print("\nLista de proyectos vacia.")
# 10. Mostrar todos los proyectos terminados en medio de la cuarentena del COVID 19 (Marzo de 2020
#     hasta el fin del 2021 por ejemplo). En caso de que no haya indicar error
def ts_proyectos_finalizados_covid(proyectos: list[dict]) -> (None):
    """
    Filtra y muestra proyectos finalizados durante la cuarentena del COVID-19.
    Args:
        proyectos (list[dict]): Lista de diccionarios con los datos de los proyectos.
    """
    lista_aux = []
    if proyectos:
        for proyecto in proyectos:
            if rango_fechas((2020, 3, 1), (2021, 12, 31), proyecto['Fecha de Fin']):
                lista_aux.append(proyecto)
        if len(lista_aux) < 1:
            print("\nNo hay proyecto para mostrar.")
        else:
            lista_fin = mostrar_clave_valor(lista_aux, 'Estado', 'Finalizado')
            print("\n\nPROYECTOS FINALIZADOS DURANTE EL COVID-19.")
            ts_mostrar_proyectos(lista_fin)
        
    else:
        print("\nLista de proyectos vacia.")
# 11. Realizar un top 3 de los proyectos activos con mayor presupuesto que hayan sido iniciados en la
#     década de los 10’ (1 de Enero de 2010 hasta 31 de Diciembre de 2019). Verificar qué haya la cantidad
#     deseada de proyectos , sino indicar un mensaje de error.
def ts_top3_proyectos_activos_mejor_presupuesto(proyectos: list[dict]) -> (None):
    """
    Filtra y muestra un top 3 de proyectos con mayor presupuesto que hayan sido inicioados
    durante la decada de 2010-2020.
    Args:
        proyectos (list[dict]): Lista de diccionarios con los datos de los proyectos.
    """
    lista_aux = []
    if proyectos:
        for proyecto in proyectos:
            if rango_fechas((2010, 1, 1), (2019, 12, 31), proyecto['Fecha de inicio']):
                lista_aux.append(proyecto)
        if len(lista_aux) < 3:
            print("\nHay menos de 3 proyectos para mostrar el top 3.")
        else:
            lista_ordenada = ordenar_tabla_valor(lista_aux, 'Presupuesto', False)
            print("\n\nMEJORES PRESUPUESTOS 2da DECADA DEL 2000.")
            ts_mostrar_proyectos(lista_ordenada[:3])
    else:
        print("\nLista de proyectos vacia.")
# 12. Salir: Terminará la ejecución del programa.
# ¡¡¡Hecho!!!





