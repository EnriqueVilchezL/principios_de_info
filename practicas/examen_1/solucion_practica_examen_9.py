# ----------------------------------------------------------------------
# MODULO DE CODIGO MORSE
# ----------------------------------------------------------------------
ESTADO = {
    'texto_original': None, 
    'morse_codificado': None
}

# Mapa de caracteres a código Morse
MAPA_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

# Mapeo inverso para la decodificación
MAPA_TEXTO = {}
for letra, codigo in MAPA_MORSE.items():
    MAPA_TEXTO[codigo] = letra

# --------------------------------------------
# FUNCIONES DE MANIPULACIÓN DEL ESTADO GLOBAL
# --------------------------------------------

def normalizar_y_codificar(mensaje_texto: str) -> str:
    """
    Normaliza el mensaje de texto (a mayúsculas) y lo codifica a código Morse.

    Esta función también actualiza el estado global con el texto limpio y el código Morse generado.
    Cumple con las Tareas 3 (Normalización) y 4 (Codificación).

    Args:
        mensaje_texto: El mensaje de texto ingresado por el usuario.

    Returns:
        str: El mensaje codificado en código Morse, donde las letras están 
             separadas por espacios y las palabras por " / ".
    """
    # 1. Normalización: Mayúsculas
    texto_normalizado = mensaje_texto.upper()
    
    # 2. Codificación
    palabras_morse = []
    
    # Se procesa palabra por palabra
    for palabra in texto_normalizado.split():
        letras_morse = []
        
        # Se procesa carácter por carácter
        for char in palabra:
            # Solo codificar caracteres válidos (letras A-Z y dígitos 0-9)
            if char in MAPA_MORSE:
                letras_morse.append(MAPA_MORSE[char])
        
        # Une los códigos Morse de las letras con un espacio
        if letras_morse:
            palabras_morse.append(" ".join(letras_morse))

    # Une las palabras codificadas con el separador de palabras '/'
    morse_codificado = " / ".join(palabras_morse)
    
    # 3. Actualizar estado global con el texto limpio y el morse generado
    # Se almacena el texto original limpio (sin espacios múltiples)
    texto_original_limpio = " ".join(texto_normalizado.split())
    
    ESTADO['texto_original'] = texto_original_limpio
    ESTADO['morse_codificado'] = morse_codificado
    
    return morse_codificado

def decodificar_mensaje(mensaje_morse: str) -> str:
    """
    Decodifica un mensaje en código Morse de vuelta a texto normal (mayúsculas).

    Reconoce secuencias de puntos/rayas separadas por espacios como letras, 
    y " / " como separador de palabras. Cumple con la Tarea 5 (Decodificación).

    Args:
        mensaje_morse: El código Morse a decodificar, e.g., ".... --- .-.. .- / -- ..- -. -.. ---".

    Returns:
        str: El mensaje decodificado en texto plano (mayúsculas).
    """
    palabras_texto = []
    
    # 1. Separar palabras por el símbolo '/'
    for palabra_morse in mensaje_morse.split(' / '):
        letras_texto = []
        
        # 2. Separar letras por el espacio
        for codigo in palabra_morse.split():
            # Buscar el código en el mapa inverso
            if codigo in MAPA_TEXTO:
                letras_texto.append(MAPA_TEXTO[codigo])
            else:
                # Si el código no existe en el mapa, se ignora por simplicidad.
                pass 
        
        # Une las letras para formar la palabra
        if letras_texto:
            palabras_texto.append("".join(letras_texto))
    
    # 3. Unir las palabras con espacios
    texto_decodificado = " ".join(palabras_texto)
    
    return texto_decodificado

def generar_estadisticas() -> dict:
    """
    Genera estadísticas detalladas del último mensaje codificado almacenado en el estado global.
    
    Las estadísticas incluyen el conteo de letras, dígitos, palabras, puntos y rayas.
    Cumple con la Tarea 7 (Generación de Estadísticas).

    Returns:
        dict: Un diccionario con las estadísticas del mensaje, o None si no hay mensaje.
    """
    texto = ESTADO['texto_original']
    morse = ESTADO['morse_codificado']
    
    if not texto or not morse:
        return None

    # 1. Contar Palabras
    # Usamos el texto limpio almacenado
    num_palabras = len(texto.split())
    
    # 2. Contar Letras y Dígitos
    num_letras = 0
    num_digitos = 0
    
    for char in texto:
        if char.isalpha():
            num_letras += 1
        elif char.isdigit():
            num_digitos += 1
            
    # 3. Contar Puntos y Rayas en el Morse
    # Se eliminan espacios y '/' para contar solo los símbolos
    simbolos_morse = morse.replace(' ', '').replace('/', '')
    num_puntos = simbolos_morse.count('.')
    num_rayas = simbolos_morse.count('-')
    
    return {
        'Mensaje original': texto,
        'Letras': num_letras,
        'Dígitos': num_digitos,
        'Palabras': num_palabras,
        'Puntos': num_puntos,
        'Rayas': num_rayas
    }

# ----------------------------------------------------------------------
# FIN DE MODULO DE CODIGO MORSE
# ----------------------------------------------------------------------

# Funcion principal
def main():
    # Ejemplo de uso del módulo de código Morse
    ejecutar = True
    while ejecutar:
        # Mostrar el menú
        opcion = input("\nOpción [Codificar|Decodificar|Validar|Fin]: ").upper().strip()
                
        # --- C: CODIFICAR ---
        if opcion == 'C':
            mensaje_texto = input("Mensaje: ")
            
            if not mensaje_texto.strip():
                print("Error: El mensaje de texto no puede estar vacío.")
                continue

            try:
                morse_codificado = normalizar_y_codificar(mensaje_texto)
                print(f"Morse: {morse_codificado}")
            except Exception as e:
                print(f"Error al codificar: {e}")
                # Limpiar el estado en caso de error
                ESTADO['texto_original'] = None
                ESTADO['morse_codificado'] = None

        # --- D: DECODIFICAR ---
        elif opcion == 'D':
            # 1. Manejo de error (Tarea 6)
            if ESTADO['texto_original'] is None:
                print("Error: No se ha ingresado un mensaje.")
                continue
                
            # 2. Pedir el código Morse a decodificar
            mensaje_morse = input("Morse: ")
            
            if not mensaje_morse.strip():
                print("Error: El código Morse no puede estar vacío.")
                continue
            
            try:
                # El mensaje a decodificar es el ingresado por el usuario, no el guardado.
                texto_decodificado = decodificar_mensaje(mensaje_morse)
                print(f"Texto: {texto_decodificado}")
            except Exception as e:
                print(f"Error al decodificar: {e}")

        # --- V: VALIDAR/ESTADÍSTICAS ---
        elif opcion == 'V':
            # 1. Manejo de error (Tarea 6)
            if ESTADO['texto_original'] is None:
                print("Error: No se ha ingresado un mensaje.")
                continue

            # 2. Generar y mostrar estadísticas
            try:
                estadisticas = generar_estadisticas()
                print(f"Mensaje original: {estadisticas['Mensaje original']}")
                print(f"Letras: {estadisticas['Letras']}")
                print(f"Dígitos: {estadisticas['Dígitos']}")
                print(f"Palabras: {estadisticas['Palabras']}")
                print(f"Puntos: {estadisticas['Puntos']}")
                print(f"Rayas: {estadisticas['Rayas']}")
            except Exception as e:
                print(f"Error al generar estadísticas: {e}")

        # --- F: FINALIZAR ---
        elif opcion == 'F':
            print("Programa finalizado. ¡Hasta pronto!")
            ejecutar = False
            
        # --- OPCIÓN INVÁLIDA ---
        else:
            print("Opción no válida. Por favor, elija C, D, V o F.")
