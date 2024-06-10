## parcial_1_2024


# Enunciado:

La empresa "TechSolutions" nos ha solicitado desarrollar un software de gestión de proyectos para
llevar a cabo un control exhaustivo de los mismos.<br>
Datos correspondientes a cada proyecto:<br>
    ● ID<br>
    ● Nombre del Proyecto<br>
    ● Descripción<br>
    ● Fecha de Inicio<br>
    ● Fecha de Fin<br>
    ● Presupuesto<br>
    ● Estado<br>


# Consideraciones:

● El programa deberá gestionar una lista de hasta 50 proyectos activos. Cada proyecto será
  representado mediante un diccionario.<br>
● Si se alcanza el límite de 50 proyectos activos, se deberá notificar al usuario.<br>
● Solo se podrá ingresar un proyecto en caso de que se finalice o cancele uno existente.<br>
● Al ingresar un proyecto, el ID debe ser autoincremental, comenzando en 1. Cada proyecto
  tendrá un ID único.<br>
● El resto de los datos deberán ser ingresados por consola.<br>


# Validaciones:

● Nombre del Proyecto: Debe contener solo caracteres alfabéticos y no exceder los 30
  caracteres. No pueden contener números ni caracteres especiales.<br>
● Descripción: Debe ser un texto alfanumérico de no más de 200 caracteres.<br>
● Presupuesto: Debe ser un valor numérico entero no menor a $500000.<br>
● Fecha de Inicio y Fecha de Fin: Deben ser fechas válidas en el formato "DD/MM/AAAA".<br>
● La Fecha de Fin no puede ser anterior a la Fecha de Inicio.<br>
● El estado debe de iniciar como ‘Activo’, pudiendo ser también ‘Cancelado’ o ‘Finalizado’<br>


# Opciones del menú:

1. Ingresar proyecto: Pedirá los datos necesarios y dará de alta a un nuevo proyecto, asignando
   un ID autoincremental.<br>
2. Modificar proyecto: Permitirá alterar cualquier dato del proyecto excepto su ID. Se usará el ID
   para identificar al proyecto a modificar. Se mostrará un submenú para seleccionar qué datos
   modificar. Se indicará si se realizaron modificaciones o no.<br>
3. Cancelar proyecto: Cancelará un proyecto de la lista original. Se pedirá el ID del proyecto a
   cancelar.<br>
4. Comprobar proyectos: Cambiará el estado de todos los proyectos cuya fecha de finalización
   ya haya sucedido.<br>
5. Mostrar todos: Imprimirá por consola la información de todos los proyectos en formato de
   tabla:<br>
        | Nombre del Proyecto | Descripción      | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado    |<br>
        | Innovación AI       | Desarrollo de IA | $1,000,000  | 01/01/2024      | 01/01/2025   | Activo    |<br>
        | Rediseño Web        | Nueva página web | $300,000    | 15/02/2024      | 30/06/2024   | Cancelado |<br>
6. Calcular presupuesto promedio: Calculará e imprimirá el presupuesto promedio de todos los
   proyectos.<br>
7. Buscar proyecto por nombre: Permitirá al usuario buscar y mostrar la información de un
   proyecto específico ingresando su nombre.<br>
8. Ordenar proyectos: Ofrecerá la opción de <br>denar y mostrar la lista de proyectos por nombre,
   presupuesto, o fecha de inicio de forma ascendente o descendente.<br>
9. Retomar proyecto: Vuelve a dar de alta un proyecto Cancelado, comprobando anteriormente
   que cumpla todos los requisitos para esto.<br>
10. Salir: Terminará la ejecución del programa.<br>


# Requisitos adicionales:

● El programa deberá estar correctamente modularizado, haciendo uso de módulos, paquetes y
  funciones propias para solicitar enteros, flotantes y cadenas, así como para las validaciones
  de cada uno de estos tipos de datos.<br>
● El código debe estar programado de manera eficiente y siguiendo buenas prácticas de la
  programación y las reglas de estilo de la cátedra.<br>


# Archivos

1. Al iniciar el programa, se deberá leer el archivo Proyectos.csv para tener la lista de proyectos
   actualizada.<br>
2. Al finalizar el programa (puede ser en la opción salir) se deberá actualizar el archivo
   Proyectos.csv, con los datos de los proyectos.<br>
3. Los proyectos que hayan sido terminados deberán guardarse en un archivo Json, llamado
   “ProyectosFinalizados.json”.<br>


# Condiciones de aprobación:
● Correcto uso de funciones, siendo estas modularizadas y documentadas de manera
  óptima.<br>
● Correcta utilización de variables, tipos de datos y estructuras de control.<br>
● Uso correcto de bibliotecas y módulos.<br>
● Gestión óptima de archivos y codificación CSV y JSON.<br>
● Clara interfaz de usuario, haciendo que el programa sea intuitivo y fácil de usar.
● Correcta validación de los datos ingresados.<br>
● Seguridad de código, para que no se de la posibilidad de que haya alguna excepción
  durante la ejecución del mismo.<br>
