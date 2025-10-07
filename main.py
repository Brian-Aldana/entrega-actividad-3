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

# Lista de carreras disponibles (NUEVO REQUISITO)
CARRERAS_DISPONIBLES = [
    "Ingeniería de Software",
    "Administración de Empresas",
    "Ingeniería Ambiental",
    "Enfermería"
]

# Variable global para verificar si los datos están ordenados por código.
datos_ordenados_por_codigo = False

# =============================================
# FUNCIONES AUXILIARES (Helpers)
# =============================================

def limpiar_pantalla():
    """Función simple para limpiar la consola y mejorar la legibilidad."""
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
# 2. FUNCIONALIDAD DE ENTRADA Y VALIDACIÓN (CORREGIDA)
# =============================================

def registrar_nuevos_estudiantes():
    """
    Solicita y valida los datos para registrar un número determinado de nuevos estudiantes
    en una única carrera seleccionada al inicio.
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

    # --- INICIO DE LA CORRECCIÓN ---
    # Se pregunta por la carrera para todo el lote de estudiantes
    print("\nSeleccione la carrera para este grupo de estudiantes:")
    for idx, carrera_opcion in enumerate(CARRERAS_DISPONIBLES):
        print(f"{idx + 1}. {carrera_opcion}")
    
    carrera_seleccionada = ""
    while True:
        try:
            opcion_carrera = int(input(f"Elija una opción (1-{len(CARRERAS_DISPONIBLES)}): "))
            if 1 <= opcion_carrera <= len(CARRERAS_DISPONIBLES):
                carrera_seleccionada = CARRERAS_DISPONIBLES[opcion_carrera - 1]
                break
            else:
                print(f"Error: La opción debe estar entre 1 y {len(CARRERAS_DISPONIBLES)}.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
    # --- FIN DE LA CORRECCIÓN ---

    print(f"\n--- Inicio de Registro para la carrera de '{carrera_seleccionada}' ---")
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

        # Agregar datos a las listas paralelas
        nombres.append(nombre)
        codigos.append(codigo)
        promedios.append(promedio)
        semestres.append(semestre)
        materias_aprobadas.append(materias)
        carreras.append(carrera_seleccionada) # Se asigna la carrera elegida al inicio
        
        # Al agregar nuevos estudiantes, el ordenamiento por código se pierde.
        datos_ordenados_por_codigo = False
        print(f"¡Estudiante '{nombre}' registrado con éxito!")
        
    print("\n--- Registro Finalizado ---")

# =============================================
# 3. ALGORITMOS DE ORDENAMIENTO (Sin cambios)
# =============================================

def ordenamiento_insercion(criterio):
    global datos_ordenados_por_codigo
    n = len(nombres)
    for i in range(1, n):
        key_nombre = nombres[i]
        key_codigo = codigos[i]
        key_promedio = promedios[i]
        key_materias = materias_aprobadas[i]
        key_semestre = semestres[i]
        key_carrera = carreras[i]
        j = i - 1
        condicion = False
        if criterio == 'nombre': condicion = j >= 0 and nombres[j] > key_nombre
        elif criterio == 'promedio': condicion = j >= 0 and promedios[j] < key_promedio
        elif criterio == 'codigo': condicion = j >= 0 and codigos[j] > key_codigo
        elif criterio == 'semestre': condicion = j >= 0 and semestres[j] < key_semestre
        while condicion:
            intercambiar_datos(j + 1, j)
            j -= 1
            if criterio == 'nombre': condicion = j >= 0 and nombres[j] > key_nombre
            elif criterio == 'promedio': condicion = j >= 0 and promedios[j] < key_promedio
            elif criterio == 'codigo': condicion = j >= 0 and codigos[j] > key_codigo
            elif criterio == 'semestre': condicion = j >= 0 and semestres[j] < key_semestre
        nombres[j + 1], codigos[j + 1], promedios[j + 1], materias_aprobadas[j + 1], semestres[j + 1], carreras[j + 1] = key_nombre, key_codigo, key_promedio, key_materias, key_semestre, key_carrera
    datos_ordenados_por_codigo = (criterio == 'codigo')
    print(f"\n>> Datos ordenados por '{criterio}' usando Inserción.")

def particion(criterio, bajo, alto):
    pivote = None
    if criterio == 'nombre': pivote = nombres[alto]
    elif criterio == 'promedio': pivote = promedios[alto]
    elif criterio == 'codigo': pivote = codigos[alto]
    elif criterio == 'semestre': pivote = semestres[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        condicion = False
        if criterio == 'nombre': condicion = nombres[j] <= pivote
        elif criterio == 'promedio': condicion = promedios[j] >= pivote
        elif criterio == 'codigo': condicion = codigos[j] <= pivote
        elif criterio == 'semestre': condicion = semestres[j] >= pivote
        if condicion:
            i += 1
            intercambiar_datos(i, j)
    intercambiar_datos(i + 1, alto)
    return i + 1

def quicksort_recursivo(criterio, bajo, alto):
    if bajo < alto:
        pi = particion(criterio, bajo, alto)
        quicksort_recursivo(criterio, bajo, pi - 1)
        quicksort_recursivo(criterio, pi + 1, alto)

def quicksort(criterio):
    global datos_ordenados_por_codigo
    if not nombres:
        print(">> No hay estudiantes para ordenar.")
        return
    quicksort_recursivo(criterio, 0, len(nombres) - 1)
    datos_ordenados_por_codigo = (criterio == 'codigo')
    print(f"\n>> Datos ordenados por '{criterio}' usando Quicksort.")

# ==================================================
# 4. ALGORITMOS DE BÚSQUEDA Y FILTRADO (Sin cambios)
# ==================================================

def busqueda_binaria_por_codigo():
    if not datos_ordenados_por_codigo:
        print("\nError: Para usar la búsqueda binaria, primero debe ordenar los datos por 'código'.")
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
    if not nombres:
        print(">> No hay estudiantes registrados para buscar.")
        return
    nombre_parcial = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().lower()
    if not nombre_parcial:
        print("Error: El término de búsqueda no puede estar vacío.")
        return
    indices_encontrados = [i for i, nombre in enumerate(nombres) if nombre_parcial in nombre.lower()]
    print(f"\n--- Resultados de la Búsqueda para '{nombre_parcial}' ---")
    mostrar_tabla_estudiantes(indices_encontrados)

def filtrar_por_rango_promedio():
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
        print("Error: Ingrese valores numéricos válidos.")
        return
    indices_filtrados = [i for i, prom in enumerate(promedios) if min_prom <= prom <= max_prom]
    print(f"\n--- Estudiantes con Promedio entre {min_prom:.2f} y {max_prom:.2f} ---")
    mostrar_tabla_estudiantes(indices_filtrados)

def filtrar_por_carrera():
    if not nombres:
        print(">> No hay estudiantes registrados para filtrar.")
        return
    carrera_buscar = input("Ingrese el nombre de la carrera a filtrar: ").strip().lower()
    if not carrera_buscar:
        print("Error: El nombre de la carrera no puede estar vacío.")
        return
    indices_filtrados = [i for i, carrera in enumerate(carreras) if carrera.lower() == carrera_buscar]
    print(f"\n--- Estudiantes de la Carrera: '{carrera_buscar.title()}' ---")
    mostrar_tabla_estudiantes(indices_filtrados)

# =============================================
# 5. ESTADÍSTICAS Y REPORTES (Sin cambios)
# =============================================

def mostrar_estadisticas_generales():
    if not nombres:
        print(">> No hay estudiantes registrados para generar estadísticas.")
        return
    n = len(nombres)
    promedio_total = sum(promedios) / n
    idx_max_prom = promedios.index(max(promedios))
    idx_min_prom = promedios.index(min(promedios))
    carreras_unicas = []
    conteo_carreras = []
    for carrera in carreras:
        if carrera not in carreras_unicas:
            carreras_unicas.append(carrera)
            conteo_carreras.append(1)
        else:
            conteo_carreras[carreras_unicas.index(carrera)] += 1
    print("\n" + "="*40 + "\n      ESTADÍSTICAS GENERALES\n" + "="*40)
    print(f"Total de Estudiantes: {n}")
    print(f"Promedio General: {promedio_total:.2f}")
    print("\n--- Rendimiento Académico ---")
    print(f"Mejor Promedio: {nombres[idx_max_prom]} ({promedios[idx_max_prom]:.2f})")
    print(f"Menor Promedio: {nombres[idx_min_prom]} ({promedios[idx_min_prom]:.2f})")
    print("\n--- Distribución por Carrera ---")
    for i in range(len(carreras_unicas)):
        print(f"- {carreras_unicas[i]}: {conteo_carreras[i]} estudiante(s)")
    print("="*40)

def mostrar_top_5_mejores_promedios():
    if not nombres:
        print(">> No hay estudiantes registrados.")
        return
    temp_datos = sorted(zip(promedios, nombres, carreras), reverse=True)
    print("\n--- Top 5 Mejores Promedios ---")
    print("-" * 80 + f"\n{'#':<4} | {'Nombre Completo':<30} | {'Promedio':<10} | {'Carrera':<25}\n" + "-" * 80)
    for i, (prom, nom, car) in enumerate(temp_datos[:5]):
        print(f"{i+1:<4} | {nom:<30} | {prom:<10.2f} | {car:<25}")
    print("-" * 80)

# =============================================
# 6. MENÚ INTERACTIVO (Sin cambios)
# =============================================

def menu_ordenamiento(algoritmo):
    while True:
        print(f"\n--- Ordenar con {algoritmo.__name__.replace('_', ' ').title()} ---")
        print("1. Nombre (A-Z)\n2. Promedio (Mayor a menor)\n3. Código estudiantil (Ascendente)\n4. Semestre (Descendente)\n5. Volver")
        opcion_ord = input("Seleccione una opción: ")
        criterio_map = {'1': 'nombre', '2': 'promedio', '3': 'codigo', '4': 'semestre'}
        if opcion_ord in criterio_map:
            if not nombres:
                print("\n>> No hay estudiantes para ordenar.")
                break
            algoritmo(criterio_map[opcion_ord])
            mostrar_tabla_estudiantes()
            break
        elif opcion_ord == '5':
            break
        else:
            print("Opción no válida.")

def main():
    while True:
        print("\n" + "="*50 + "\n      SISTEMA INTEGRAL DE GESTIÓN ACADÉMICA\n" + "="*50)
        print("1. Agregar estudiantes")
        print("2. Mostrar todos los estudiantes")
        print("3. Ordenar (Inserción)")
        print("4. Ordenar (Quicksort)")
        print("\n--- Búsqueda y Filtrado ---")
        print("5. Buscar por código (B. Binaria)")
        print("6. Buscar por nombre (B. Lineal)")
        print("7. Filtrar por promedio")
        print("8. Filtrar por carrera")
        print("\n--- Reportes ---")
        print("9. Estadísticas generales")
        print("10. Top 5 estudiantes")
        print("\n11. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1': registrar_nuevos_estudiantes()
        elif opcion == '2': mostrar_tabla_estudiantes()
        elif opcion == '3': menu_ordenamiento(ordenamiento_insercion)
        elif opcion == '4': menu_ordenamiento(quicksort)
        elif opcion == '5': busqueda_binaria_por_codigo()
        elif opcion == '6': busqueda_lineal_por_nombre()
        elif opcion == '7': filtrar_por_rango_promedio()
        elif opcion == '8': filtrar_por_carrera()
        elif opcion == '9': mostrar_estadisticas_generales()
        elif opcion == '10': mostrar_top_5_mejores_promedios()
        elif opcion == '11':
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            sys.exit()
        else:
            print("\nOpción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()