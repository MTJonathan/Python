import tkinter as tk

def saludar():
    mensaje.config(text="¡Hola, mundo!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera app en Tkinter")

# Crear un botón
boton = tk.Button(ventana, text="Haz clic aquí", command=saludar)
boton.pack(pady=20)

# Crear una etiqueta para mostrar el mensaje
mensaje = tk.Label(ventana, text="")
mensaje.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
