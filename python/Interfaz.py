# Interfaz.py
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from lectura_temperatura import obtener_datos_temperatura
from accion_btn_zoom import accion_btn_zoom

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz")
        self.root.geometry("600x400")  # Set window size to 600x400

        self.label = tk.Label(self.root, text="")
        self.label.pack()

        self.button = tk.Button(self.root, text="Actualizar Gráfico", command=self.actualizar_grafico)
        self.button.pack()

        # Frame to hold the bottom buttons
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Frame to hold the left buttons
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Frame to hold the right graph
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Define the size for the icons
        icon_size = (50, 50)

        # Load and resize the icon images
        self.tostador_icon_image = Image.open("imagenes/TOSTADOR_ICON.PNG").resize(icon_size, Image.LANCZOS)
        self.tostador_icon_photo = ImageTk.PhotoImage(self.tostador_icon_image)

        self.conveccion_icon_image = Image.open("imagenes/CONVECCION_ICON.PNG").resize(icon_size, Image.LANCZOS)
        self.conveccion_icon_photo = ImageTk.PhotoImage(self.conveccion_icon_image)

        self.agitador_icon_image = Image.open("imagenes/AGITADOR_ICON.PNG").resize(icon_size, Image.LANCZOS)
        self.agitador_icon_photo = ImageTk.PhotoImage(self.agitador_icon_image)

        self.enfriador_icon_image = Image.open("imagenes/ENFRIADOR_ICON.PNG").resize(icon_size, Image.LANCZOS)
        self.enfriador_icon_photo = ImageTk.PhotoImage(self.enfriador_icon_image)

        self.run_icon_image = Image.open("imagenes/RUN_ICON.PNG").resize(icon_size, Image.LANCZOS)
        self.run_icon_photo = ImageTk.PhotoImage(self.run_icon_image)

        self.stop_icon_image = Image.open("imagenes/STOP_ICON.PNG").resize(icon_size, Image.LANCZOS)
        self.stop_icon_photo = ImageTk.PhotoImage(self.stop_icon_image)

        self.zoom_icon_image = Image.open("imagenes/ZOOM_ICON.PNG").resize(icon_size, Image.LANCZOS)
        self.zoom_icon_photo = ImageTk.PhotoImage(self.zoom_icon_image)

        # Left buttons
        self.run_button = tk.Button(self.left_frame, text="Run", command=self.on_run_click, image=self.run_icon_photo, compound=tk.LEFT)
        self.run_button.pack(side=tk.TOP, pady=10)

        self.stop_button = tk.Button(self.left_frame, text="Stop", command=self.on_stop_click, image=self.stop_icon_photo, compound=tk.LEFT)
        self.stop_button.pack(side=tk.TOP, pady=10)

        # Bottom buttons
        self.tostador_button = tk.Button(self.bottom_frame, text="Tostador", command=self.on_tostador_click, image=self.tostador_icon_photo, compound=tk.LEFT)
        self.tostador_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.conveccionador_button = tk.Button(self.bottom_frame, text="Conveccionador", command=self.on_conveccionador_click, image=self.conveccion_icon_photo, compound=tk.LEFT)
        self.conveccionador_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.agitador_button = tk.Button(self.bottom_frame, text="Agitador", command=self.on_agitador_click, image=self.agitador_icon_photo, compound=tk.LEFT)
        self.agitador_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.enfriador_button = tk.Button(self.bottom_frame, text="Enfriador", command=self.on_enfriador_click, image=self.enfriador_icon_photo, compound=tk.LEFT)
        self.enfriador_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Create a figure and axis for the graph
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Temperatura vs Tiempo')
        self.ax.set_xlabel('Tiempo')
        self.ax.set_ylabel('Temperatura')
        self.ax.grid(True)

        # Store the data
        self.tiempo, self.temperatura = obtener_datos_temperatura()

        # Plot the initial data
        self.ax.plot(self.tiempo, self.temperatura)

        # Canvas for the graph
        self.graph_canvas = FigureCanvasTkAgg(self.fig, master=self.right_frame)
        self.graph_canvas.draw()
        self.graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Zoom button
        self.zoom_button = tk.Button(self.right_frame, image=self.zoom_icon_photo, command=self.on_zoom_click)
        self.zoom_button.place(relx=0.95, rely=0.05, anchor=tk.NE)

        # Exit button
        self.exit_button = tk.Button(self.root, text="Salir", command=self.root.quit)
        self.exit_button.pack(side=tk.BOTTOM, pady=10)

    def mostrar_mensaje(self, mensaje):
        self.label.config(text=mensaje)

    def on_button_click(self):
        self.mostrar_mensaje("Button was clicked!")

    def on_tostador_click(self):
        self.mostrar_mensaje("Tostador button was clicked!")

    def on_conveccionador_click(self):
        self.mostrar_mensaje("Conveccionador button was clicked!")

    def on_agitador_click(self):
        self.mostrar_mensaje("Agitador button was clicked!")

    def on_enfriador_click(self):
        self.mostrar_mensaje("Enfriador button was clicked!")

    def on_run_click(self):
        self.mostrar_mensaje("Run button was clicked!")

    def on_stop_click(self):
        self.mostrar_mensaje("Stop button was clicked!")

    def on_zoom_click(self):
        accion_btn_zoom(self.root, self.fig)

    def actualizar_grafico(self):
        # Clear the current plot
        self.ax.clear()
        self.ax.set_title('Temperatura vs Tiempo')
        self.ax.set_xlabel('Tiempo')
        self.ax.set_ylabel('Temperatura')
        self.ax.grid(True)
        # Plot the new data
        self.ax.plot(self.tiempo, self.temperatura)
        self.graph_canvas.draw()

    def iniciar(self):
        self.root.mainloop()