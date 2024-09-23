import tkinter as tk
from tkinter import messagebox

# Diccionario con las letras y los emojis de frutas/vegetales
frutero = {
    'A': '🍏', 'B': '🍎', 'C': '🍐', 'D': '🍊', 'E': '🍋',
    'F': '🧄', 'G': '🍌', 'H': '🍉', 'I': '🍇', 'J': '🍓',
    'K': '🥕', 'L': '🍈', 'M': '🍒', 'N': '🍑', 'Ñ': '🥭',
    'O': '🍍', 'P': '🥥', 'Q': '🥝', 'R': '🍅', 'S': '🍆',
    'T': '🥑', 'U': '🌽', 'V': '🥦', 'W': '🥬', 'X': '🥒',
    'Y': '🌶', 'Z': '🥔'
}

# Diccionario inverso para decodificar de emojis a texto
frutero_inverso = {valor: clave for clave, valor in frutero.items()}

# Función para convertir texto a frutero
def decodificar_a_frutas(texto):
    resultado = ''
    for letra in texto.upper():
        if letra in frutero:
            resultado += frutero[letra]
        else:
            resultado += letra  # Dejar espacios y signos de puntuación
    return resultado

# Función para convertir de frutero a texto
def decodificar_a_texto(texto_frutero):
    resultado = ''
    i = 0
    while i < len(texto_frutero):
        encontrado = False
        for emoji in frutero_inverso:
            if texto_frutero[i:i+len(emoji)] == emoji:  # Busca el emoji completo
                resultado += frutero_inverso[emoji]
                i += len(emoji)
                encontrado = True
                break
        if not encontrado:
            resultado += texto_frutero[i]  # Añade caracteres que no son emojis
            i += 1
    return resultado

# Función que se ejecuta cuando el usuario presiona el botón de traducir
def traducir():
    texto_entrada = entrada_texto.get("1.0", tk.END).strip()  # Obtiene el texto de la caja de texto
    if variable_opcion.get() == "Texto a Frutero":
        resultado = decodificar_a_frutas(texto_entrada)
    elif variable_opcion.get() == "Frutero a Texto":
        resultado = decodificar_a_texto(texto_entrada)
    else:
        messagebox.showerror("Error", "Selecciona una opción válida")
        return
    
    # Muestra el resultado en la caja de texto de salida
    salida_texto.delete("1.0", tk.END)  # Limpia la salida anterior
    salida_texto.insert(tk.END, resultado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Decodificador Frutero")
ventana.geometry("400x300")

# Modo oscuro - colores personalizados
color_fondo = "#2E2E2E"  # Fondo oscuro
color_texto = "#FFFFFF"  # Texto claro
color_caja_texto = "#1C1C1C"  # Fondo de las cajas de texto
color_boton = "#3A3A3A"  # Fondo de los botones
color_borde = "#5E5E5E"  # Bordes más claros

# Configuración del modo oscuro en la ventana
ventana.configure(bg=color_fondo)

# Etiqueta para la opción de traducción
etiqueta_opcion = tk.Label(ventana, text="Selecciona una opción:", bg=color_fondo, fg=color_texto)
etiqueta_opcion.pack(pady=10)

# Menú desplegable para elegir la opción
variable_opcion = tk.StringVar(ventana)
variable_opcion.set("Texto a Frutero")  # Valor por defecto

menu_opciones = tk.OptionMenu(ventana, variable_opcion, "Texto a Frutero", "Frutero a Texto")
menu_opciones.config(bg=color_boton, fg=color_texto, activebackground=color_borde, activeforeground=color_texto)
menu_opciones["menu"].config(bg=color_boton, fg=color_texto)
menu_opciones.pack(pady=5)

# Etiqueta y caja de entrada de texto
etiqueta_entrada = tk.Label(ventana, text="Introduce el texto:", bg=color_fondo, fg=color_texto)
etiqueta_entrada.pack(pady=5)

entrada_texto = tk.Text(ventana, height=5, width=40, bg=color_caja_texto, fg=color_texto, insertbackground=color_texto)
entrada_texto.pack(pady=5)

# Botón para ejecutar la traducción
boton_traducir = tk.Button(ventana, text="Traducir", command=traducir, bg=color_boton, fg=color_texto)
boton_traducir.pack(pady=10)

# Caja de texto para mostrar el resultado
salida_texto = tk.Text(ventana, height=5, width=40, bg=color_caja_texto, fg=color_texto, insertbackground=color_texto)
salida_texto.pack(pady=5)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
