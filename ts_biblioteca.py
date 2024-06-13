



import os
from datetime import datetime


def limpiar_consola():
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: 
        os.system('cls')   


def imprimir_menu() ->(str):
    """
    Imprime en consola el menu del sistema
    Args:
        None.
    Returns:
        str: Devuelve uan cadena de caracteres
    """
    menu = \
    """
    01. Ingresar proyecto.
    02. Modificar proyecto.
    03. Cancelar proyecto.
    04. Comprobar proyectos.
    05. Mostrar todos.
    06. Calcular presupuesto promedio.
    07. Buscar proyecto por nombre.
    08. Ordenar proyectos por nombre.
    09. Retomar proyecto.
    10. Salir.
    """
    print(menu)


def validar_entero(numero_str: str, minimo: int, maximo: int) -> (bool):
    """
    Recibe un numero parceado a string para validar si es un entero
    ademas de indicar el valor minimo a validar que se pasa por parametro
    Args:
        numero_str (str): Caracter o caracteres que se desean validar
        minimo (int): Cantidad minima para validar
        maximo (int): Cantidad maxima para validar
    Returns:
        bool: Devuelve si es falso o verdadero el numero
    """
    validador_ok = False
    
    if len(numero_str) >= minimo and len(numero_str) <= maximo:
        validador_ok = numero_str.isdigit()
    
    return validador_ok


def ts_menu_principal() -> (int):
    """
    Muestra en cosola menu principal y valida si la opcion ingresada sea correcta
    Returns:
        (int): devuelve -1 si no es un valor numerico o el valor ingresado
    """
    valor = -1
    imprimir_menu()
    opcion = input("Ingrese la opcion (1-10): ")
    if validar_entero(opcion, 1, 2):
        valor = int(opcion)
    return valor


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
    
    if validar_entero(dia, 1, 2) and validar_entero(mes, 1, 2)\
        and validar_entero(anio, 4, 4):
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
    opcion = input("Presione enter para continuar o Ingrese 2 para 'Cancelado' o 3 para 'Filanizado' si desea cambiar el estado: ")
    
    if validar_entero(opcion, 1, 1) and (int(opcion) == 2 or int(opcion) == 3):
        estado_ok = estado[opcion]
        print(f"Estado se cambio correctamente a: {estado_ok}")
    else:
        print(f"Se asigna estado: {estado_ok}")
    
    return estado_ok


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
    if validar_entero(presupuesto, 6, 10) and int(presupuesto) >= 500000:
        aux_list.append(int(presupuesto))
        print("Presupuesto Ingresado correctamente")
    else:
        print("No se pudo ingresar correctamente presupuesto. Verifique el monto")
    
    # Estado
    aux_list.append(estado_proyecto())
    
    return aux_list


def ts_ingreso_datos_proyecto(proyectos: list) -> (None):
    """
    Se encarga de asignar un id de manera autoincremental a cada proyecto ademas de
    agregar diccionarios a la lista ingresada por parametro en la funcion
    Args:
        proyectos (list): Lista con diccionaros o vacia
    """
    if len(proyectos) <= 50:
        id = len(proyectos) + 1
        
        try:
            datos = ingreso_datos()
            proyecto_dict = {"id":id, "nombre de proyecto":datos[0], "descripcion":datos[1], "fecha inicio":datos[2], "fecha fin":datos[3],\
                "presupuesto":datos[4], "estado":datos[5]}

            proyectos.append(proyecto_dict)
        
        except IndexError:
            print("No se ingreso datos de proyecto, si desea ingresar un proyecto por favor intente de nuevo siguiendo el formato requerido.")

# 2. Modificar proyecto: Permitirá alterar cualquier dato del proyecto excepto su ID. Se usará el ID
#     para identificar al proyecto a modificar. Se mostrará un submenú para seleccionar qué datos
#     modificar. Se indicará si se realizaron modificaciones o no.

# 3. Cancelar proyecto: Cancelará un proyecto de la lista original. Se pedirá el ID del proyecto a
#     cancelar.
# 4. Comprobar proyectos: Cambiará el estado de todos los proyectos cuya fecha de finalización
#     ya haya sucedido.
# 5. Mostrar todos: Imprimirá por consola la información de todos los proyectos en formato de
#     tabla:
#         | Nombre del Proyecto | Descripción      | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado    |
#         | Innovación AI       | Desarrollo de IA | $1,000,000  | 01/01/2024      | 01/01/2025   | Activo    |
#         | Rediseño Web        | Nueva página web | $300,000    | 15/02/2024      | 30/06/2024   | Cancelado |
# 6. Calcular presupuesto promedio: Calculará e imprimirá el presupuesto promedio de todos los
#     proyectos.
# 7. Buscar proyecto por nombre: Permitirá al usuario buscar y mostrar la información de un
#     proyecto específico ingresando su nombre.
# 8. Ordenar proyectos: Ofrecerá la opción de ordenar y mostrar la lista de proyectos por nombre,
#     presupuesto, o fecha de inicio de forma ascendente o descendente.
# 9. Retomar proyecto: Vuelve a dar de alta un proyecto Cancelado, comprobando anteriormente
#     que cumpla todos los requisitos para esto.
# 10. Salir: Terminará la ejecución del programa.






