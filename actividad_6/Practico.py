import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class RegistroVehiculos:
    vehiculos_registrados = []  
    
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Vehículos")
        
        
        self.labels_text = ["Placa:", "Marca:", "Color:", "Tipo (Residente/Visitante):"]
        self.entries = {}
        
        for i, text in enumerate(self.labels_text):
            tk.Label(root, text=text).grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[text] = entry
        
        
        tk.Button(root, text="Guardar", command=self.guardar_vehiculo).grid(row=4, column=0, pady=10)
        tk.Button(root, text="Limpiar", command=lambda: self.limpiar_campos()).grid(row=4, column=1, pady=10)
        tk.Button(root, text="Mostrar Registro", command=self.mostrar_registro).grid(row=5, column=0, columnspan=2, pady=10)
        
        
        self.label_mensaje = tk.Label(root, text="", fg="red")
        self.label_mensaje.grid(row=6, column=0, columnspan=2, pady=5)
    
    def guardar_vehiculo(self):
        datos = {text: self.entries[text].get().strip() for text in self.labels_text}
        
        
        if any(valor == "" for valor in datos.values()):
            self.label_mensaje.config(text="Todos los campos son obligatorios")
            return
        
        datos["Hora Ingreso"] = datetime.now().strftime("%H:%M:%S")
        self.vehiculos_registrados.append(datos)
        messagebox.showinfo("Éxito", "Vehículo registrado correctamente")
        self.limpiar_campos()
    
    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.label_mensaje.config(text="")
    
    def mostrar_registro(self):
        print("Vehículos Registrados:")
        for vehiculo in self.vehiculos_registrados:
            print(vehiculo)
        
        mensaje = "\n".join([f"Placa: {v['Placa:']}, Marca: {v['Marca:']}, Hora: {v['Hora Ingreso']}" for v in self.vehiculos_registrados])
        self.label_mensaje.config(text=mensaje if mensaje else "No hay registros")


root = tk.Tk()
app = RegistroVehiculos(root)
root.mainloop()
