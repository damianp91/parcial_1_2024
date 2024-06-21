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



from ts_biblioteca import(
    ts_menu_principal, ts_ingreso_datos_proyecto, ts_mostrar_proyectos,
    ts_mostrar_proyectos, ts_modificar_proyecto, ts_mostrar_tabla_ordenada
)

from ts_validaciones import(
    limpiar_consola
)

def ts_gestion_proyectos_app(lista_proyectos: list[dict]) -> (None):
    """
    Funcion encargada de llamar las funciones principales para el fincionamiento
    del ABM
    Args:
        lista_proyectos (list[dict]): Lista de diccionarios a manipular
    """
    
    while True:
        
        ts_mostrar_proyectos(lista_proyectos)
        eleccion = ts_menu_principal()
        
        match eleccion:
            case 1:
                ts_ingreso_datos_proyecto(lista_proyectos)
            case 2:
                ts_modificar_proyecto(lista_proyectos)
            case 3:
                pass
            case 4:
                pass
            case 5:
                ts_mostrar_proyectos(lista_proyectos)
            case 6:
                pass
            case 7:
                pass
            case 8:
                ts_mostrar_tabla_ordenada(lista_proyectos)
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                print("¡¡¡Gracias por usar nuestra app!!!")
                break
            case _:
                print(f'Opción inválida, el numero {eleccion} no esta en el rago de 1 - 12')
        limpiar_consola()
