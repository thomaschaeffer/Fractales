from pathlib import Path
from fractales.render import mandelbrot_compute_fractal,julia_compute_fractal,burning_ship_compute_fractal, save_grayscale,save_colorize
from fractales.palettes import colors

A = mandelbrot_compute_fractal(1600, 1200, -2.5, 1.0, -1.2, 1.2, 100)
B=julia_compute_fractal(1600, 1200, -1.6, 1.6, -1.2, 1.2, 150,complex(-0.8,0.156))
Bis=julia_compute_fractal(1600, 1200, -1.6, 1.6, -1.2, 1.2, 300,complex(0,0.7))
Bthird=julia_compute_fractal(1600, 1200, -1.6, 1.6, -1.2, 1.2, 300,complex(0.285,0.01))
C = burning_ship_compute_fractal(1600, 1200, -2.5, 1.0, -1.2, 1.2, 150)
#julia value c: (-0.123,0.745),
def mandelbrot_gray():
    save_grayscale(A, 100 , "outputs/mandelbrot_gray.png")

def mandelbrot():
    save_colorize(A,100,colors["sunset"],"outputs/mandelbrot_sunset.png")
def julia():
    save_colorize(B,150,colors["sunset"],"outputs/julia_sunset.png")
    save_colorize(Bis,300,colors["sunset"],"outputs/julia_sunsetbis.png")
    save_colorize(Bthird,300,colors["sunset"],"outputs/julia_sunsetbthird.png")
def burning_ship():
    save_colorize(C,150,colors["sunset"],"outputs/burning_ship_sunset.png")

if __name__ == "__main__":
    mandelbrot_gray()
    mandelbrot()
    julia()
    burning_ship()