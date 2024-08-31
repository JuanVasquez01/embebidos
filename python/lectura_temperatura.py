import numpy as np
from scipy.interpolate import CubicSpline

curva_tostion = [
    (0, 160), (0.5, 151), (1, 142), (1.5, 139), (2, 137), (2.5, 137), (3, 137), (3.5, 136.5), (4, 136),
    (4.5, 136), (5, 136), (5.5, 135.5), (6, 135), (6.5, 135), (7, 135), (7.5, 135), (8, 135), (8.5, 135.5),
    (9, 136), (9.5, 137), (10, 138), (10.5, 138.5), (11, 139), (11.5, 140), (12, 141), (12.5, 142), (13, 143),
    (13.5, 144), (14, 145), (14.5, 146.5), (15, 148), (15.5, 149), (16, 150), (16.5, 151.5), (17, 153),
    (17.5, 154.5), (18, 156), (18.5, 157), (19, 158), (19.5, 159), (20, 160)
]

def generar_curva_tostion(tiempo):
    tiempos = [punto[0] for punto in curva_tostion] 
    temperaturas = [punto[1] for punto in curva_tostion]
    cs = CubicSpline(tiempos, temperaturas)
    return cs(tiempo)

def obtener_datos_temperatura():
    tiempo = np.linspace(0, 20, 200)  # Aumentar el número de puntos de tiempo
    temperatura = generar_curva_tostion(tiempo)
    return tiempo, temperatura