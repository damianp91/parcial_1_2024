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


def menu_principal() -> (None):
    """
    Imprime por consola el menu del sistema principal
    Args:
        None.
    Returns:
        str: Devuelve uan cadena de caracteres
    """
    menu = \
    """
    =============================================
                GESTION DE PROYECTOS
    =============================================
    01. Ingresar proyecto.
    02. Modificar proyecto.
    03. Cancelar proyecto.
    04. Comprobar proyectos.
    05. Mostrar todos.
    06. Calcular presupuesto promedio.
    07. Buscar proyecto por nombre.
    08. Ordenar proyectos por nombre.
    09. Retomar proyecto.
    10. Informe proyectos finalizados 
        durante el COVI-19.
    11. Informe top 3 proyectos con mayor
        presupuesto durante 2010-2020.
    12. Salir.
    =============================================
    """
    print(menu)


def menu_modificar() -> (None):
    """
    Imprime en consola el submenu del sistema para modificar
    elementos en los campos indicados
    Args:
        None.
    Returns:
        str: Devuelve una cadena de caracteres
    """
    sub_menu = \
    """
    ==================================
            MODIFICACION DATOS 
    ==================================
    01. Nombre proyecto.
    02. Descripcion proyecto.
    03. Presupuesto proyecto.
    04. Fecha inicio proyecto.
    05. Fecha fin proyecto.
    06. Estado proyecto.
    07. Salir.
    ==================================
    """
    print(sub_menu)


def menu_ornenamiento() -> (None):
    """
    Imprime en consola el submenu del sistema para ordenar
    elementos en los campos indicados
    Args:
        None.
    Returns:
        str: Devuelve una cadena de caracteres
    """
    sub_menu = \
    """
    ==================================
            ORDENAMIENTO DATOS
    ==================================
    01. Nombre proyecto.
    02. Presupuesto.
    03. Fecha inicio. 
    04. Salir.
    ==================================
    """
    print(sub_menu)


def menu_menor_mayor() -> (None):
    """
    Imprime en consola el submenu del sistema para indicar
    el sentido elementos en los campos indicados
    Args:
        None.
    Returns:
        str: Devuelve una cadena de caracteres
    """
    sub_menu = \
    """
    ==================================
            SENTIDO ORDENAMIENTO
    ==================================
    01. Mayor a Menor.
    02. Menor a Mayor.
    03. Salir.
    ==================================
    """
    print(sub_menu)