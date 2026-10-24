from pathlib import Path
from fractales.render import compute_fractal_mandelbrot, save_grayscale,save_colorize
from fractales.palettes import colors

A = compute_fractal_mandelbrot(1600, 1200, -2.5, 1.0, -1.2, 1.2, 100)

def mandelbrot_gray():
    save_grayscale(A, 100 , "outputs/mandelbrot_gray.png")

def mandelbrot():
    save_colorize(A,100,colors["sunset"],"outputs/mandelbrot_sunset_clean.png")

if __name__ == "__main__":
    mandelbrot_gray()
    mandelbrot()
