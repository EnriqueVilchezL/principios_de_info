"""
POSIBLE Solución del sistema de análisis de materiales.
"""

# ==============================================================================
# MÓDULO DE NEGOCIO
# ==============================================================================

import numpy as np

def calcular_delta(w: np.ndarray, L: float, E: float, I: float) -> np.ndarray:
    """
    Calcula la deflexión máxima (delta) para una viga simplemente apoyada con carga uniforme.
    delta = (5 * w * L^4) / (384 * E * I)
    """
    numerator = 5 * w * (L**4)
    denominator = 384 * E * I
    # Se usa np.divide para manejar la posibilidad de w=0 sin errores si se implementara fuera del linspace.
    return np.divide(numerator, denominator, out=np.zeros_like(w), where=denominator!=0)

def calcular_carga_limite(delta_limite: float, L: float, E: float, I: float) -> float:
    """
    Calcula la carga máxima admisible (w_max) que la viga puede soportar.
    w_max = (384 * E * I * delta_limite) / (5 * L^4)
    """
    numerator = 384 * E * I * delta_limite
    denominator = 5 * (L**4)
    return numerator / denominator

def calcular_delta_limite(L: float) -> float:
    """
    Calcula el límite de deflexión permisible basado en la longitud de la viga.
    delta_limite = L / 360
    """
    return L / 360

# ==============================================================================
# FUNCIONES DE INTERACCION
# ==============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- PARÁMETROS DE DISEÑO FIJOS ---
L: float = 12.0                  # Longitud de la viga (m)
I: float = 1.5e-4                # Momento de Inercia (m^4)
E_A: float = 200e9               # Módulo de Elasticidad - Acero A (Pa)
E_B: float = 180e9               # Módulo de Elasticidad - Acero B (Pa)

def generate_interactive_data() -> pd.DataFrame:
    """
    Solicita el número de muestras y el porcentaje de ruido para cada punto de carga, 
    generando el DataFrame de datos experimentales simulados.
    """
    
    # 1. Solicitar Número de Muestras
    valido = False
    while not valido:
        try:
            N = int(input("Ingrese el número de muestras (N) a simular (ej: 10): "))
            if N > 0:
                valido = True
            else:
                print("El número de muestras debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")
    
    # 2. Generación de Cargas Base (5,000 N/m a 35,000 N/m)
    cargas_w_np = np.linspace(1000, 5000, N)
    
    cargas_medidas = []
    deflexiones_medidas = []
    
    print("\n--- INICIO DE SIMULACIÓN INTERACTIVA ---")
    
    # 3. Simulación Interactiva y Carga
    for i, w_i in enumerate(cargas_w_np):
        # Cálculo de Deflexión Teórica para Acero A
        delta_teorica = calcular_delta(np.array([w_i]), L, E_A, I)[0]
        
        valido = False
        while not valido:
            try:
                # Solicitar porcentaje de ruido
                ruido_porcentaje = float(input(f"Muestra {i+1}/{N} (Carga: {w_i:.0f} N/m). Ingrese % max ruido (ej: 5.0): "))
                if ruido_porcentaje >= 0:
                    valido = True
                else:
                    print("El porcentaje debe ser positivo.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número decimal.")
        
        # Generar ruido aleatorio (uniforme entre -% y +%)
        # El ruido se calcula como el porcentaje ingresado del valor teórico.
        max_ruido_abs = (ruido_porcentaje / 100.0) * delta_teorica
        ruido = np.random.uniform(-max_ruido_abs, max_ruido_abs)
        
        # Cálculo de Deflexión Medida
        delta_medida = delta_teorica + ruido
        
        # Recolección de datos
        cargas_medidas.append(w_i)
        deflexiones_medidas.append(delta_medida)

    print("--- SIMULACIÓN COMPLETADA ---")
    
    # 4. Creación del DataFrame
    data = {
        'Test_ID': np.arange(1, N + 1),
        'Carga_w_Nm': cargas_medidas,
        'Deflexion_medida_m': deflexiones_medidas
    }
    df = pd.DataFrame(data)
    return df


def perform_analysis(df: pd.DataFrame) -> tuple:
    """
    Realiza la validación experimental y calcula las cargas límite (w_max).
    """
    print("\n2. Validación y Cálculo de Cargas Límite...")
    
    # --- Validación Experimental (Acero A) ---
    w_np = df['Carga_w_Nm'].values
    
    # Deflexión Teórica para Acero A (NumPy vectorizado)
    delta_A_teorica = calcular_delta(w_np, L, E_A, I)
    df['Delta_A_Teorica_m'] = delta_A_teorica
    
    # Cálculo del error promedio porcentual
    delta_medida_np = df['Deflexion_medida_m'].values
    # El error se calcula solo si la deflexión teórica es diferente de cero (lo cual es cierto aquí)
    error_porcentual = np.abs(delta_medida_np - delta_A_teorica) / delta_A_teorica * 100
    avg_error = np.mean(error_porcentual)
    
    print(f"   -> Error promedio del modelo teórico vs. experimento: {avg_error:.2f}%")
    
    # --- Cálculo de Cargas Límite ---
    delta_limite = calcular_delta_limite(L)
    w_max_A = calcular_carga_limite(delta_limite, L, E_A, I)
    w_max_B = calcular_carga_limite(delta_limite, L, E_B, I)
    
    print(f"   -> Delta Límite ($\\delta_{{limite}}$): {delta_limite * 1000:.2f} mm")
    print(f"   -> Carga Máxima Admisible: Acero A = {w_max_A:.0f} N/m ({w_max_A/1000:.1f} kN/m)")
    print(f"   -> Carga Máxima Admisible: Acero B = {w_max_B:.0f} N/m ({w_max_B/1000:.1f} kN/m)")
    
    return w_max_A, w_max_B, avg_error, delta_limite


def plot_comparative_analysis(df: pd.DataFrame, w_max_A: float, w_max_B: float, delta_limite: float) -> None:
    """
    Genera el gráfico comparativo de Deflexión vs. Carga.
    """
    print("\n3. Generando gráfico comparativo...")
    
    # Rango de carga para el modelado (hasta w_max_A con un margen)
    W_test = np.linspace(1000, 5000, len(df))
    
    # Curvas Teóricas
    delta_A = calcular_delta(W_test, L, E_A, I)
    delta_B = calcular_delta(W_test, L, E_B, I)
    
    # Crear Figura y Ejes
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # --- Gráfico de Datos y Curvas ---
    
    # Curva 1: Acero A (Teórica)
    ax.plot(W_test / 1000, delta_A * 1000, 
            label=f'Modelo Teórico (Acero A, E={E_A:.0e} Pa)', 
            color='blue', linewidth=2)
    
    # Curva 2: Acero B (Teórica)
    ax.plot(W_test / 1000, delta_B * 1000, 
            label=f'Modelo Teórico (Acero B, E={E_B:.0e} Pa)', 
            color='orange', linewidth=2)
    
    # Datos Experimentales Simulados (puntos dispersos)
    ax.scatter(df['Carga_w_Nm'] / 1000, df['Deflexion_medida_m'] * 1000, 
               label='Datos Experimentales Simulados (Acero A)', 
               color='darkblue', marker='x', alpha=0.7)
    
    # --- Gráfico de Límites ---
    
    # Línea Horizontal: Límite de Deflexión (L/360)
    ax.axhline(delta_limite * 1000, color='red', linestyle='-', linewidth=2, 
               label=f'Límite $\\delta_{{limite}}$ ({delta_limite * 1000:.2f} mm)')
    
    # Líneas Verticales: Cargas Máximas (w_max)
    ax.axvline(w_max_A / 1000, color='blue', linestyle='--', alpha=0.6, 
               label=f'$w_{{max}}$ (Acero A) = {w_max_A / 1000:.1f} kN/m')
    ax.axvline(w_max_B / 1000, color='orange', linestyle='--', alpha=0.6, 
               label=f'$w_{{max}}$ (Acero B) = {w_max_B / 1000:.1f} kN/m')

    # --- Configuración Final ---
    ax.set_title(f'Comparación de Materiales y Carga Límite ($\\delta$ vs. Carga)')
    ax.set_xlabel('Carga Distribuida ($w$, kN/m)')
    ax.set_ylabel('Deflexión Máxima ($\\delta$, mm)')
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.legend(loc='upper left')
    ax.set_ylim(bottom=0)
    
    fig.tight_layout()
    plt.show()


def main():
    # 1. Generar datos de forma interactiva
    df_data = generate_interactive_data()
    
    # 2. Realizar el análisis y cálculos
    w_max_A, w_max_B, avg_error, delta_limite = perform_analysis(df_data)
    
    # 3. Visualizar resultados
    plot_comparative_analysis(df_data, w_max_A, w_max_B, delta_limite)
    
    print("\nAnálisis de Comparación de Materiales y Carga Límite Completado.")

main()
