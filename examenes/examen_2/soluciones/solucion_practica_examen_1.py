"""
POSIBLE Solución del sistema de análisis del coeficiente de arrastre.
"""

# ==============================================================================
# MÓDULO DE NEGOCIO
# ==============================================================================

import numpy as np

# Constantes del problema
RHO_AIR = 1.225  # Densidad del aire (kg/m^3)
REF_AREA = 0.5   # Área de referencia del modelo (m^2)

def calculate_cd(F_D: np.ndarray, V: np.ndarray, rho: float = RHO_AIR, A: float = REF_AREA) -> np.ndarray:
    """
    Calcula el Coeficiente de Arrastre (CD) a partir de la fuerza y la velocidad.
    
    CD = FD / (0.5 * rho * V^2 * A)
    """
    # Término de presión dinámica: 0.5 * rho * V^2 * A
    dynamic_pressure_term = 0.5 * rho * (V**2) * A
    
    # Previene la división por cero si la velocidad fuera 0
    CD = np.divide(F_D, dynamic_pressure_term, out=np.zeros_like(F_D), where=dynamic_pressure_term!=0)
    
    return CD

def calculate_drag_force(C_D: float, V: np.ndarray, rho: float = RHO_AIR, A: float = REF_AREA) -> np.ndarray:
    """
    Calcula la Fuerza de Arrastre Teórica (FD) para un CD constante.
    
    FD = CD * 0.5 * rho * V^2 * A
    """
    return C_D * 0.5 * rho * (V**2) * A

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# FUNCIONES DE INTERACCION
# ==============================================================================

# --- 1. Función de Carga, Cálculo y Modelado ---

def process_data(file_path: str) -> tuple:
    """
    Carga, calcula el CD promedio y genera los arrays del modelo teórico.
    
    Returns:
        Tuple[pd.DataFrame, float, np.ndarray, np.ndarray]:
        (DataFrame con CD, CD_avg, V_model, F_D_model). Retorna None en caso de error.
    """
    print("1. Cargando y preparando datos...")
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado. Asegúrese de que existe.")
        return None, None, None, None

    # Preparación de arrays NumPy
    drag_forces_np = df['Drag_Force_N'].values
    velocities_np = df['Velocity_mps'].values

    # 2. Cálculo del CD y adición al DataFrame
    print("2. Calculando Coeficiente de Arrastre (CD)...")
    CD_values = calculate_cd(drag_forces_np, velocities_np)
    df['Coefficient_of_Drag'] = CD_values
    
    CD_avg: float = df['Coefficient_of_Drag'].mean()
    print(f"   -> Coeficiente de Arrastre Promedio (CD_avg): {CD_avg:.4f}")

    # 3. Generación del Modelo Teórico
    # V_model: Array de 100 puntos de velocidad para la curva teórica
    V_model = np.linspace(df['Velocity_mps'].min(), df['Velocity_mps'].max(), 100)
    
    # F_D_model: Fuerza de arrastre teórica basada en CD_avg
    F_D_model = calculate_drag_force(CD_avg, V_model)
    
    return df, CD_avg, V_model, F_D_model

# --- 2. Funciones de Visualización (una por gráfico) ---

def plot_fd_vs_v(ax: plt.Axes, df: pd.DataFrame, V_model: np.ndarray, F_D_model: np.ndarray, CD_avg: float) -> None:
    """
    Genera el Gráfico Principal (FD vs. V) en el objeto Axes (ax) dado.
    """
    # Datos Experimentales (puntos dispersos)
    ax.plot(
        df['Velocity_mps'], 
        df['Drag_Force_N'], 
        'o', 
        label='Datos Experimentales ($F_D$ Medida)',
        color='blue',
        markersize=4
    )
    
    # Curva del Modelo Teórico (línea)
    ax.plot(
        V_model, 
        F_D_model, 
        '--', 
        label=f'Modelo Teórico ($C_D \\approx {CD_avg:.4f}$)',
        color='red'
    )
    
    ax.set_title('Fuerza de Arrastre vs. Velocidad: Medido vs. Modelo Teórico')
    ax.set_xlabel('Velocidad ($V$, m/s)')
    ax.set_ylabel('Fuerza de Arrastre ($F_D$, N)')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()


def plot_cd_consistency(ax: plt.Axes, df: pd.DataFrame, CD_avg: float) -> None:
    """
    Genera el Gráfico de Consistencia (CD vs. V) en el objeto Axes (ax) dado.
    """
    # Variación del CD calculado (puntos dispersos)
    ax.plot(
        df['Velocity_mps'],
        df['Coefficient_of_Drag'],
        'x',
        label='$C_D$ por punto de prueba',
        color='green',
        markersize=5
    )
    
    # Línea horizontal del CD promedio
    ax.axhline(CD_avg, color='orange', linestyle='-', linewidth=2, label=f'Promedio de $C_D$ ({CD_avg:.4f})')
    
    ax.set_title('Consistencia del Coeficiente de Arrastre ($C_D$)')
    ax.set_xlabel('Velocidad ($V$, m/s)')
    ax.set_ylabel('$C_D$')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()

# --- 3. Función Principal de Ejecución ---

def main() -> None:
    """
    Función principal que orquesta el flujo de trabajo y gestiona los subplots.
    """
    file_path = 'wind_tunnel_data.csv'
    
    # Desempaquetado con Type Hint
    df, CD_avg, V_model, F_D_model = process_data(file_path)
    
    # Verificación de datos
    if df is not None and CD_avg is not None and V_model is not None and F_D_model is not None:
        print("4. Generando visualizaciones...")
        
        # La tupla de retorno contiene la Figura y un array de los objetos Axes.
        fig, ax_array = plt.subplots(nrows=2, ncols=1, figsize=(10, 8)) 
        
        # Llamamos a las funciones de visualización, pasando los objetos Axes.
        # ax_array[0] es el eje superior (primera fila).
        ax1 = ax_array[0]
        plot_fd_vs_v(ax1, df, V_model, F_D_model, CD_avg)
        
        # ax_array[1] es el eje inferior (segunda fila).
        ax2 = ax_array[1]
        plot_cd_consistency(ax2, df, CD_avg)
        
        # 3. Ajustamos el diseño y mostramos.
        fig.tight_layout()
        plt.show()
        
main()
