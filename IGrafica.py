import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from ALexico import analizador_lexico
from ASintactico import analizador_sintactico

def procesar():
    entrada = texto_entrada.get("1.0", tk.END)
    tokens = analizador_lexico(entrada)
    resultado_lexico = "Análisis Léxico:\n"
    for token in tokens:
        resultado_lexico += f"Tipo: {token[0]}, Lexema: {token[1]}, Línea: {token[2]}\n"

    resultado_sintactico = "Análisis Sintáctico:\n" + analizador_sintactico(tokens)

    texto_salida.delete("1.0", tk.END)
    texto_salida.insert(tk.END, resultado_lexico + "\n" + resultado_sintactico)

ventana = tk.Tk()
ventana.title("Programa Analizador")
ventana.geometry("800x600")

texto_entrada = ScrolledText(ventana, height=15)
texto_entrada.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

boton_procesar = tk.Button(ventana, text="Procesar", command=procesar)
boton_procesar.pack(pady=5)

texto_salida = ScrolledText(ventana, height=15)
texto_salida.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

ventana.mainloop()