import tkinter as tk
from tkinter import messagebox
import random
import threading
import time

class Sensor:
    def __init__(self):
        self.temperatura = 0
        self.humedad = 0
    
    def leer_datos(self):
        try:
            self.temperatura = round(random.uniform(0, 50), 2)
            self.humedad = round(random.uniform(20, 90), 2)
        except Exception as e:
            print("Error en la generación de datos:", e)
        return self.temperatura, self.humedad

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.sensor = Sensor()
        self.umbral = 30.0  
        
        self.root.title("Monitor de Sensor")
        
        self.label_temp = tk.Label(root, text="Temperatura: 0°C", font=("Arial", 14))
        self.label_temp.pack()
        
        self.label_hum = tk.Label(root, text="Humedad: 0%", font=("Arial", 14))
        self.label_hum.pack()
        
        self.label_umbral = tk.Label(root, text="Ingrese umbral de temperatura:")
        self.label_umbral.pack()
        
        self.entry_umbral = tk.Entry(root)
        self.entry_umbral.pack()
        
        self.boton_confirmar = tk.Button(root, text="Confirmar", command=self.actualizar_umbral)
        self.boton_confirmar.pack()
        
        self.estado_label = tk.Label(root, text="Estado: Normal", font=("Arial", 14))
        self.estado_label.pack()
        
        self.hilo = threading.Thread(target=self.actualizar_datos, daemon=True)
        self.hilo.start()
        
    def actualizar_umbral(self):
        try:
            self.umbral = float(self.entry_umbral.get())
            messagebox.showinfo("Información", "Umbral actualizado correctamente")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")
    
    def actualizar_datos(self):
        while True:
            temperatura, humedad = self.sensor.leer_datos()
            self.label_temp.config(text=f"Temperatura: {temperatura}°C")
            self.label_hum.config(text=f"Humedad: {humedad}%")
            
            if temperatura > self.umbral:
                self.estado_label.config(text="Estado: ¡Alerta!", fg="red")
            else:
                self.estado_label.config(text="Estado: Normal", fg="black")
            
            time.sleep(2)

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()