"""
POSIBLE Solución del sistema de gestión de flota de transporte.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# --- Constantes y Parámetros ---
BBL_TO_GAL = 42
COSTO_BASE_GALON = 1500
COLUMN_NAMES = ['Tipo_de_registro', 'ID_o_Transportista', 'Nombre_o_Carga', 'Distancia_o_Capacidad_o_Deposito_1', 'Deposito_2']
SEPARATOR = ','

# --- 1. Funciones de Conversión y Utilidad ---

def parse_bbl_gal_to_galones(bbl_gal_str: str) -> float:
    """Convierte una cadena 'BB/GG' (Barriles/Galones) a Galones Totales.

    Args:
        bbl_gal_str (str): Cadena que contiene la carga en formato 'BB/GG'.

    Returns:
        float: Volumen total en galones. Retorna 0.0 si el formato es inválido o GG >= 42.
    """
    try:
        bb, gg = map(int, bbl_gal_str.split('/'))
        if gg >= BBL_TO_GAL:
             return 0.0 
        return (bb * BBL_TO_GAL) + gg
    except ValueError:
        return 0.0

def parse_bbl_gal_to_barriles(bbl_gal_str: str) -> float:
    """Convierte una cadena 'BB/GG' (Barriles/Galones) a Barriles Totales.

    Args:
        bbl_gal_str (str): Cadena que contiene la capacidad/carga en formato 'BB/GG'.

    Returns:
        float: Volumen total en barriles base. Retorna 0.0 si el formato es inválido.
    """
    try:
        bb, gg = map(int, bbl_gal_str.split('/'))
        return bb + (gg / BBL_TO_GAL)
    except ValueError:
        return 0.0

def cargar_datos(filename: str) -> tuple:
    """Carga, separa y limpia el archivo único en tres DataFrames (Depósito, Transportista, Flete).

    Args:
        filename (str): Nombre del archivo CSV a cargar.

    Returns:
        tuple: DataFrames con datos limpios de depósitos, transportistas y fletes.
    """
    if not os.path.exists(filename):
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    try:
        df = pd.read_csv(filename, sep=SEPARATOR, header=None, dtype=str, names=COLUMN_NAMES)
        
        df_deposito = df[df['Tipo_de_registro'] == 'deposito'].copy().reset_index(drop=True)
        df_transpor = df[df['Tipo_de_registro'] == 'transpor'].copy().reset_index(drop=True)
        df_flete = df[df['Tipo_de_registro'] == 'flete'].copy().reset_index(drop=True)
        
        # --- Limpieza y Conversión ---
        
        df_deposito.rename(columns={'ID_o_Transportista': 'ID', 'Nombre_o_Carga': 'Nombre', 
                                    'Distancia_o_Capacidad_o_Deposito_1': 'Distancia_km'}, inplace=True)
        df_deposito['ID'] = pd.to_numeric(df_deposito['ID'], errors='coerce', downcast='integer')
        df_deposito['Distancia_km'] = pd.to_numeric(df_deposito['Distancia_km'], errors='coerce')

        df_transpor.rename(columns={'ID_o_Transportista': 'ID', 'Nombre_o_Carga': 'Nombre', 
                                    'Distancia_o_Capacidad_o_Deposito_1': 'Capacidad_BblGal'}, inplace=True)
        df_transpor['ID'] = pd.to_numeric(df_transpor['ID'], errors='coerce', downcast='integer')
        df_transpor['Capacidad_Bbl_Base'] = df_transpor['Capacidad_BblGal'].apply(parse_bbl_gal_to_barriles)
        df_transpor['Capacidad_Galones'] = df_transpor['Capacidad_BblGal'].apply(parse_bbl_gal_to_galones)
        
        df_flete.rename(columns={'ID_o_Transportista': 'ID_Transpor', 'Nombre_o_Carga': 'Carga_BblGal', 
                                 'Distancia_o_Capacidad_o_Deposito_1': 'Dep_ID_1', 'Deposito_2': 'Dep_ID_2'}, inplace=True)
        df_flete['ID_Transpor'] = pd.to_numeric(df_flete['ID_Transpor'], errors='coerce', downcast='integer')
        df_flete['Dep_ID_1'] = pd.to_numeric(df_flete['Dep_ID_1'], errors='coerce', downcast='integer')
        df_flete['Dep_ID_2'] = pd.to_numeric(df_flete['Dep_ID_2'], errors='coerce', downcast='integer').fillna(0).astype(int)
        df_flete['Galones_Totales'] = df_flete['Carga_BblGal'].apply(parse_bbl_gal_to_galones)

        return df_deposito, df_transpor, df_flete
        
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

def escribir_registro(filename: str, registro: str) -> None:
    """Añade una línea de registro al archivo CSV.

    Args:
        filename (str): Nombre del archivo CSV.
        registro (str): Línea de texto a añadir, separada por coma.
    """
    try:
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            with open(filename, 'w') as f:
                f.write(SEPARATOR.join(COLUMN_NAMES)) 
        
        with open(filename, 'a') as f:
            f.write("\n" + registro)
        print(f"(Registro '{registro}' añadido al archivo.)")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

# --- 2. Funciones de Cálculo Centralizado (P, E, G) ---

def calcular_pagos_df(df_flete: pd.DataFrame, df_transpor: pd.DataFrame, df_deposito: pd.DataFrame) -> pd.DataFrame:
    """Calcula el Factor de Ajuste (F_ajuste) y el Pago para cada flete usando NumPy.

    Args:
        df_flete (pd.DataFrame): DataFrame con los registros de fletes.
        df_transpor (pd.DataFrame): DataFrame con los registros de transportistas.
        df_deposito (pd.DataFrame): DataFrame con los registros de depósitos.

    Returns:
        pd.DataFrame: DataFrame de fletes con columnas añadidas para D_promedio, F_ajuste y Pago.
    """
    if df_flete.empty or df_transpor.empty or df_deposito.empty:
        return pd.DataFrame()

    df_merge = df_flete.merge(df_transpor[['ID', 'Nombre', 'Capacidad_Bbl_Base']], 
                              left_on='ID_Transpor', right_on='ID', suffixes=('_flete', '_transpor'))
    
    distancias = df_deposito.set_index('ID')['Distancia_km']
    
    def get_distancia_vec(dep_id: np.ndarray) -> np.ndarray:
        """Función vectorizada para buscar distancias en el DF de depósitos."""
        return np.where(dep_id != 0, distancias.reindex(dep_id).fillna(0).values, 0.0)

    dep_id_1_np = df_merge['Dep_ID_1'].values
    dep_id_2_np = df_merge['Dep_ID_2'].values

    distancias_1 = get_distancia_vec(dep_id_1_np)
    distancias_2 = get_distancia_vec(dep_id_2_np)
    
    # 1. Distancia Promedio (D_promedio)
    divisor = np.where(dep_id_2_np != 0, 2.0, 1.0)
    df_merge['D_promedio'] = (distancias_1 + distancias_2) / divisor

    # 2. Factor de Ajuste (F_ajuste): 1 + (D_promedio / C_base)
    C_base = df_merge['Capacidad_Bbl_Base'].values
    D_promedio = df_merge['D_promedio'].values
    F_ajuste = 1 + np.divide(D_promedio, C_base, out=np.ones_like(D_promedio), where=C_base!=0)
    df_merge['F_ajuste'] = F_ajuste
    
    # 3. Pago del Flete: Galones Totales * 1500 * F_ajuste
    Galones_Totales = df_merge['Galones_Totales'].values
    df_merge['Pago'] = Galones_Totales * COSTO_BASE_GALON * F_ajuste
    
    return df_merge

# --- 3. Implementación de Opciones de Menú (Funciones operativas) ---

def opcion_deposito(filename: str) -> None:
    """Implementa la opción D: Registra un nuevo depósito receptor."""
    print("\n--- REGISTRAR NUEVO DEPÓSITO ---")
    try:
        id_deposito = int(input("Identificador (ID): "))
        nombre = input("Nombre: ")
        distancia = float(input("Distancia (km): "))
    except ValueError:
        print("ERROR: ID o Distancia deben ser valores numéricos. Cancelando.")
        return
    registro = f"deposito{SEPARATOR}{id_deposito}{SEPARATOR}{nombre}{SEPARATOR}{distancia}"
    escribir_registro(filename, registro)

def opcion_transpor(filename: str) -> None:
    """Implementa la opción T: Registra un nuevo transportista."""
    print("\n--- REGISTRAR NUEVO TRANSPORTISTA ---")
    try:
        id_transpor = int(input("Identificador (ID): "))
        nombre = input("Nombre: ")
        capacidad = input("Capacidad camión (Bbl/Gal, ej: 400/0): ")
        if parse_bbl_gal_to_galones(capacidad) <= 0:
            print("ERROR: Capacidad en formato Bbl/Gal inválida o cero. Cancelando.")
            return
    except ValueError:
        print("ERROR: ID debe ser un valor numérico. Cancelando.")
        return
    registro = f"transpor{SEPARATOR}{id_transpor}{SEPARATOR}{nombre}{SEPARATOR}{capacidad}"
    escribir_registro(filename, registro)

def opcion_flete(filename: str, df_transpor: pd.DataFrame, df_deposito: pd.DataFrame) -> None:
    """Implementa la opción F: Registra un nuevo viaje de entrega (flete)."""
    print("\n--- REGISTRAR NUEVO FLETE ---")
    try:
        id_transpor = int(input("ID Transportista: "))
        if id_transpor not in df_transpor['ID'].values:
            print("ERROR: ID de transportista no existe. Cancelando.")
            return

        carga_bbl_gal = input("Combustible transportado (Bbl/Gal, ej: 40/20): ")
        if parse_bbl_gal_to_galones(carga_bbl_gal) <= 0:
            print("ERROR: Carga inválida o formato incorrecto (BB/GG). Cancelando.")
            return

        dep_id_1 = int(input("Depósito 1 (ID): "))
        if dep_id_1 not in df_deposito['ID'].values:
            print("ERROR: ID de depósito 1 no existe. Cancelando.")
            return
            
        dep_id_2 = int(input("Depósito 2 (ID, 0 si no aplica): "))
        if dep_id_2 != 0 and dep_id_2 not in df_deposito['ID'].values:
            print("ERROR: ID de depósito 2 no existe (y no es 0). Cancelando.")
            return

    except ValueError:
        print("ERROR: Las IDs o la carga deben ser valores numéricos. Cancelando.")
        return

    registro = f"flete{SEPARATOR}{id_transpor}{SEPARATOR}{carga_bbl_gal}{SEPARATOR}{dep_id_1}{SEPARATOR}{dep_id_2}"
    escribir_registro(filename, registro)

def opcion_pago(df_flete: pd.DataFrame, df_transpor: pd.DataFrame, df_deposito: pd.DataFrame) -> None:
    """Implementa la opción P: Reporte de pagos pendientes a transportistas."""
    if df_flete.empty:
        print("No hay fletes registrados para calcular pagos.")
        return

    df_pago_calc = calcular_pagos_df(df_flete.copy(), df_transpor, df_deposito)
    
    if df_pago_calc.empty:
        print("No se pudo calcular el pago. Verifique si los datos de depósito/transportista están completos.")
        return

    print("\n--- REPORTE DE PAGOS PENDIENTES ---")
    
    reporte_pago = df_pago_calc.groupby(['ID_Transpor', 'Nombre_transpor'])['Pago'].sum().reset_index()
    
    for _, row in reporte_pago.iterrows():
        # Formato de moneda con separador de miles
        pago_formato = f"{row['Pago']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        print(f"{int(row['ID_Transpor']):<3} {row['Nombre_transpor']:<10}: {pago_formato} Colones")

def opcion_atencion(df_flete: pd.DataFrame, df_deposito: pd.DataFrame) -> None:
    """Implementa la opción A: Reporte de depósitos no visitados (pendientes de atención)."""
    if df_deposito.empty:
        print("No hay depósitos registrados.")
        return

    print("\n--- DEPÓSITOS PENDIENTES DE ATENCIÓN ---")
    
    all_depot_ids = set(df_deposito['ID'].values)
    
    if df_flete.empty:
        visited_ids = set()
    else:
        # IDs visitados (Dep_ID_1 y Dep_ID_2 > 0)
        visited_ids_1 = set(df_flete['Dep_ID_1'].unique())
        visited_ids_2 = set(df_flete[df_flete['Dep_ID_2'] > 0]['Dep_ID_2'].unique())
        visited_ids = visited_ids_1.union(visited_ids_2)
        
    pending_ids = sorted(list(all_depot_ids - visited_ids))
    
    if pending_ids:
        for dep_id in pending_ids:
            nombre = df_deposito[df_deposito['ID'] == dep_id]['Nombre'].iloc[0]
            print(f"- {dep_id}: {nombre}")
    else:
        print("(Ninguno - Todos los depósitos fueron visitados)")

def opcion_estadisticas(df_flete: pd.DataFrame, df_transpor: pd.DataFrame, df_deposito: pd.DataFrame) -> None:
    """Implementa la opción E: Muestra métricas de fletes usando NumPy y Pandas."""
    if df_flete.empty:
        print("No hay fletes registrados para estadísticas.")
        return

    df_pago_calc = calcular_pagos_df(df_flete.copy(), df_transpor, df_deposito)
    if df_pago_calc.empty:
        print("No se pudo calcular la estadística. Verifique si los datos de depósito/transportista están completos.")
        return

    print("\n--- ESTADÍSTICAS DE FLOTA (NumPy/Pandas) ---")
    
    # 1. Carga Promedio por Viaje
    media_carga = df_pago_calc['Galones_Totales'].mean()
    std_carga = df_pago_calc['Galones_Totales'].std()
    print("\n1. Carga Promedio por Viaje:")
    print(f"   - Media: {media_carga:.2f} Galones")
    print(f"   - Desviación Estándar: {std_carga:.2f} Galones")
    
    # 2. Eficiencia de Ruta (Factor de Ajuste)
    media_f_ajuste = df_pago_calc['F_ajuste'].mean()
    varianza_f_ajuste = np.var(df_pago_calc['F_ajuste'].values)
    print("\n2. Eficiencia de Ruta (Factor de Ajuste):")
    print(f"   - Media (F_ajuste): {media_f_ajuste:.3f}")
    print(f"   - Varianza (F_ajuste): {varianza_f_ajuste:.5f} (NumPy)")

    # 3. Top 3 Transportistas por Capacidad
    top_3 = df_transpor.sort_values(by='Capacidad_Galones', ascending=False).head(3)
    print("\n3. Top 3 Transportistas por Capacidad (en Galones):")
    for _, row in top_3.iterrows():
        print(f"   - {int(row['ID'])} {row['Nombre']}: {row['Capacidad_Galones']:.1f} Galones")

def opcion_grafico(df_flete: pd.DataFrame, df_transpor: pd.DataFrame, df_deposito: pd.DataFrame) -> None:
    """Implementa la opción G: Genera un gráfico de dispersión con Matplotlib."""
    if df_flete.empty:
        print("No hay fletes registrados para graficar.")
        return
        
    df_graph = calcular_pagos_df(df_flete.copy(), df_transpor, df_deposito)

    if df_graph.empty:
        print("No se pudo calcular el gráfico. Verifique si los datos de depósito/transportista están completos.")
        return

    print("\n--- VISUALIZACIÓN (Matplotlib) ---")
    df_graph['Costo_Ajustado_x_Galon'] = COSTO_BASE_GALON * df_graph['F_ajuste']

    fig, ax = plt.subplots(figsize=(10, 6))
    
    scatter = ax.scatter(df_graph['Galones_Totales'], df_graph['Costo_Ajustado_x_Galon'], 
                         c=df_graph['F_ajuste'], cmap='plasma', alpha=0.8, edgecolors='k')
    
    ax.axhline(COSTO_BASE_GALON, color='r', linestyle='--', linewidth=2, 
               label=f'Costo Base ({COSTO_BASE_GALON} Col/Gal)')

    ax.set_title('Relación entre Carga Transportada y Costo Ajustado por Galón')
    ax.set_xlabel('Combustible Transportado (Galones)')
    ax.set_ylabel('Costo por Galón Ajustado (Colones/Gal)')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()
    
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label('Factor de Ajuste (F_ajuste)')
    
    plt.tight_layout()
    plt.show()

# --- Función Principal de Ejecución ---

def main():
    """Función principal que maneja el flujo del programa y el menú interactivo."""
    print("--- INICIO DEL SISTEMA DE GESTIÓN DE FLOTA ---")
    filename = input("Por favor, ingrese el nombre del archivo de transporte (ej: transportes.csv): ")
    
    df_deposito, df_transpor, df_flete = cargar_datos(filename)
    
    if df_deposito.empty and df_transpor.empty and df_flete.empty:
        print(f"ADVERTENCIA: No se pudo cargar ningún dato desde '{filename}'. Se creará un archivo si se registra un dato.")
    else:
        print(f"Datos cargados exitosamente desde '{filename}': {len(df_deposito)} Depósitos, {len(df_transpor)} Transportistas, {len(df_flete)} Fletes.")

    # Menú Principal
    comando = ''
    while comando != 'S':
        # Recargar datos en cada iteración para incluir nuevos registros
        df_deposito, df_transpor, df_flete = cargar_datos(filename)
        
        print("\n" + "="*50)
        comando = input("Menú [D/T/F/A/P/E/G/S]: ").upper()
        print("="*50)

        if comando == 'D':
            opcion_deposito(filename)
        elif comando == 'T':
            opcion_transpor(filename)
        elif comando == 'F':
            opcion_flete(filename, df_transpor, df_deposito)
        elif comando == 'A':
            opcion_atencion(df_flete, df_deposito)
        elif comando == 'P':
            opcion_pago(df_flete, df_transpor, df_deposito)
        elif comando == 'E':
            opcion_estadisticas(df_flete, df_transpor, df_deposito)
        elif comando == 'G':
            opcion_grafico(df_flete, df_transpor, df_deposito)
        elif comando == 'S':
            print("Finalizando el programa. ¡Adiós!")
        else:
            print("Comando no reconocido. Intente de nuevo.")

main()
