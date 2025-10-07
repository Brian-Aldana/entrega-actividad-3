# -*- coding: utf-8 -*-
import sys # Se usa para sys.exit() para una salida limpia del programa

# =============================================
# 1. ESTRUCTURA DE DATOS PRINCIPAL (Listas Paralelas)
# =============================================
# Se inicializan las listas que contendrán toda la información de los estudiantes.
nombres = []
codigos = []
promedios = []
materias_aprobadas = []
semestres = []
carreras = []

# Variable global para verificar si los datos están ordenados por código para la búsqueda binaria.
# Se invalida si se añaden nuevos estudiantes o se ordena por otro criterio.
datos_ordenados_por_codigo = False

# =============================================
# FUNCIONES AUXILIARES (Helpers)
# =============================================

def limpiar_pantalla():
    """Función simple para limpiar la consola y mejorar la legibilidad."""
    # Esta función no es esencial para la lógica, pero mejora la experiencia de usuario.
    # import os
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 20)


def mostrar_tabla_estudiantes(indices=None):
    """
    Imprime una tabla formateada con los datos de los estudiantes.
    Si se proporciona una lista de 'indices', solo muestra esos estudiantes.
    De lo contrario, muestra todos los estudiantes.
    """
    if not nombres:
        print(">> No hay estudiantes registrados en el sistema.")
        return

    # Si no se especifica, se muestran todos los estudiantes
    if indices is None:
        indices = range(len(nombres))

    if not indices:
        print(">> No se encontraron estudiantes que coincidan con el criterio.")
        return

    # Encabezados de la tabla
    print("-" * 110)
    print(f"{'Código':<12} | {'Nombre Completo':<30} | {'Carrera':<25} | {'Semestre':<10} | {'Promedio':<10} | {'Materias Apr.':<15}")
    print("-" * 110)

    # Filas con los datos de cada estudiante
    for i in indices:
        print(f"{codigos[i]:<12} | {nombres[i]:<30} | {carreras[i]:<25} | {semestres[i]:<10} | {promedios[i]:<10.2f} | {materias_aprobadas[i]:<15}")
    print("-" * 110)


def intercambiar_datos(i, j):
    """
    Intercambia la posición de los datos de dos estudiantes (en los índices i y j)
    en todas las listas paralelas para mantener la consistencia.
    """
    nombres[i], nombres[j] = nombres[j], nombres[i]
    codigos[i], codigos[j] = codigos[j], codigos[i]
    promedios[i], promedios[j] = promedios[j], promedios[i]
    materias_aprobadas[i], materias_aprobadas[j] = materias_aprobadas[j], materias_aprobadas[i]
    semestres[i], semestres[j] = semestres[j], semestres[i]
    carreras[i], carreras[j] = carreras[j], carreras[i]

# =============================================
# 2. FUNCIONALIDAD DE ENTRADA Y VALIDACIÓN
# =============================================

def registrar_nuevos_estudiantes():
    """
    Solicita y valida los datos para registrar un número determinado de nuevos estudiantes.
    """
    global datos_ordenados_por_codigo
    
    # Validar cantidad de estudiantes
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de estudiantes a registrar (entre 10 y 50): "))
            if 10 <= cantidad <= 50:
                break
            else:
                print("Error: La cantidad debe estar entre 10 y 50.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

    print("\n--- Inicio de Registro ---")
    for i in range(cantidad):
        print(f"\n--- Registrando Estudiante #{i + 1} de {cantidad} ---")

        # Validar Código (debe ser único)
        while True:
            try:
                codigo = int(input(f"Código del estudiante: "))
                if codigo not in codigos:
                    break
                else:
                    print("Error: El código ya existe. Ingrese un código único.")
            except ValueError:
                print("Error: El código debe ser un número entero.")

        # Solicitar Nombre
        nombre = input("Nombre completo: ").strip().title()

        # Validar Promedio (0.0 a 5.0)
        while True:
            try:
                promedio = float(input("Promedio (0.0 - 5.0): "))
                if 0.0 <= promedio <= 5.0:
                    break
                else:
                    print("Error: El promedio debe estar en el rango de 0.0 a 5.0.")
            except ValueError:
                print("Error: Ingrese un número decimal válido para el promedio.")

        # Validar Semestre (1 a 10)
        while True:
            try:
                semestre = int(input("Semestre (1 - 10): "))
                if 1 <= semestre <= 10:
                    break
                else:
                    print("Error: El semestre debe estar en el rango de 1 a 10.")
            except ValueError:
                print("Error: Ingrese un número entero válido para el semestre.")

        # Validar Materias Aprobadas (no puede exceder semestre * 6)
        while True:
            try:
                materias = int(input(f"Materias aprobadas (máximo {semestre * 6}): "))
                if 0 <= materias <= semestre * 6:
                    break
                else:
                    print(f"Error: El número de materias aprobadas no puede ser negativo ni exceder {semestre * 6}.")
            except ValueError:
                print("Error: Ingrese un número entero válido.")

        # Solicitar Carrera
        carrera = input("Carrera: ").strip().title()

        # Agregar datos a las listas paralelas
        nombres.append(nombre)
        codigos.append(codigo)
        promedios.append(promedio)
        semestres.append(semestre)
        materias_aprobadas.append(materias)
        carreras.append(carrera)
        
        # Al agregar nuevos estudiantes, el ordenamiento por código se pierde.
        datos_ordenados_por_codigo = False
        print(f"¡Estudiante '{nombre}' registrado con éxito!")
        
    print("\n--- Registro Finalizado ---")

# =============================================
# 3. ALGORITMOS DE ORDENAMIENTO (Desde Cero)
# =============================================

# --- Algoritmo Básico: Ordenamiento por Inserción ---
def ordenamiento_insercion(criterio):
    """
    Ordena los datos de los estudiantes usando el algoritmo de Insertion Sort.
    Modifica todas las listas paralelas para mantener la consistencia de los datos.
    
    Args:
        criterio (str): 'nombre', 'promedio', 'codigo' o 'semestre'.
    """
    global datos_ordenados_por_codigo
    n = len(nombres)
    
    # Se itera desde el segundo elemento (índice 1) hasta el final de la lista.
    for i in range(1, n):
        # Se guardan los valores del elemento actual (en la posición 'i') que vamos a insertar.
        # Es como tomar una carta de la baraja para colocarla en su lugar correcto.
        key_nombre = nombres[i]
        key_codigo = codigos[i]
        key_promedio = promedios[i]
        key_materias = materias_aprobadas[i]
        key_semestre = semestres[i]
        key_carrera = carreras[i]
        
        j = i - 1
        
        # Se determina la condición de comparación según el criterio.
        # Mientras el elemento en 'j' sea "mayor" que nuestra 'key' (según el criterio),
        # se desplazan los elementos de la sección ordenada hacia la derecha.
        condicion = False
        if criterio == 'nombre':
            condicion = j >= 0 and nombres[j] > key_nombre # A-Z
        elif criterio == 'promedio':
            condicion = j >= 0 and promedios[j] < key_promedio # Mayor a menor
        elif criterio == 'codigo':
            condicion = j >= 0 and codigos[j] > key_codigo # Ascendente
        elif criterio == 'semestre':
            condicion = j >= 0 and semestres[j] < key_semestre # Descendente

        while condicion:
            # Desplazamiento en todas las listas
            nombres[j + 1] = nombres[j]
            codigos[j + 1] = codigos[j]
            promedios[j + 1] = promedios[j]
            materias_aprobadas[j + 1] = materias_aprobadas[j]
            semestres[j + 1] = semestres[j]
            carreras[j + 1] = carreras[j]
            j -= 1
            
            # Re-evaluar la condición para el siguiente elemento a la izquierda
            if criterio == 'nombre':
                condicion = j >= 0 and nombres[j] > key_nombre
            elif criterio == 'promedio':
                condicion = j >= 0 and promedios[j] < key_promedio
            elif criterio == 'codigo':
                condicion = j >= 0 and codigos[j] > key_codigo
            elif criterio == 'semestre':
                condicion = j >= 0 and semestres[j] < key_semestre
        
        # Se inserta la 'key' (la carta que tomamos) en la posición correcta.
        nombres[j + 1] = key_nombre
        codigos[j + 1] = key_codigo
        promedios[j + 1] = key_promedio
        materias_aprobadas[j + 1] = key_materias
        semestres[j + 1] = key_semestre
        carreras[j + 1] = key_carrera

    # Actualizar el estado de ordenamiento
    datos_ordenados_por_codigo = (criterio == 'codigo')
    print(f"\n>> Datos ordenados por '{criterio}' usando Inserción.")


# --- Algoritmo Eficiente: Quicksort ---
def particion(criterio, bajo, alto):
    """
    Función de partición para Quicksort. Toma un pivote (el último elemento)
    y coloca los elementos "menores" a su izquierda y los "mayores" a su derecha.
    """
    # Se selecciona el último elemento como pivote.
    pivote = None
    if criterio == 'nombre': pivote = nombres[alto]
    elif criterio == 'promedio': pivote = promedios[alto]
    elif criterio == 'codigo': pivote = codigos[alto]
    elif criterio == 'semestre': pivote = semestres[alto]
    
    i = bajo - 1  # Índice del elemento más pequeño

    for j in range(bajo, alto):
        # Se compara el elemento actual 'j' con el pivote.
        # Si es "menor" (según el criterio), se intercambia con el elemento en 'i'.
        condicion = False
        if criterio == 'nombre':
            condicion = nombres[j] <= pivote # A-Z
        elif criterio == 'promedio':
            condicion = promedios[j] >= pivote # Mayor a menor
        elif criterio == 'codigo':
            condicion = codigos[j] <= pivote # Ascendente
        elif criterio == 'semestre':
            condicion = semestres[j] >= pivote # Descendente

        if condicion:
            i += 1
            intercambiar_datos(i, j)

    # Finalmente, se coloca el pivote en su posición correcta.
    intercambiar_datos(i + 1, alto)
    return i + 1


def quicksort_recursivo(criterio, bajo, alto):
    """Función recursiva principal de Quicksort."""
    if bajo < alto:
        # pi es el índice de la partición, donde el pivote ya está en su lugar.
        pi = particion(criterio, bajo, alto)

        # Se ordenan recursivamente los elementos antes y después de la partición.
        quicksort_recursivo(criterio, bajo, pi - 1)
        quicksort_recursivo(criterio, pi + 1, alto)


def quicksort(criterio):
    """
    Función 'wrapper' o envoltorio para iniciar el algoritmo Quicksort.
    """
    global datos_ordenados_por_codigo
    if not nombres:
        print(">> No hay estudiantes para ordenar.")
        return
        
    quicksort_recursivo(criterio, 0, len(nombres) - 1)
    
    # Actualizar el estado de ordenamiento
    datos_ordenados_por_codigo = (criterio == 'codigo')
    print(f"\n>> Datos ordenados por '{criterio}' usando Quicksort.")

# ==================================================
# 4. ALGORITMOS DE BÚSQUEDA Y FILTRADO
# ==================================================

def busqueda_binaria_por_codigo():
    """
    Busca un estudiante por su código usando Búsqueda Binaria.
    Requiere que la lista de códigos esté ordenada ascendentemente.
    """
    if not datos_ordenados_por_codigo:
        print("\nError: Para usar la búsqueda binaria, primero debe ordenar los datos por 'código'.")
        print("Vaya al menú de ordenamiento (opción 3 o 4) y elija 'código'.")
        return

    try:
        codigo_buscar = int(input("Ingrese el código del estudiante a buscar: "))
    except ValueError:
        print("Error: El código debe ser un número entero.")
        return
        
    bajo, alto = 0, len(codigos) - 1
    indice_encontrado = -1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if codigos[medio] == codigo_buscar:
            indice_encontrado = medio
            break
        elif codigos[medio] < codigo_buscar:
            bajo = medio + 1
        else:
            alto = medio - 1
            
    if indice_encontrado != -1:
        print(f"\n--- Estudiante Encontrado (Código: {codigo_buscar}) ---")
        mostrar_tabla_estudiantes([indice_encontrado])
    else:
        print(f"\n>> No se encontró ningún estudiante con el código {codigo_buscar}.")


def busqueda_lineal_por_nombre():
    """
    Busca estudiantes cuyo nombre contenga el texto de búsqueda (búsqueda parcial).
    """
    if not nombres:
        print(">> No hay estudiantes registrados para buscar.")
        return
    
    nombre_parcial = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().lower()
    if not nombre_parcial:
        print("Error: El término de búsqueda no puede estar vacío.")
        return

    indices_encontrados = []
    for i in range(len(nombres)):
        if nombre_parcial in nombres[i].lower():
            indices_encontrados.append(i)
    
    print(f"\n--- Resultados de la Búsqueda para '{nombre_parcial}' ---")
    mostrar_tabla_estudiantes(indices_encontrados)


def filtrar_por_rango_promedio():
    """
    Muestra los estudiantes cuyo promedio se encuentre en un rango [min, max].
    """
    if not nombres:
        print(">> No hay estudiantes registrados para filtrar.")
        return
        
    try:
        min_prom = float(input("Ingrese el promedio mínimo del rango (ej: 3.5): "))
        max_prom = float(input("Ingrese el promedio máximo del rango (ej: 4.5): "))
        if min_prom > max_prom:
            print("Error: El promedio mínimo no puede ser mayor que el máximo.")
            return
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para los promedios.")
        return

    indices_filtrados = []
    for i in range(len(promedios)):
        if min_prom <= promedios[i] <= max_prom:
            indices_filtrados.append(i)
            
    print(f"\n--- Estudiantes con Promedio entre {min_prom:.2f} y {max_prom:.2f} ---")
    mostrar_tabla_estudiantes(indices_filtrados)


def filtrar_por_carrera():
    """
    Muestra todos los estudiantes que pertenecen a una carrera específica.
    """
    if not nombres:
        print(">> No hay estudiantes registrados para filtrar.")
        return
        
    carrera_buscar = input("Ingrese el nombre de la carrera a filtrar: ").strip().lower()
    if not carrera_buscar:
        print("Error: El nombre de la carrera no puede estar vacío.")
        return

    indices_filtrados = []
    for i in range(len(carreras)):
        if carreras[i].lower() == carrera_buscar:
            indices_filtrados.append(i)

    print(f"\n--- Estudiantes de la Carrera: '{carrera_buscar.title()}' ---")
    mostrar_tabla_estudiantes(indices_filtrados)

# =============================================
# 5. ESTADÍSTICAS Y REPORTES
# =============================================

def mostrar_estadisticas_generales():
    """
    Calcula y muestra un resumen de estadísticas sobre todos los estudiantes.
    """
    if not nombres:
        print(">> No hay estudiantes registrados para generar estadísticas.")
        return
        
    n = len(nombres)
    
    # 1. Promedio general
    promedio_total = sum(promedios) / n
    
    # 2. Estudiante con promedio más alto y más bajo
    idx_max_prom, idx_min_prom = 0, 0
    for i in range(1, n):
        if promedios[i] > promedios[idx_max_prom]:
            idx_max_prom = i
        if promedios[i] < promedios[idx_min_prom]:
            idx_min_prom = i
            
    nombre_max = nombres[idx_max_prom]
    promedio_max = promedios[idx_max_prom]
    nombre_min = nombres[idx_min_prom]
    promedio_min = promedios[idx_min_prom]
    
    # 3. Distribución de estudiantes por carrera
    # Implementación sin diccionarios
    carreras_unicas = []
    conteo_carreras = []
    for carrera in carreras:
        if carrera not in carreras_unicas:
            carreras_unicas.append(carrera)
            conteo_carreras.append(1)
        else:
            idx = carreras_unicas.index(carrera)
            conteo_carreras[idx] += 1
            
    print("\n" + "="*40)
    print("      ESTADÍSTICAS GENERALES")
    print("="*40)
    print(f"Total de Estudiantes Registrados: {n}")
    print(f"Promedio General de la Institución: {promedio_total:.2f}")
    print("\n--- Rendimiento Académico ---")
    print(f"Mejor Promedio: {nombre_max} ({promedio_max:.2f})")
    print(f"Menor Promedio: {nombre_min} ({promedio_min:.2f})")
    print("\n--- Distribución por Carrera ---")
    for i in range(len(carreras_unicas)):
        print(f"- {carreras_unicas[i]}: {conteo_carreras[i]} estudiante(s)")
    print("="*40)


def mostrar_top_5_mejores_promedios():
    """
    Muestra los 5 estudiantes con los promedios más altos.
    """
    if not nombres:
        print(">> No hay estudiantes registrados.")
        return
    
    # Para no alterar el orden original, creamos copias temporales de las listas
    # y las ordenamos por promedio de mayor a menor.
    temp_nombres = list(nombres)
    temp_codigos = list(codigos)
    temp_promedios = list(promedios)
    temp_materias = list(materias_aprobadas)
    temp_semestres = list(semestres)
    temp_carreras = list(carreras)

    # Ordenamos las listas temporales usando Quicksort por promedio
    # (adaptación para listas temporales)
    def quicksort_temporal(arr_prom, bajo, alto):
        if bajo < alto:
            pi = particion_temporal(arr_prom, bajo, alto)
            quicksort_temporal(arr_prom, bajo, pi - 1)
            quicksort_temporal(arr_prom, pi + 1, alto)

    def particion_temporal(arr_prom, bajo, alto):
        pivote = arr_prom[alto]
        i = bajo - 1
        for j in range(bajo, alto):
            if arr_prom[j] >= pivote: # Orden descendente
                i += 1
                # Intercambio en todas las listas temporales
                temp_nombres[i], temp_nombres[j] = temp_nombres[j], temp_nombres[i]
                temp_codigos[i], temp_codigos[j] = temp_codigos[j], temp_codigos[i]
                temp_promedios[i], temp_promedios[j] = temp_promedios[j], temp_promedios[i]
                temp_materias[i], temp_materias[j] = temp_materias[j], temp_materias[i]
                temp_semestres[i], temp_semestres[j] = temp_semestres[j], temp_semestres[i]
                temp_carreras[i], temp_carreras[j] = temp_carreras[j], temp_carreras[i]
        # Intercambio final para el pivote
        temp_nombres[i+1], temp_nombres[alto] = temp_nombres[alto], temp_nombres[i+1]
        temp_codigos[i+1], temp_codigos[alto] = temp_codigos[alto], temp_codigos[i+1]
        temp_promedios[i+1], temp_promedios[alto] = temp_promedios[alto], temp_promedios[i+1]
        temp_materias[i+1], temp_materias[alto] = temp_materias[alto], temp_materias[i+1]
        temp_semestres[i+1], temp_semestres[alto] = temp_semestres[alto], temp_semestres[i+1]
        temp_carreras[i+1], temp_carreras[alto] = temp_carreras[alto], temp_carreras[i+1]
        return i + 1

    quicksort_temporal(temp_promedios, 0, len(temp_promedios) - 1)

    print("\n--- Top 5 Mejores Promedios ---")
    # Mostramos los primeros 5 (o menos si no hay suficientes estudiantes)
    limite = min(5, len(temp_nombres))
    if limite == 0:
        print(">> No hay estudiantes para mostrar.")
        return
        
    # Encabezados
    print("-" * 80)
    print(f"{'#':<4} | {'Nombre Completo':<30} | {'Promedio':<10} | {'Carrera':<25}")
    print("-" * 80)
    # Filas
    for i in range(limite):
        print(f"{i+1:<4} | {temp_nombres[i]:<30} | {temp_promedios[i]:<10.2f} | {temp_carreras[i]:<25}")
    print("-" * 80)

# =============================================
# 6. MENÚ INTERACTIVO
# =============================================
def menu_ordenamiento(algoritmo):
    """Submenú para elegir el criterio de ordenamiento."""
    while True:
        print(f"\n--- Ordenar con {algoritmo.__name__.replace('_', ' ').title()} ---")
        print("Elija el criterio para ordenar:")
        print("1. Nombre (A-Z)")
        print("2. Promedio (Mayor a menor)")
        print("3. Código estudiantil (Ascendente)")
        print("4. Semestre (Descendente)")
        print("5. Volver al menú principal")
        
        opcion_ord = input("Seleccione una opción: ")
        
        criterio = None
        if opcion_ord == '1': criterio = 'nombre'
        elif opcion_ord == '2': criterio = 'promedio'
        elif opcion_ord == '3': criterio = 'codigo'
        elif opcion_ord == '4': criterio = 'semestre'
        elif opcion_ord == '5': break
        else:
            print("Opción no válida. Intente de nuevo.")
            continue
            
        if not nombres:
            print("\n>> No hay estudiantes para ordenar. Agregue estudiantes primero.")
            break
            
        algoritmo(criterio)
        mostrar_tabla_estudiantes()
        break # Volver al menú principal tras ordenar

def main():
    """
    Función principal que ejecuta el menú interactivo del sistema.
    """
    while True:
        print("\n" + "="*50)
        print("      SISTEMA INTEGRAL DE GESTIÓN ACADÉMICA")
        print("="*50)
        print("1. Agregar estudiantes")
        print("2. Mostrar todos los estudiantes")
        print("3. Ordenar por criterio (Algoritmo de Inserción)")
        print("4. Ordenar por criterio (Algoritmo Quicksort)")
        print("\n--- Búsqueda y Filtrado ---")
        print("5. Buscar estudiante por código (Búsqueda Binaria)")
        print("6. Buscar estudiantes por nombre (Búsqueda Lineal)")
        print("7. Filtrar estudiantes por rango de promedio")
        print("8. Filtrar por carrera")
        print("\n--- Reportes ---")
        print("9. Mostrar estadísticas generales")
        print("10. Mostrar Top 5 estudiantes por promedio")
        print("\n11. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_nuevos_estudiantes()
        elif opcion == '2':
            mostrar_tabla_estudiantes()
        elif opcion == '3':
            menu_ordenamiento(ordenamiento_insercion)
        elif opcion == '4':
            menu_ordenamiento(quicksort)
        elif opcion == '5':
            busqueda_binaria_por_codigo()
        elif opcion == '6':
            busqueda_lineal_por_nombre()
        elif opcion == '7':
            filtrar_por_rango_promedio()
        elif opcion == '8':
            filtrar_por_carrera()
        elif opcion == '9':
            mostrar_estadisticas_generales()
        elif opcion == '10':
            mostrar_top_5_mejores_promedios()
        elif opcion == '11':
            print("\nGracias por usar el Sistema de Gestión Académica. ¡Hasta pronto!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")
            
        input("\nPresione Enter para continuar...")
        # limpiar_pantalla() # Descomentar para una mejor experiencia en terminal

if __name__ == "__main__":
    main()