import tkinter as tk
import random

class ValorantAgente:
    agentes = ["Jett", "Phoenix", "Sage", "Raze", "Sova", "Chamber", "Skye", "Reyna", "Killjoy"]
    roles = ["Duelista", "Centinela", "Controlador", "Iniciador"]
    habilidades = [
        "Resurrección", "Tour De Force", "Réplica", 
        "Prowler", "Bum Bot", "Nanobots", "Cables Trampa"
    ]

    historial = []

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tu Agente Valorant Personalizado")

        tk.Label(self.ventana, text="Ingresa tu nombre de jugador:").pack(pady=5)
        self.nombre_entry = tk.Entry(self.ventana)
        self.nombre_entry.pack()

        tk.Button(self.ventana, text="Generar Agente", command=self.generar_agente).pack(pady=10)
        tk.Button(self.ventana, text="Limpiar", command=self.limpiar).pack()

        self.resultado = tk.Label(self.ventana, text="", fg="darkgreen", wraplength=300)
        self.resultado.pack(pady=15)

        self.ventana.mainloop()

    def generar_agente(self):
        nombre = self.nombre_entry.get().strip()

        if not nombre:
            self.resultado.config(text="Por favor ingresa tu nombre.")
            return

        agente = random.choice(self.agentes)
        rol = random.choice(self.roles)
        habilidad = random.choice(self.habilidades)

        mensaje = (f"{nombre}, tu agente personalizado es {agente}.\n"
                   f"Rol: {rol}\n"
                   f"Habilidad especial: {habilidad} 💥")

        self.resultado.config(text=mensaje)
        self.historial.append((nombre, agente, rol, habilidad))

    def limpiar(self):
        self.nombre_entry.delete(0, tk.END)
        self.resultado.config(text="")

ValorantAgente()
