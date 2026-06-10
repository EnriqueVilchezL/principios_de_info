"""
POSIBLE Solución del sistema de simulación del intercambiador de calor.
"""

# ==============================================================================
# MÓDULO DE NEGOCIO
# ==============================================================================

import numpy as np
import pandas as pd

def simular_intercambiador_T_h(U: float, L_TOTAL: float, T_H_I: float, T_C_I: float, M_DOT_H: float, C_P_H: float, P: float, NUM_POINTS: int) -> pd.DataFrame:
    """
    Simula el perfil de temperatura de un fluido caliente en un intercambiador
    de calor para un Coeficiente Global de Transferencia (U) dado.

    Args:
        U (float): Coeficiente Global de Transferencia de Calor [W/(m^2·K)].

    Returns:
        pd.DataFrame: DataFrame con la longitud (x) y la temperatura (Th)
                      para el U proporcionado.
    """
    
    # 1. Generar vector de Longitud (x) usando NumPy
    # Vector de 100 puntos uniformemente espaciados de 0 a L_TOTAL
    x_vector: np.ndarray = np.linspace(0, L_TOTAL, NUM_POINTS)

    # 2. Calcular la Constante de Transferencia (K)
    # K = (U * P) / (m_dot_h * C_p_h)
    # Se realiza el cálculo con punto flotante explícito
    K: float = (U * P) / (M_DOT_H * C_P_H)

    # 3. Calcular el vector de Temperaturas (T_h) usando NumPy
    # Th(x) = T_c_i + (T_h_i - T_c_i) * exp(-K * x)
    temp_diff: float = T_H_I - T_C_I
    
    # Aplicación vectorizada de la fórmula
    T_h_vector: np.ndarray = T_C_I + temp_diff * np.exp(-K * x_vector)

    # 4. Crear y devolver el DataFrame de Pandas
    data = {
        'Longitud_x (m)': x_vector,
        'Temperatura_Th (K)': T_h_vector
    }
    return pd.DataFrame(data)

# ==============================================================================
# FUNCIONES DE INTERACCION
# ==============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Definición de las constantes fijas del sistema
L_TOTAL: float = 5.0
T_H_I: float = 360.0
T_C_I: float = 300.0
M_DOT_H: float = 0.5
C_P_H: float = 4180.0
P: float = 0.15
NUM_POINTS: int = 100

# Lista de escenarios U a simular
ESCENARIOS_U: list[float] = [150.0, 300.0, 450.0]

# Variable global para almacenar el DataFrame maestro. Inicialmente es None.
maestro_df: pd.DataFrame | None = None

def realizar_simulacion_y_analisis() -> None:
    """
    Ejecuta la simulación para todos los escenarios, estructura los datos,
    realiza el análisis crítico e imprime el gráfico.
    """
    global maestro_df

    print("\n[INICIANDO] Simulación del Perfil de Temperatura para U=150, 300, y 450 W/(m^2·K)...")

    # Lista para almacenar los DataFrames de cada escenario
    dfs_simulacion: list[pd.DataFrame] = []

    # 2. Ejecución de la función para cada escenario U
    for i, u_val in enumerate(ESCENARIOS_U):
        # Simula y obtiene el DataFrame para el U actual, pasando todos los parámetros
        df_temp: pd.DataFrame = simular_intercambiador_T_h(
            u_val, L_TOTAL, T_H_I, T_C_I, M_DOT_H, C_P_H, P, NUM_POINTS
        )
        
        # Renombrar la columna de temperatura para la fusión
        col_name: str = f'Th_U{int(u_val)}'
        df_temp.rename(columns={'Temperatura_Th (K)': col_name}, inplace=True)
        
        # Guardar solo las columnas de interés
        if i == 0:
            # Para el primer DF, guardar la longitud
            dfs_simulacion.append(df_temp[['Longitud_x (m)', col_name]])
        else:
            # Para los siguientes, solo la columna de temperatura
            dfs_simulacion.append(df_temp[[col_name]])

    # Combinar los DataFrames en un único DataFrame maestro
    maestro_df = pd.concat(dfs_simulacion, axis=1)

    # Imprimir DataFrame Maestro (Fragmento)
    print("\n### DataFrame Maestro de Perfiles de Temperatura (Fragmento) ###")
    print(maestro_df.head(3).to_string(index=False, float_format='%.3f'))
    print("...")
    print(maestro_df.tail(2).to_string(index=False, float_format='%.3f'))

    # 3. Análisis de Resultados (Temperaturas Críticas)
    
    # Extraer la fila final (x = L_TOTAL) para obtener las temperaturas de salida
    ultima_fila: pd.Series = maestro_df.iloc[-1]
    
    resumen_data: dict = {
        "Escenario (U)": [],
        "Temperatura Salida (Th,o) [K]": [],
        "Caída de Temperatura Total (ΔT total) [K]": []
    }
    
    print("\n### Análisis de Resultados (Temperaturas Críticas) ###")
    
    for u_val in ESCENARIOS_U:
        col_name: str = f'Th_U{int(u_val)}'
        
        # Temperatura de Salida (Th_o)
        T_h_o: float = ultima_fila[col_name]
        
        # Caída de Temperatura Total (Delta T)
        delta_T_total: float = T_H_I - T_h_o
        
        # Llenar el diccionario de resumen
        resumen_data["Escenario (U)"].append(f'U{int(u_val)}')
        resumen_data["Temperatura Salida (Th,o) [K]"].append(f'{T_h_o:.3f}')
        resumen_data["Caída de Temperatura Total (ΔT total) [K]"].append(f'{delta_T_total:.3f}')

    # Crear el DataFrame de resumen y imprimirlo (sustituyendo tabulate)
    resumen_df = pd.DataFrame(resumen_data)
    # Usar to_string para imprimir el DF completo sin truncar y con alineación
    print(resumen_df.to_string(index=False))

    # 4. Visualización Comparativa (Matplotlib)
    print("\n[GRÁFICO] Generando y mostrando el gráfico comparativo (Matplotlib)...")
    
    # Crear la figura y los ejes
    plt.figure(figsize=(10, 6))
    
    # Trazar las tres curvas de temperatura
    for u_val in ESCENARIOS_U:
        col_name: str = f'Th_U{int(u_val)}'
        plt.plot(
            maestro_df['Longitud_x (m)'], 
            maestro_df[col_name], 
            label=f'U = {int(u_val)} W/(m²·K)'
        )
    
    # Línea horizontal de referencia (Límite Termodinámico)
    plt.axhline(
        y=T_C_I, 
        color='r', 
        linestyle='--', 
        linewidth=1, 
        label=f'Límite T_c,i ({T_C_I} K)'
    )
    
    # Configuración del gráfico
    plt.title('Perfil de Temperatura del Fluido Caliente vs. Longitud')
    plt.xlabel('Longitud del Intercambiador, x [metros]')
    plt.ylabel('Temperatura del Fluido Caliente, Th [K]')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='Coeficiente U')
    
    # Mostrar el gráfico
    plt.show()

    print("[ÉXITO] Simulación y análisis completados. Datos listos para guardar.")

def guardar_resultados_csv() -> None:
    """
    Solicita el nombre del archivo y guarda el DataFrame maestro con manejo de errores.
    """
    global maestro_df
    
    # Verificar la dependencia: Si la simulación no se ha ejecutado
    if maestro_df is None:
        print("\n[ERROR] Debe ejecutar primero la Opción 1 para generar la simulación. Datos no disponibles.")
        return

    # Solicitar el nombre del archivo
    print("\nSeleccione la Opción 2 para Guardar Resultados.")
    
    try:
        # Nota: En un entorno de examen interactivo real, esto sería una entrada de usuario.
        filename: str = input("Ingrese el nombre del archivo (.csv): ")
    except Exception as e:
        print(f"[ERROR de entrada] No se pudo leer la entrada: {e}")
        return

    # 2. Bloque try...except para la protección del proceso de guardado
    try:
        # Verificar que la extensión sea correcta o añadirla
        if not filename.lower().endswith('.csv'):
            filename += '.csv'
            
        # Intento de guardar el DataFrame
        maestro_df.to_csv(filename, index=False, float_format='%.3f')
        print(f"[ÉXITO] Resultados guardados en {filename}.")
        
    except FileNotFoundError:
        # Captura errores comunes de I/O, como una ruta no válida o permisos
        print(f"[ERROR al guardar] No se pudo escribir el archivo. Verifique la ruta y los permisos. (Excepción capturada: la ruta especificada no existe).")
    except PermissionError:
        print(f"[ERROR al guardar] No se pudo escribir el archivo. Verifique la ruta y los permisos. (Excepción capturada: Permiso denegado en el sistema operativo).")
    except Exception as e:
        # Captura cualquier otra excepción
        print(f"[ERROR al guardar] Ocurrió un error inesperado al guardar: {e}")


def main() -> None:
    """
    Función principal que gestiona el menú del programa.
    """
    terminar = False
    while not terminar:
        print("\n--- Analizador de Intercambiadores de Calor ---")
        print("1. Realizar Simulación (Generar Datos y Gráfico)")
        print("2. Guardar Resultados en Archivo CSV")
        print("3. Salir")
        
        # Simulación de la entrada del usuario (en un entorno real, usaría input())
        try:
            opcion: str = input("Seleccione una opción: ")
            
            if opcion == '1':
                realizar_simulacion_y_analisis()
            elif opcion == '2':
                guardar_resultados_csv()
            elif opcion == '3':
                print("\nSaliendo del programa.")
                terminar = True
            else:
                print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
        
        except KeyboardInterrupt:
            print("\nOperación interrumpida por el usuario. Saliendo.")
            terminar = True
        except Exception as e:
            print(f"Ocurrió un error inesperado en el menú: {e}")

main()
