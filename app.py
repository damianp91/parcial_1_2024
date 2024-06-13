









from ts_biblioteca import(
    limpiar_consola, ts_menu_principal, ts_ingreso_datos_proyecto
)

def ts_gestion_proyectos_app() -> (None):
    
    while True:
        
        eleccion = ts_menu_principal()
        lista = []
        match eleccion:
            case 1:
                ts_ingreso_datos_proyecto(lista)
                print(lista)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                print("¡¡¡Gracias por usar nuestra app!!!")
                break
            case _:
                print(f'Opción inválida, el numero {eleccion} no esta en el rago de 1 - 10')
        limpiar_consola()
