# =============================================================================
# FUNCIONES DE CÁLCULO (PURAS) - NO INTERACTÚAN CON EL USUARIO
# =============================================================================

def calcular_crecimiento_logistico(p_inicial: float, tasa_r: float, capacidad_k: float) -> int:
    """
    Calcula el crecimiento poblacional usando el modelo logístico.
    
    El modelo logístico describe el crecimiento de una población en un entorno
    con recursos limitados, considerando la capacidad de carga del entorno.
    
    Parámetros:
        p_inicial (float): Población inicial
        tasa_r (float): Tasa intrínseca de crecimiento (decimal, ej: 0.1 para 10%)
        capacidad_k (float): Capacidad de carga del entorno
    
    Retorna:
        int: Nueva población (población inicial + cambio), truncada a entero
    
    Fórmula utilizada:
        ΔP = tasa_r × p_inicial × (1 - p_inicial/capacidad_k)
        Nueva población = p_inicial + ΔP
    """
    # Calcular el cambio en la población usando la fórmula del modelo logístico
    delta_p = tasa_r * p_inicial * (1 - (p_inicial / capacidad_k))
    
    # Calcular la nueva población
    nueva_poblacion = p_inicial + delta_p
    
    # Retornar truncado a entero como se especifica
    return int(nueva_poblacion)


def calcular_velocidad_terminal(masa: float, area_proyectada: float, coef_arrastre: float) -> float:
    """
    Calcula la velocidad terminal de un objeto cayendo a través del aire.
    
    La velocidad terminal es la velocidad constante máxima que alcanza un objeto
    cuando la fuerza de resistencia del aire se iguala a la fuerza de gravedad.
    
    Parámetros:
        masa (float): Masa del objeto en kg
        area_proyectada (float): Área de la sección transversal en m²
        coef_arrastre (float): Coeficiente de arrastre (adimensional)
    
    Retorna:
        float: Velocidad terminal en m/s
    
    Fórmula utilizada:
        v_t = √(2 × masa × g / (ρ × área × coef_arrastre))
    
    Constantes utilizadas:
        g = 9.81 m/s² (aceleración de la gravedad)
        ρ = 1.225 kg/m³ (densidad del aire a nivel del mar)
    """
    # Constantes físicas
    g = 9.81  # Aceleración de la gravedad en m/s²
    rho = 1.225  # Densidad del aire en kg/m³
    
    # Calcular velocidad terminal usando la fórmula
    numerador = 2 * masa * g
    denominador = rho * area_proyectada * coef_arrastre
    
    velocidad_terminal = (numerador / denominador)**(1/2)
    
    return velocidad_terminal


# =============================================================================
# FUNCIONES DE VALIDACIÓN DE ENTRADA
# =============================================================================

def obtener_numero_positivo(mensaje: str) -> float:
    """
    Solicita al usuario un número positivo con validación completa.
    
    Parámetros:
        mensaje (str): Mensaje a mostrar al usuario
    
    Retorna:
        float: Número positivo válido ingresado por el usuario
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: El valor debe ser positivo (mayor que 0). Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número válido. Intente nuevamente.")


def obtener_opcion_menu() -> int:
    """
    Solicita al usuario una opción válida del menú principal.
    
    Retorna:
        int: Opción válida del menú (1, 2, o 3)
    """
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-3): "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Error: Debe seleccionar una opción válida (1, 2 o 3). Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")


# =============================================================================
# FUNCIONES GESTORAS (INTERFAZ) - MANEJAN LA INTERACCIÓN CON EL USUARIO
# =============================================================================

def gestionar_simulacion_poblacional() -> None:
    """
    Función gestora para el modelo de crecimiento poblacional logístico.
    
    Maneja toda la interacción con el usuario: explicación del modelo,
    solicitud y validación de datos, llamada a la función de cálculo
    y presentación de resultados.
    """
    print("\n" + "="*60)
    print("MODELO LOGÍSTICO DE CRECIMIENTO POBLACIONAL")
    print("="*60)
    print()
    print("El modelo logístico describe el crecimiento de una población")
    print("en un entorno con recursos limitados. A diferencia del crecimiento")
    print("exponencial, este modelo considera la 'capacidad de carga' (K),")
    print("que es el tamaño máximo de población que el entorno puede sostener.")
    print()
    
    # Solicitar y validar datos de entrada
    print("Ingrese los parámetros para la simulación:")
    p_inicial = obtener_numero_positivo("Población inicial: ")
    
    print("Tasa de crecimiento (ejemplo: 0.1 para 10%): ", end="")
    tasa_r = obtener_numero_positivo("")
    
    capacidad_k = obtener_numero_positivo("Capacidad de carga del entorno: ")
    
    # Validación adicional: capacidad debe ser mayor que población inicial
    while capacidad_k <= p_inicial:
        print(f"Error: La capacidad de carga ({capacidad_k}) debe ser mayor")
        print(f"que la población inicial ({p_inicial}). Intente nuevamente.")
        capacidad_k = obtener_numero_positivo("Capacidad de carga del entorno: ")
    
    # Llamar a la función de cálculo pura
    nueva_poblacion = calcular_crecimiento_logistico(p_inicial, tasa_r, capacidad_k)
    
    # Presentar resultados
    print()
    print("RESULTADO DE LA SIMULACIÓN:")
    print("-" * 30)
    print(f"En un entorno con capacidad para {int(capacidad_k)} individuos,")
    print(f"una población inicial de {int(p_inicial)} con una tasa de")
    print(f"crecimiento de {tasa_r} crecerá a aproximadamente")
    print(f"{nueva_poblacion} individuos en el siguiente periodo.")
    print()


def gestionar_calculo_velocidad_terminal() -> None:
    """
    Función gestora para el cálculo de velocidad terminal.
    
    Maneja toda la interacción con el usuario: explicación del concepto,
    solicitud y validación de datos, llamada a la función de cálculo
    y presentación de resultados.
    """
    print("\n" + "="*60)
    print("CÁLCULO DE VELOCIDAD TERMINAL")
    print("="*60)
    print()
    print("La velocidad terminal es la velocidad constante máxima que")
    print("alcanza un objeto al caer a través de un fluido (como el aire).")
    print("Se produce cuando la fuerza de resistencia del fluido se iguala")
    print("a la fuerza de la gravedad, resultando en aceleración neta cero.")
    print()
    
    # Solicitar y validar datos de entrada
    print("Ingrese los parámetros del objeto:")
    masa = obtener_numero_positivo("Masa del objeto (kg): ")
    area_proyectada = obtener_numero_positivo("Área proyectada (m²): ")
    
    print("Coeficiente de arrastre (ejemplo: 0.5 para esfera): ", end="")
    coef_arrastre = obtener_numero_positivo("")
    
    # Llamar a la función de cálculo pura
    velocidad_terminal = calcular_velocidad_terminal(masa, area_proyectada, coef_arrastre)
    
    # Presentar resultados
    print()
    print("RESULTADO DEL CÁLCULO:")
    print("-" * 25)
    print(f"Un objeto de {masa} kg con un área de {area_proyectada} m²")
    print(f"y un coeficiente de {coef_arrastre} alcanzará una velocidad")
    print(f"terminal de {velocidad_terminal:.2f} m/s.")
    print()


def mostrar_menu() -> None:
    """
    Muestra el menú principal del programa.
    """
    print("\n" + "*" * 50)
    print("*** Biblioteca de Simulación Científica ***")
    print("*" * 50)
    print("1. Modelo Logístico de Crecimiento Poblacional (Biología)")
    print("2. Cálculo de Velocidad Terminal (Física)")
    print("3. Salir")
    print("*" * 50)


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

def main() -> None:
    """
    Función principal que controla el flujo del programa.
    
    Implementa el bucle principal del menú y llama a las funciones
    gestoras apropiadas según la selección del usuario.
    """
    print("Bienvenido a la Biblioteca de Simulación Científica")
    print("Este programa le permite realizar cálculos científicos especializados.")
    
    while True:
        try:
            # Mostrar menú y obtener opción del usuario
            mostrar_menu()
            opcion = obtener_opcion_menu()
            
            # Procesar la opción seleccionada
            if opcion == 1:
                gestionar_simulacion_poblacional()
                
            elif opcion == 2:
                gestionar_calculo_velocidad_terminal()
                
            elif opcion == 3:
                print("\n¡Gracias por usar la Biblioteca de Simulación Científica!")
                print("¡Hasta la vista!")
                break
                
            # Pausa para que el usuario pueda ver los resultados
            input("\nPresione Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            print("¡Hasta la vista!")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Por favor, intente nuevamente.")


# =============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# =============================================================================

if __name__ == "__main__":
    main()
