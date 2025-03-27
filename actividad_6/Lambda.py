import tkinter as tk

class Formulario:
    def __init__(self):
        self.ventana_formulario = tk.Tk()
        self.ventana_formulario.title("Formulario")

        self.label_nombre = tk.Label(self.ventana_formulario, text="digite el nombre")
        self.label_nombre.pack()

        self.entry_nombre = tk.Entry(self.ventana_formulario)
        self.entry_nombre.pack()

        self.boton_enviar = tk.Button(self.ventana_formulario, text="Guardar Cliente", command=self.tomar_datos)
        self.boton_enviar.pack()

        self.boton_limpiar = tk.Button(self.ventana_formulario, text="limpiar", command=self.limpiar_campos)
        self.boton_limpiar.pack()

        self.ventana_formulario.mainloop()

    def tomar_datos(self):
        nombre = self.entry_nombre.get()
        print(f"Nombre guardado: {nombre}")

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)

Formulario()
