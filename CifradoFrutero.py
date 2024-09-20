
# Diccionario con las letras y los emojis de frutas/vegetales
frutero = {
    'A': '🍏', 'B': '🍎', 'C': '🍐', 'D': '🍊', 'E': '🍋',
    'F': '🧄', 'G': '🍌', 'H': '🍉', 'I': '🍇', 'J': '🍓',
    'K': '🥕', 'L': '🍈', 'M': '🍒', 'N': '🍑', 'Ñ': '🥭',
    'O': '🍍', 'P': '🥥', 'Q': '🥝', 'R': '🍅', 'S': '🍆',
    'T': '🥑', 'U': '🌽', 'V': '🥦', 'W': '🥬', 'X': '🥒',
    'Y': '🌶', 'Z': '🥔'
}

# Creamos un diccionario inverso para traducir de frutero a texto
frutero_inverso = {valor: clave for clave, valor in frutero.items()}

# Función para decodificar texto a "lenguaje frutero"
def decodificar_a_frutas(texto):
    resultado = ''
    for letra in texto.upper():
        if letra in frutero:
            resultado += frutero[letra]
        else:
            resultado += letra  # Mantenemos espacios y signos de puntuación
    return resultado

# Función para decodificar de "lenguaje frutero" a texto
def decodificar_a_texto(texto_frutero):
    resultado = ''
    i = 0
    while i < len(texto_frutero):
        encontrado = False
        for emoji in frutero_inverso:
            if texto_frutero[i:i+len(emoji)] == emoji:  # Busca el emoji completo
                resultado += frutero_inverso[emoji]
                i += len(emoji)  # Avanza el índice según el tamaño del emoji
                encontrado = True
                break
        if not encontrado:
            resultado += texto_frutero[i]  # Añade espacios o caracteres que no son emojis
            i += 1
    return resultado

# Función principal con opción de traducción
def traducir():
    print("Seleccione una opción:")
    print("1. Traducir de texto a frutero")
    print("2. Traducir de frutero a texto")
    
    opcion = input("Opción (1 o 2): ")
    
    if opcion == '1':
        texto_usuario = input("Escribe un texto para convertir a frutas: ")
        print("Texto frutero:", decodificar_a_frutas(texto_usuario))
    elif opcion == '2':
        texto_frutero = input("Escribe el texto en lenguaje frutero: ")
        print("Texto traducido a letras:", decodificar_a_texto(texto_frutero))
    else:
        print("Opción no válida. Por favor, selecciona 1 o 2.")

# Ejecutamos el programa
traducir()
