
# 1. Ingresar proyecto: Pedirá los datos necesarios y dará de alta a un nuevo proyecto, asignando
#     un ID autoincremental.
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


import os

def limpiar_consola():
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: os.system('cls')    









