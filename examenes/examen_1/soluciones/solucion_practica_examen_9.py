"""
POSIBLE Solución del Sistema de Triage Hospitalario con Gestión de Recursos Críticos
"""
# ==============================================================================
# MÓDULO DE NEGOCIO DEL HOSPITAL (Lógica, Variables Globales y Funciones)
# ==============================================================================

# Variables Globales de Estado (Requisito de Implementación)
PACIENTES = []
NEXT_ID = 1
RECURSOS_CRITICOS = {
    "CAMA UCI": {"total": 3, "disponible": 3, "nivel_triage": 5},
    "EQUIPO DE CHOQUE": {"total": 5, "disponible": 5, "nivel_triage": 4},
    "SALA DE OBSERVACIÓN": {"total": 10, "disponible": 10, "nivel_triage": 3},
}

# --- Funciones de Cálculo de Triage (EAT) ---

def calcular_puntuacion_tas(tas: int) -> int:
    """Calcula los puntos EAT por Tensión Arterial Sistólica (TAS).

    Args:
        tas: Valor de la Tensión Arterial Sistólica en mmHg.

    Returns:
        Puntuación EAT (0, 2 o 3) basada en el rango de TAS.
    """
    if tas <= 90:
        return 3
    elif 91 <= tas <= 100 or tas >= 160:
        return 2
    else: # 101 - 159
        return 0

def calcular_puntuacion_fr(fr: int) -> int:
    """Calcula los puntos EAT por Frecuencia Respiratoria (FR).

    Args:
        fr: Valor de la Frecuencia Respiratoria en respiraciones por minuto (rpm).

    Returns:
        Puntuación EAT (0, 2 o 3) basada en el rango de FR.
    """
    if fr >= 25:
        return 3
    elif fr <= 8:
        return 2
    else: # 9 - 24
        return 0

def calcular_puntuacion_fc(fc: int) -> int:
    """Calcula los puntos EAT por Frecuencia Cardiaca (FC).

    Args:
        fc: Valor de la Frecuencia Cardiaca en latidos por minuto (lpm).

    Returns:
        Puntuación EAT (0, 2 o 3) basada en el rango de FC.
    """
    if fc >= 130:
        return 3
    elif 100 <= fc <= 129:
        return 2
    else: # 50 - 99
        return 0

def calcular_puntuacion_temp_dolor(temp: float, dolor: int) -> int:
    """Calcula los puntos EAT por Temperatura y Nivel de Dolor.

    Args:
        temp: Valor de la Temperatura corporal en grados Celsius (°C).
        dolor: Nivel de Dolor en una escala del 1 al 10.

    Returns:
        Puntuación EAT (0, 1 o 2) combinada por ambos factores.
    """
    puntos = 0
    if temp >= 38.5 or temp <= 35.0:
        puntos += 1
    if dolor >= 8:
        puntos += 1
    return puntos

def asignar_triage_y_recurso(puntuacion_eat: int) -> tuple[int, str, str]:
    """Asigna Nivel, Color y Recurso Requerido basándose en la Puntuación EAT.

    Args:
        puntuacion_eat: Puntuación EAT total calculada para el paciente.

    Returns:
        Una tupla con el Nivel (int), Color (str) y Recurso Requerido (str).
    """
    if puntuacion_eat >= 5:
        nivel, color, recurso_req = 5, "ROJO", "CAMA UCI"
    elif 3 <= puntuacion_eat <= 4:
        nivel, color, recurso_req = 4, "NARANJA", "EQUIPO DE CHOQUE"
    elif puntuacion_eat == 2:
        nivel, color, recurso_req = 3, "AMARILLO", "SALA DE OBSERVACIÓN"
    elif puntuacion_eat == 1:
        nivel, color, recurso_req = 2, "VERDE", "NINGUNO"
    else: # puntuacion_eat == 0
        nivel, color, recurso_req = 1, "AZUL", "NINGUNO"

    return nivel, color, recurso_req

# --- Funciones de Gestión de Pacientes y Recursos ---

def ingresar_paciente() -> None:
    """Recibe datos del paciente, calcula EAT, asigna recurso y agrega a la lista global.

    Modifica las variables globales PACIENTES y NEXT_ID.
    """
    global NEXT_ID

    print("\n--- INGRESO DE NUEVO PACIENTE ---")
    nombre = input("Nombre completo: ").strip()
    edad = int(input("Edad: "))
    sintomas = input("Síntomas Clave: ").strip()
    print("--- INGRESO DE SIGNOS VITALES ---")
    tas = int(input("TAS (mmHg): "))
    fr = int(input("FR (rpm): "))
    fc = int(input("FC (lpm): "))
    temp = float(input("Temp (°C, ej: 36.5): "))
    dolor = int(input("Nivel de Dolor (1-10): "))

    # 1. Cálculo de Puntuación EAT
    puntos_tas = calcular_puntuacion_tas(tas)
    puntos_fr = calcular_puntuacion_fr(fr)
    puntos_fc = calcular_puntuacion_fc(fc)
    puntos_tyd = calcular_puntuacion_temp_dolor(temp, dolor)
    puntuacion_total = puntos_tas + puntos_fr + puntos_fc + puntos_tyd

    # 2. Asignación de Triage y Recurso Requerido
    nivel, color, recurso_req = asignar_triage_y_recurso(puntuacion_total)

    # 3. Creación del objeto paciente
    nuevo_paciente = {
        "ID": NEXT_ID,
        "Nombre": nombre,
        "Edad": edad,
        "Síntomas": sintomas,
        "Signos Vitales": {"TAS": tas, "FR": fr, "FC": fc, "Temp": temp, "Dolor": dolor},
        "Puntuación EAT": puntuacion_total,
        "Nivel": nivel,
        "Color": color,
        "Recurso Requerido": recurso_req,
        "Estado": "EN ESPERA",
    }

    PACIENTES.append(nuevo_paciente)

    print(f"\n[ÉXITO] Paciente ID {NEXT_ID} ingresado. Prioridad {color}. Recurso requerido: {recurso_req}.")
    NEXT_ID += 1

def procesar_paciente() -> None:
    """Intenta admitir al paciente más urgente y en espera (máximo Nivel, mínimo ID).

    Si el paciente requiere un recurso crítico, intenta asignarlo y cambia el estado a 'EN PROCESAMIENTO'.
    Si el paciente es Nivel 1 o 2, se da de alta inmediatamente.

    Modifica las variables globales PACIENTES y RECURSOS_CRITICOS.
    """
    global PACIENTES, RECURSOS_CRITICOS

    # 1. Identificar al paciente más urgente (Prioridad Max, luego ID Min)
    pacientes_en_espera = sorted(
        [p for p in PACIENTES if p['Estado'] == 'EN ESPERA'],
        key=lambda p: (-p['Nivel'], p['ID'])
    )

    if not pacientes_en_espera:
        print("\n[INFO] No hay pacientes EN ESPERA para procesar.")
        return

    paciente_a_procesar = pacientes_en_espera[0]
    id_proc = paciente_a_procesar['ID']
    nivel_proc = paciente_a_procesar['Nivel']
    recurso_req = paciente_a_procesar['Recurso Requerido']
    nombre_proc = paciente_a_procesar['Nombre']

    print(f"\n--- INTENTO DE ADMISIÓN (ID: {id_proc}, Prioridad: {paciente_a_procesar['Color']}) ---")

    # 2. Manejo de Nivel 1 o 2 (Sin Recurso Crítico)
    if nivel_proc <= 2:
        # Se atiende y retira de la lista inmediatamente
        PACIENTES = [p for p in PACIENTES if p['ID'] != id_proc]
        print(f"[ATENDIDO] {nombre_proc} (ID: {id_proc}) - Nivel general. No consume recurso crítico.")
        return

    # 3. Manejo de Nivel 3, 4 o 5 (Con Recurso Crítico)

    # Identificar el recurso en el inventario
    recurso_data = RECURSOS_CRITICOS.get(recurso_req)

    if recurso_data and recurso_data['disponible'] > 0:
        # Asignar el recurso (decrementa el inventario)
        RECURSOS_CRITICOS[recurso_req]['disponible'] -= 1

        # Cambiar el estado a EN PROCESAMIENTO (permanece en la lista)
        for p in PACIENTES:
            if p['ID'] == id_proc:
                p['Estado'] = 'EN PROCESAMIENTO'
                break

        print(f"[ADMITIDO] {nombre_proc} admitido en {recurso_req}.")
        print(f"Recursos restantes de {recurso_req}: {RECURSOS_CRITICOS[recurso_req]['disponible']}")
    else:
        # No hay disponibilidad
        print(f"[BLOQUEADO] No hay {recurso_req} disponible. Paciente {nombre_proc} sigue EN ESPERA.")
        # El paciente permanece en estado EN ESPERA

def liberar_recurso() -> None:
    """Simula la finalización del tratamiento de un paciente 'EN PROCESAMIENTO' y libera el recurso crítico asociado.

    El paciente es removido de la lista global de pacientes.

    Modifica las variables globales PACIENTES y RECURSOS_CRITICOS.
    """
    global PACIENTES, RECURSOS_CRITICOS

    pacientes_en_proceso = [p for p in PACIENTES if p['Estado'] == 'EN PROCESAMIENTO']

    if not pacientes_en_proceso:
        print("\n[INFO] No hay pacientes EN PROCESAMIENTO para dar de alta.")
        return

    print("\n--- LIBERACIÓN DE RECURSO ---")
    print("Pacientes actualmente en proceso:")
    for p in pacientes_en_proceso:
        print(f"  ID: {p['ID']} | Nombre: {p['Nombre']} | Usando: {p['Recurso Requerido']}")

    try:
        id_dar_alta = int(input("ID del paciente dado de alta: "))
    except ValueError:
        print("[ERROR] ID inválido. Intente de nuevo.")
        return

    paciente_alta = next((p for p in pacientes_en_proceso if p['ID'] == id_dar_alta), None)

    if paciente_alta:
        recurso_req = paciente_alta['Recurso Requerido']

        # 1. Liberación: Incrementa la disponibilidad
        if recurso_req in RECURSOS_CRITICOS:
            RECURSOS_CRITICOS[recurso_req]['disponible'] += 1
            print(f"\n[LIBERADO] Recurso {recurso_req} liberado.")
            print(f"Recursos disponibles ahora: {RECURSOS_CRITICOS[recurso_req]['disponible']}")
        else:
            # Esto no debería ocurrir para niveles 3, 4, 5
            print(f"\n[ADVERTENCIA] El recurso {recurso_req} no es un recurso crítico gestionado.")

        # 2. Retira al paciente de la lista (DISCARGADO)
        global PACIENTES
        PACIENTES = [p for p in PACIENTES if p['ID'] != id_dar_alta]

        print(f"[DISCARGADO] Paciente {paciente_alta['Nombre']} dado de alta y removido de la lista.")

    else:
        print(f"\n[ERROR] El paciente con ID {id_dar_alta} no fue encontrado o no está EN PROCESAMIENTO.")

def ver_lista() -> None:
    """Muestra la lista de pacientes global ordenada por Prioridad (Nivel descendente) y Antigüedad (ID ascendente)."""

    if not PACIENTES:
        print("\n[INFO] La lista de pacientes está vacía.")
        return

    # Ordenar: Nivel (descendente) y luego ID (ascendente)
    lista_ordenada = sorted(PACIENTES, key=lambda p: (-p['Nivel'], p['ID']))

    print("\n--- LISTA DE ESPERA (Prioridad EAT y Antigüedad) ---")
    print(f"Total de Pacientes: {len(lista_ordenada)}")

    for i, p in enumerate(lista_ordenada, 1):
        sv = p['Signos Vitales']
        print(f"\n--- Posición {i} ---")
        print(f"ID: {p['ID']} | Nombre: {p['Nombre']} | Estado: {p['Estado']}")
        print(f"  > Triage: {p['Color']} (N{p['Nivel']}) - EAT: {p['Puntuación EAT']} pts")
        print(f"  > Recurso: {p['Recurso Requerido']}")
        print(f"  > SV: TAS:{sv['TAS']} | FR:{sv['FR']} | FC:{sv['FC']} | Temp:{sv['Temp']} | Dolor:{sv['Dolor']}")

def analizar() -> None:
    """Genera un reporte estadístico que incluye ocupación de recursos y promedios de signos vitales.

    Utiliza las variables globales PACIENTES y RECURSOS_CRITICOS para el cálculo de métricas.
    """

    if not PACIENTES:
        print("\n[INFO] No hay pacientes para generar el reporte estadístico.")
        return

    print("\n--- REPORTE ESTADÍSTICO DE GESTIÓN DE RECURSOS ---")

    # 1. Número total de pacientes
    total_pacientes = len(PACIENTES)
    print(f"Número total de pacientes en sala (Espera + Proceso): {total_pacientes}")

    # 2. Ocupación de Recursos
    print("\n-- Ocupación y Utilización de Recursos --")
    for recurso, data in RECURSOS_CRITICOS.items():
        ocupado = data['total'] - data['disponible']
        utilizacion_pct = (ocupado / data['total']) * 100 if data['total'] > 0 else 0

        print(f"  > {recurso}: Capacidad Total={data['total']} | Ocupado={ocupado} | Disponible={data['disponible']}")
        print(f"    [Utilización: {utilizacion_pct:.1f}%]")

    # 3. Promedio General de Signos Vitales
    suma_tas, suma_fr, suma_fc, suma_temp, suma_dolor = 0, 0, 0, 0.0, 0
    for p in PACIENTES:
        sv = p['Signos Vitales']
        suma_tas += sv['TAS']
        suma_fr += sv['FR']
        suma_fc += sv['FC']
        suma_temp += sv['Temp']
        suma_dolor += sv['Dolor']

    promedio_tas = suma_tas / total_pacientes
    promedio_fr = suma_fr / total_pacientes
    promedio_fc = suma_fc / total_pacientes
    promedio_temp = suma_temp / total_pacientes
    promedio_dolor = suma_dolor / total_pacientes

    print("\n-- Promedios de Signos Vitales --")
    print(f"  > Promedio TAS: {promedio_tas:.1f}")
    print(f"  > Promedio FR: {promedio_fr:.1f}")
    print(f"  > Promedio FC: {promedio_fc:.1f}")
    print(f"  > Promedio Temp: {promedio_temp:.2f} °C")
    print(f"  > Promedio Dolor: {promedio_dolor:.1f}")

    # 4. Prioridad más alta
    max_nivel = max(p['Nivel'] for p in PACIENTES)
    color_max = next(p['Color'] for p in PACIENTES if p['Nivel'] == max_nivel)
    print(f"\nPrioridad más alta en sala: {color_max} (Nivel {max_nivel})")


# ==============================================================================
# FUNCIÓN PRINCIPAL DEL PROGRAMA (Coordinación y Menú Interactivo)
# ==============================================================================

def main() -> None:
    """Función principal para ejecutar el ciclo del programa y el menú de opciones interactivas."""
    print("--- Sistema de Triage Hospitalario v4.0 (Gestión de Recursos Críticos) ---")
    print("Bienvenido. Preparese para gestionar la disponibilidad de UCI y Choque.")

    terminar = False
    while not terminar:
        opcion = input("\nOpción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: ").upper()

        if opcion == 'I':
            ingresar_paciente()
        elif opcion == 'P':
            procesar_paciente()
        elif opcion == 'L':
            liberar_recurso()
        elif opcion == 'V':
            ver_lista()
        elif opcion == 'A':
            analizar()
        elif opcion == 'F':
            print("\nPrograma finalizado. Saliendo del sistema.")
            terminar = True
        else:
            print("[ERROR] Opción no válida. Intente con I, P, L, V, A o F.")