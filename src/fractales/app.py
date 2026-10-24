import cupy as cp
from fractales.render import mandelbrot_compute_fractal,julia_compute_fractal,burning_ship_compute_fractal, save_grayscale,save_colorize
from fractales.palettes import colors
from fractales.gpu import compute_mandelbrot_gpu




def mandelbrot_gray():
    A = mandelbrot_compute_fractal(1600, 1200, -2.5, 1.0, -1.2, 1.2, 100)
    save_grayscale(A, 100 , "outputs/mandelbrot_gray.png")

def mandelbrot():
    A = mandelbrot_compute_fractal(1600, 1200, -2.5, 1.0, -1.2, 1.2, 100)
    save_colorize(A,100,colors["sunset"],"outputs/mandelbrot_sunset.png")

def julia():
    B=julia_compute_fractal(1600, 1200, -1.6, 1.6, -1.2, 1.2, 150,complex(-0.8,0.156))
    Bis=julia_compute_fractal(1600, 1200, -1.6, 1.6, -1.2, 1.2, 300,complex(0,0.7))
    Bthird=julia_compute_fractal(1600, 1200, -1.6, 1.6, -1.2, 1.2, 300,complex(0.285,0.01))
    save_colorize(B,150,colors["sunset"],"outputs/julia_sunset.png")
    save_colorize(Bis,300,colors["sunset"],"outputs/julia_sunsetbis.png")
    save_colorize(Bthird,300,colors["sunset"],"outputs/julia_sunsetbthird.png")
    #julia value c: (-0.123,0.745),

def burning_ship():
    C = burning_ship_compute_fractal(1600, 1200, -2.5, 1.0, -1.2, 1.2, 150)
    save_colorize(C,150,colors["sunset"],"outputs/burning_ship_sunset.png")

def CPU():
    #mandelbrot_gray()
    mandelbrot()
    julia()
    burning_ship()

def GPU():
    A = compute_mandelbrot_gpu(7000, 4800, -2.5,  1.0, -1.2, 1.2, 150)
    A = cp.asnumpy(A)
    save_colorize(A,150,colors["sunset"],"outputs/mandelbrot_sunset.png")
if __name__ == "__main__":
    #CPU()
    GPU()