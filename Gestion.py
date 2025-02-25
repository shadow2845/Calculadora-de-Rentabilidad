import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calcular_punto_equilibrio():
    try:
        costos_fijos = float(entry_costos_fijos.get())
        costos_variables = float(entry_costos_variables.get())
        precio_venta = float(entry_precio_venta.get())

        if precio_venta <= costos_variables:
            if messagebox:
                messagebox.showerror("Error", "El precio de venta debe ser mayor que el costo variable.")
            else:
                print("Error: El precio de venta debe ser mayor que el costo variable.")
            return

        punto_equilibrio = costos_fijos / (precio_venta - costos_variables)
        label_resultado.config(text=f"Punto de Equilibrio: {punto_equilibrio:.2f} unidades")
        graficar_rentabilidad(costos_fijos, costos_variables, precio_venta, punto_equilibrio)
    except ValueError:
        if messagebox:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
        else:
            print("Error: Por favor, ingrese valores numéricos válidos.")

def graficar_rentabilidad(costos_fijos, costos_variables, precio_venta, punto_equilibrio):
    global canvas, fig, ax
    unidades = np.linspace(0, punto_equilibrio * 2, 100)
    costos_totales = costos_fijos + (costos_variables * unidades)
    ingresos_totales = precio_venta * unidades
    
    ax.clear()
    ax.plot(unidades, ingresos_totales, label="Ingresos", color='green')
    ax.plot(unidades, costos_totales, label="Costos Totales", color='red')
    ax.axvline(punto_equilibrio, linestyle='--', color='blue', label="Punto de Equilibrio")
    ax.set_xlabel("Unidades Vendidas")
    ax.set_ylabel("Monto ($)")
    ax.legend()
    ax.set_title("Análisis de Rentabilidad")
    ax.grid()
    canvas.draw()

def actualizar_simulacion(val):
    costos_fijos = float(entry_costos_fijos.get())
    costos_variables = float(entry_costos_variables.get()) * (1 + (slider_costo_variable.get() / 100))
    precio_venta = float(entry_precio_venta.get()) * (1 + (slider_precio.get() / 100))
    
    punto_equilibrio = costos_fijos / (precio_venta - costos_variables)
    label_resultado.config(text=f"Punto de Equilibrio: {punto_equilibrio:.2f} unidades")
    graficar_rentabilidad(costos_fijos, costos_variables, precio_venta, punto_equilibrio)

def crear_interfaz():
    global entry_costos_fijos, entry_costos_variables, entry_precio_venta, label_resultado, slider_costo_variable, slider_precio, canvas, fig, ax
    
    if messagebox is None:
        print("Modo consola: tkinter no disponible")
        return
    
    root = tk.Tk()
    root.title("Calculadora de Rentabilidad")
    root.geometry("600x600")
    
    tk.Label(root, text="Costos Fijos:").pack()
    entry_costos_fijos = tk.Entry(root)
    entry_costos_fijos.pack()
    
    tk.Label(root, text="Costos Variables por Unidad:").pack()
    entry_costos_variables = tk.Entry(root)
    entry_costos_variables.pack()
    
    tk.Label(root, text="Precio de Venta por Unidad:").pack()
    entry_precio_venta = tk.Entry(root)
    entry_precio_venta.pack()
    
    btn_calcular = tk.Button(root, text="Calcular Punto de Equilibrio", command=calcular_punto_equilibrio)
    btn_calcular.pack()
    
    label_resultado = tk.Label(root, text="Punto de Equilibrio: ? unidades", font=("Arial", 12))
    label_resultado.pack()
    
    tk.Label(root, text="Variación de Costos Variables (%):").pack()
    slider_costo_variable = tk.Scale(root, from_=-20, to=20, orient='horizontal', command=actualizar_simulacion)
    slider_costo_variable.pack()
    
    tk.Label(root, text="Variación del Precio de Venta (%):").pack()
    slider_precio = tk.Scale(root, from_=-20, to=20, orient='horizontal', command=actualizar_simulacion)
    slider_precio.pack()
    
    fig, ax = plt.subplots(figsize=(6,4))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()
    
    root.mainloop()

crear_interfaz()




