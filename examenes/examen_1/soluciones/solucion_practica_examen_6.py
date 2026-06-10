# =============================================================================
# OPTIMIZACIÓN DEL RIEGO EN CULTIVOS HIDROPÓNICOS
# =============================================================================

def main():
    """
    Función Principal: Define los parámetros del desafío y gestiona
    el menú interactivo para evaluar estrategias de riego.
    """
    
    # --- PARÁMETROS DEL DESAFÍO DE RIEGO ---
    
    # Unidades totales de agua que deben ser distribuidas para completar el cultivo.
    unidades_agua_totales = 80
    
    # Tiempo de penalización (en segundos) por cambiar el sistema de tuberías entre ciclos.
    duracion_mantenimiento = 20
    
    # Tabla de Rendimiento de Tuberías: {Tipo: (Tiempo por 1ra UA, Degradación por UA Adicional)}
    datos_tuberia = {
        'A': (0.80, 0.12),  # Alto Caudal
        'M': (1.00, 0.08),  # Mediano Caudal
        'B': (1.20, 0.03)   # Bajo Caudal
    }
    tipos_tuberia_validos = list(datos_tuberia.keys())

    print(f"--- SIMULADOR DE EFICIENCIA HÍDRICA ---")
    print(f"Total de Agua Requerida: {unidades_agua_totales} UA")
    print(f"Costo por Mantenimiento: {duracion_mantenimiento} segundos\n")

    # --- VARIABLES DE SEGUIMIENTO ---
    mejor_tiempo = float('inf') 
    ingeniero_ganador = None
    
    # --- BUCLE PRINCIPAL DEL MENÚ ---
    opcion = -1 
    while opcion != 0:
        # PASO 1: Leer la opción del usuario.
        opcion = leer_opcion_menu("\nOpción [1=Analizar 2=Ganador 0=Salir]: ")

        if opcion == 1:
            # PASO 2: Procesar una nueva estrategia.
            resultado = analizar_estrategia(
                unidades_agua_totales, 
                duracion_mantenimiento, 
                datos_tuberia, 
                tipos_tuberia_validos
            )
            
            # PASO 3: Actualizar el récord si la nueva estrategia es válida y mejor.
            if resultado is not None:
                nombre, tiempo = resultado
                if tiempo < mejor_tiempo:
                    mejor_tiempo = tiempo
                    ingeniero_ganador = nombre

        elif opcion == 2:
            # PASO 4: Mostrar el mejor resultado registrado.
            if ingeniero_ganador is None:
                print("No hay estrategias ganadoras registradas todavía.")
            else:
                print(f"\nEl Ingeniero {ingeniero_ganador} lidera la optimización.")
                print(f"Tiempo Récord: {mejor_tiempo:.2f} segundos")

    print("\nSaliendo del programa de simulación.")

# ----------------------------------------------------------------------
# FUNCIONES DE LECTURA DE DATOS Y MENÚ
# ----------------------------------------------------------------------

def leer_opcion_menu(mensaje):
    """
    Lee y valida la opción del menú (0, 1, o 2).
    Usa un bucle while controlado por la validez del dato.
    """
    opcion_valida = None
    while opcion_valida is None:
        try:
            opcion = int(input(mensaje))
            if opcion in [0, 1, 2]:
                opcion_valida = opcion
            else:
                print("Opción inválida. Ingrese 0, 1 o 2.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
    return opcion_valida

def leer_entero_positivo(mensaje):
    """
    Lee y valida que la entrada sea un entero estrictamente positivo (> 0).
    """
    valor_valido = None
    while valor_valido is None:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Error: El valor debe ser un entero positivo.")
            else:
                valor_valido = valor
        except ValueError:
            print("Error: Ingrese un número entero válido.")
    return valor_valido

def leer_tipo_tuberia(mensaje, tipos_validos):
    """
    Lee el tipo de tubería y valida que sea una de las opciones permitidas (A, M, B).
    """
    tipo_valido = None
    while tipo_valido is None:
        tipo = input(mensaje).upper()
        if tipo in tipos_validos:
            tipo_valido = tipo
        else:
            print(f"Error: Tipo de tubería inválido. Opciones válidas: {', '.join(tipos_validos)}")
    return tipo_valido

# ----------------------------------------------------------------------
# FUNCIÓN DE LÓGICA Y VALIDACIÓN
# ----------------------------------------------------------------------

def analizar_estrategia(ua_totales, duracion_mantenimiento, datos_tuberia, tipos_tuberia_validos):
    """
    Procesa la secuencia de ciclos de riego, calcula el tiempo total
    y realiza las validaciones de las reglas del desafío.
    """
    nombre_equipo = input("Nombre del ingeniero: ")
    num_ciclos = leer_entero_positivo("Cantidad ciclos de riego: ")

    tiempo_total_carrera = 0.0
    ua_distribuidas = 0
    estrategia_valida = True

    # Bucle para procesar cada ciclo de riego
    for i in range(1, num_ciclos + 1):
        # Condicional que previene procesar más ciclos si ya se encontró un error
        if estrategia_valida:
            try:
                print(f"--- Ciclo {i} ---")
                
                # PASO 1: Obtener datos de entrada para el ciclo actual.
                tipo_tuberia = leer_tipo_tuberia(f"Ciclo {i} tipo de tubería ({'/'.join(tipos_tuberia_validos)}): ", tipos_tuberia_validos)
                cantidad_ua = leer_entero_positivo(f"Ciclo {i} cantidad de UA: ")

                # PASO 2: Calcular la duración del ciclo (incluyendo el desgaste).
                duracion_ciclo = calcular_duracion_ciclo(tipo_tuberia, cantidad_ua, datos_tuberia)

                # PASO 3: Acumular el tiempo y las unidades de agua.
                tiempo_total_carrera += duracion_ciclo
                ua_distribuidas += cantidad_ua

                # PASO 4: Sumar el costo de mantenimiento si es necesario.
                if i < num_ciclos:
                    tiempo_total_carrera += duracion_mantenimiento

            except ValueError as e:
                # Si calcular_duracion_ciclo lanza un error, se invalida la estrategia.
                print(f"Error en el Ciclo {i}: {e}")
                estrategia_valida = False

            # PASO 5: Validación: ¿Excedimos el límite total de agua?
            if estrategia_valida and (ua_distribuidas > ua_totales):
                print(f"ERROR: La suma de UA ({ua_distribuidas}) excede el total permitido ({ua_totales}).")
                estrategia_valida = False
        
    # --- VALIDACIONES FINALES ---

    # PASO 6: Validación: ¿Se distribuyó la cantidad exacta requerida?
    if estrategia_valida and (ua_distribuidas != ua_totales):
        print(f"ERROR: La suma de UA no es {ua_totales}. Total ingresado: {ua_distribuidas}.")
        estrategia_valida = False

    # PASO 7: Retornar resultado
    if not estrategia_valida:
        print(f"Ingeniero {nombre_equipo} desclasificado por estrategia inválida.")
        return None

    print(f"Ingeniero {nombre_equipo} terminará en {tiempo_total_carrera:.2f}s")
    return (nombre_equipo, tiempo_total_carrera)

# ----------------------------------------------------------------------
# FUNCIONES DE CÁLCULO
# ----------------------------------------------------------------------

def calcular_duracion_ciclo(tipo_tuberia, cantidad_ua, datos_tuberia):
    """
    Calcula la duración total de un ciclo de riego, aplicando el desgaste
    acumulado según la cantidad de UA y el tipo de tubería.
    """
    try:
        if cantidad_ua <= 0:
            raise ValueError("La cantidad de UA debe ser positiva.")

        # PASO 1: Obtener los coeficientes del tipo de tubería.
        tiempo_base = obtener_tiempo_primera_ua(tipo_tuberia, datos_tuberia)
        degradacion = obtener_degradacion_por_ua(tipo_tuberia, datos_tuberia)

        # PASO 2: Calcular el factor de desgaste acumulado.
        # Suma de la serie aritmética: (N * (N - 1)) / 2
        suma_degradacion_indices = cantidad_ua * (cantidad_ua - 1) / 2

        # PASO 3: Calcular el tiempo total.
        # Tiempo = (Tiempo Base * N) + (Degradación * Desgaste Acumulado)
        tiempo_total_procesamiento = (tiempo_base * cantidad_ua) + (degradacion * suma_degradacion_indices)

        return tiempo_total_procesamiento

    except ValueError as e:
        # Propagar la excepción para manejar la desclasificación
        raise e

# ----------------------------------------------------------------------
# FUNCIONES AUXILIARES DE DATOS
# ----------------------------------------------------------------------

def obtener_tiempo_primera_ua(tipo_tuberia, datos_tuberia):
    """Busca el tiempo que tarda la primera Unidad de Agua (UA) en distribuirse."""
    if tipo_tuberia not in datos_tuberia:
        raise ValueError("Tipo de tubería no definido.")
    return datos_tuberia[tipo_tuberia][0]

def obtener_degradacion_por_ua(tipo_tuberia, datos_tuberia):
    """Busca la degradación en segundos por cada UA adicional distribuida."""
    if tipo_tuberia not in datos_tuberia:
        raise ValueError("Tipo de tubería no definido.")
    return datos_tuberia[tipo_tuberia][1]

# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

main()