import sys
import time


nombres = [
    "Juan David Pérez", "Sofía Ramírez", "Carlos Andrés Rojas", "Valentina Morales", 
    "Andrés Felipe Gil", "Camila Andrea Ortiz", "Mateo Jiménez", "Isabella Castro", 
    "Daniel Santiago Ríos", "Laura Valentina Gómez"
]
codigos = [
    20231001, 20222005, 20211010, 20241003, 20202015, 
    20231008, 20212020, 20221012, 20241002, 20201030
]
promedios = [
    4.5, 3.8, 3.2, 4.9, 2.8, 4.1, 3.9, 4.8, 3.5, 4.2
]
materias_aprobadas = [
    28, 22, 15, 6, 40, 25, 20, 29, 5, 45
]
semestres = [
    5, 4, 3, 1, 7, 5, 4, 5, 1, 8
]
carreras = [
    "Ingenieria de Software", "Ingenieria de Software", "Ingenieria de Software", 
    "Ingenieria de Software", "Ingenieria de Software", "Ingenieria de Software", 
    "Ingenieria de Software", "Ingenieria de Software", "Ingenieria de Software", 
    "Ingenieria de Software"
]

CARRERAS_DISPONIBLES = [
    "Ingenieria de Software",
    "Administracion de Empresas",
    "Ingenieria Ambiental",
    "Enfermeria"
]

datos_ordenados_por_codigo = False

# =============================================
# FUNCIONES AUXILIARES (Helpers)
# =============================================
def limpiar_pantalla():
    print("\n" * 20)

def mostrar_tabla_estudiantes(indices=None):
    if not nombres:
        print(">> No hay estudiantes registrados en el sistema.")
        return
    if indices is None:
        indices = range(len(nombres))
    if not indices:
        print(">> No se encontraron estudiantes que coincidan con el criterio.")
        return
    print("-" * 110)
    print(f"{'Código':<12} | {'Nombre Completo':<30} | {'Carrera':<25} | {'Semestre':<10} | {'Promedio':<10} | {'Materias Apr.':<15}")
    print("-" * 110)
    for i in indices:
        print(f"{codigos[i]:<12} | {nombres[i]:<30} | {carreras[i]:<25} | {semestres[i]:<10} | {promedios[i]:<10.2f} | {materias_aprobadas[i]:<15}")
    print("-" * 110)

def intercambiar_datos(i, j):
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
    global datos_ordenados_por_codigo
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de estudiantes a registrar (entre 10 y 50): "))
            if 1 <= cantidad <= 50:
                break
            else:
                print("Error: La cantidad debe estar entre 10 y 50.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

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

    print(f"\n--- Inicio de Registro para la carrera de '{carrera_seleccionada}' ---")
    for i in range(cantidad):
        print(f"\n--- Registrando Estudiante #{i + 1} de {cantidad} ---")
        while True:
            try:
                codigo = int(input(f"Código del estudiante: "))
                if codigo not in codigos: break
                else: print("Error: El código ya existe.")
            except ValueError: print("Error: El código debe ser un número entero.")
        nombre = input("Nombre completo: ").strip().title()
        while True:
            try:
                promedio = float(input("Promedio (0.0 - 5.0): "))
                if 0.0 <= promedio <= 5.0: break
                else: print("Error: El promedio debe estar entre 0.0 y 5.0.")
            except ValueError: print("Error: Ingrese un número decimal.")
        while True:
            try:
                semestre = int(input("Semestre (1 - 10): "))
                if 1 <= semestre <= 10: break
                else: print("Error: El semestre debe estar entre 1 y 10.")
            except ValueError: print("Error: Ingrese un número entero.")
        while True:
            try:
                materias = int(input(f"Materias aprobadas (máximo {semestre * 6}): "))
                if 0 <= materias <= semestre * 6: break
                else: print(f"Error: No puede exceder {semestre * 6}.")
            except ValueError: print("Error: Ingrese un número entero.")
        nombres.append(nombre)
        codigos.append(codigo)
        promedios.append(promedio)
        semestres.append(semestre)
        materias_aprobadas.append(materias)
        carreras.append(carrera_seleccionada)
        datos_ordenados_por_codigo = False
        print(f"¡Estudiante '{nombre}' registrado!")
    print("\n--- Registro Finalizado ---")

# =============================================
# 3. ALGORITMOS DE ORDENAMIENTO (CON TIMING)
# =============================================

def ordenamiento_insercion(criterio):
    global datos_ordenados_por_codigo
    n = len(nombres)

    # Inicia el cronómetro
    inicio = time.time()

    for i in range(1, n):
        key_nombre, key_codigo, key_promedio, key_materias, key_semestre, key_carrera = \
            nombres[i], codigos[i], promedios[i], materias_aprobadas[i], semestres[i], carreras[i]
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
        nombres[j + 1], codigos[j + 1], promedios[j + 1], materias_aprobadas[j + 1], semestres[j + 1], carreras[j + 1] = \
            key_nombre, key_codigo, key_promedio, key_materias, key_semestre, key_carrera

    # Detiene el cronómetro
    fin = time.time()

    datos_ordenados_por_codigo = (criterio == 'codigo')
    print(f"\n>> Datos ordenados por '{criterio}' usando Inserción.")

    # Retorna el tiempo transcurrido
    return fin - inicio

def particion(criterio, bajo, alto):
    pivote_val = None
    if criterio == 'nombre': pivote_val = nombres[alto]
    elif criterio == 'promedio': pivote_val = promedios[alto]
    elif criterio == 'codigo': pivote_val = codigos[alto]
    elif criterio == 'semestre': pivote_val = semestres[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        condicion = False
        if criterio == 'nombre': condicion = nombres[j] <= pivote_val
        elif criterio == 'promedio': condicion = promedios[j] >= pivote_val
        elif criterio == 'codigo': condicion = codigos[j] <= pivote_val
        elif criterio == 'semestre': condicion = semestres[j] >= pivote_val
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
        return 0

    # Inicia el cronómetro
    inicio = time.time()

    quicksort_recursivo(criterio, 0, len(nombres) - 1)

    # Detiene el cronómetro
    fin = time.time()

    datos_ordenados_por_codigo = (criterio == 'codigo')
    print(f"\n>> Datos ordenados por '{criterio}' usando Quicksort.")

    # Retorna el tiempo transcurrido
    return fin - inicio

# ==================================================
# 4. ALGORITMOS DE BÚSQUEDA Y FILTRADO
# ==================================================
def busqueda_binaria_por_codigo():
    if not datos_ordenados_por_codigo:
        print("\nError: Para usar la búsqueda binaria, primero ordene los datos por 'código'.")
        return
    try:
        codigo_buscar = int(input("Ingrese el código a buscar: "))
    except ValueError:
        print("Error: El código debe ser un número.")
        return
    bajo, alto, indice_encontrado = 0, len(codigos) - 1, -1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if codigos[medio] == codigo_buscar:
            indice_encontrado = medio
            break
        elif codigos[medio] < codigo_buscar: bajo = medio + 1
        else: alto = medio - 1
    if indice_encontrado != -1:
        print(f"\n--- Estudiante Encontrado (Código: {codigo_buscar}) ---")
        mostrar_tabla_estudiantes([indice_encontrado])
    else:
        print(f"\n>> No se encontró estudiante con el código {codigo_buscar}.")

def busqueda_lineal_por_nombre():
    if not nombres:
        print(">> No hay estudiantes registrados.")
        return
    nombre_parcial = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().lower()
    if not nombre_parcial:
        print("Error: El término de búsqueda no puede estar vacío.")
        return
    indices_encontrados = [i for i, nombre in enumerate(nombres) if nombre_parcial in nombre.lower()]
    print(f"\n--- Resultados para '{nombre_parcial}' ---")
    mostrar_tabla_estudiantes(indices_encontrados)

def filtrar_por_rango_promedio():
    if not nombres:
        print(">> No hay estudiantes registrados.")
        return
    try:
        min_prom = float(input("Promedio mínimo del rango: "))
        max_prom = float(input("Promedio máximo del rango: "))
        if min_prom > max_prom:
            print("Error: El mínimo no puede ser mayor que el máximo.")
            return
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return
    indices = [i for i, prom in enumerate(promedios) if min_prom <= prom <= max_prom]
    print(f"\n--- Estudiantes con Promedio entre {min_prom:.2f} y {max_prom:.2f} ---")
    mostrar_tabla_estudiantes(indices)

def filtrar_por_carrera():
    if not nombres:
        print(">> No hay estudiantes registrados.")
        return
    carrera_buscar = input("Ingrese la carrera a filtrar: ").strip().lower()
    if not carrera_buscar:
        print("Error: El nombre de la carrera no puede estar vacío.")
        return
    indices = [i for i, c in enumerate(carreras) if c.lower() == carrera_buscar]
    print(f"\n--- Estudiantes de la Carrera: '{carrera_buscar.title()}' ---")
    mostrar_tabla_estudiantes(indices)

# =============================================
# 5. ESTADÍSTICAS Y REPORTES
# =============================================
def mostrar_estadisticas_generales():
    if not nombres:
        print(">> No hay estudiantes para generar estadísticas.")
        return
    n = len(nombres)
    promedio_total = sum(promedios) / n
    idx_max_prom = promedios.index(max(promedios))
    idx_min_prom = promedios.index(min(promedios))
    carreras_unicas, conteo_carreras = [], []
    for carrera in carreras:
        if carrera not in carreras_unicas:
            carreras_unicas.append(carrera)
            conteo_carreras.append(1)
        else:
            conteo_carreras[carreras_unicas.index(carrera)] += 1
    print("\n" + "="*40 + "\n      ESTADÍSTICAS GENERALES\n" + "="*40)
    print(f"Total de Estudiantes: {n}\nPromedio General: {promedio_total:.2f}")
    print(f"\nMejor Promedio: {nombres[idx_max_prom]} ({promedios[idx_max_prom]:.2f})")
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

def mostrar_top_5_indice_rendimiento():
    if not nombres:
        print(">> No hay estudiantes registrados.")
        return
    
    # Calcular índices de rendimiento para todos los estudiantes
    indices_rendimiento = []
    for i in range(len(nombres)):
        # Componente del promedio (60%)
        comp_promedio = promedios[i] * 0.60
        # Componente de avance en la carrera (40%)
        max_materias = semestres[i] * 6  # Máximo de materias posibles hasta el semestre actual
        avance = (materias_aprobadas[i] / max_materias) * 5  # Normalizado a escala de 5
        comp_avance = avance * 0.40
        # Índice total
        indice = comp_promedio + comp_avance
        indices_rendimiento.append((indice, nombres[i], carreras[i], promedios[i], materias_aprobadas[i], semestres[i]))
    
    # Ordenar por índice de rendimiento (orden descendente)
    indices_rendimiento.sort(reverse=True)
    
    print("\n--- Top 5 por Índice de Rendimiento ---")
    print("-" * 120)
    print(f"{'#':<4} | {'Nombre':<25} | {'Índice':<8} | {'Promedio':<8} | {'Mat. Apr.':<8} | {'Semestre':<8} | {'Carrera':<25}")
    print("-" * 120)
    
    for i, (indice, nom, car, prom, mat, sem) in enumerate(indices_rendimiento[:5]):
        print(f"{i+1:<4} | {nom:<25} | {indice:<8.2f} | {prom:<8.2f} | {mat:<8d} | {sem:<8d} | {car:<25}")
    print("-" * 120)
    print("\nFórmula del Índice de Rendimiento:")
    print("(Promedio x 60%) + (Materias Aprobadas ÷ (Semestre x 6) x 5 x 40%)")

# =============================================
# 6. MENÚ INTERACTIVO
# =============================================
def menu_ordenamiento(algoritmo):
    while True:
        print(f"\n--- Ordenar con {algoritmo.__name__.replace('_', ' ').title()} ---")
        print("1. Nombre (A-Z)\n2. Promedio (Mayor a menor)\n3. Código (Ascendente)\n4. Semestre (Descendente)\n5. Volver")
        opcion_ord = input("Seleccione una opción: ")
        criterio_map = {'1': 'nombre', '2': 'promedio', '3': 'codigo', '4': 'semestre'}

        if opcion_ord in criterio_map:
            if not nombres:
                print("\n>> No hay estudiantes para ordenar.")
                break

            # Llama al algoritmo y recibe el tiempo de ejecución
            tiempo_transcurrido = algoritmo(criterio_map[opcion_ord])

            # Muestra la tabla de datos ya ordenados
            mostrar_tabla_estudiantes()

            # Imprime el tiempo de ejecución debajo de la tabla
            print(f"\n⏱️ Tiempo de ordenamiento ({algoritmo.__name__}): {tiempo_transcurrido:.6f} segundos.")
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
        print("10. Top 5 por promedio")
        print("11. Top 5 por índice de rendimiento")
        print("\n12. Salir")
        print("="*50)
        opcion = input("Seleccione una opción: ")
        
        opciones = {
            '1': registrar_nuevos_estudiantes, '2': mostrar_tabla_estudiantes,
            '3': lambda: menu_ordenamiento(ordenamiento_insercion),
            '4': lambda: menu_ordenamiento(quicksort),
            '5': busqueda_binaria_por_codigo, '6': busqueda_lineal_por_nombre,
            '7': filtrar_por_rango_promedio, '8': filtrar_por_carrera,
            '9': mostrar_estadisticas_generales, '10': mostrar_top_5_mejores_promedios,
            '11': mostrar_top_5_indice_rendimiento
        }
        
        if opcion in opciones:
            opciones[opcion]()
        elif opcion == '12':
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            sys.exit()
        else:
            print("\nOpción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()