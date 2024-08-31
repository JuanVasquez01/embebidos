# accion_btn_zoom.py
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def accion_btn_zoom(root, fig):
    zoom_window = tk.Toplevel(root)
    zoom_window.title("Zoom Gráfico")
    zoom_window.geometry("1200x1100")

    zoom_canvas = FigureCanvasTkAgg(fig, master=zoom_window)
    zoom_canvas.draw()
    zoom_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)