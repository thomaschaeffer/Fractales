from pathlib import Path
from fractales.render import compute_fractal_mandelbrot, save_grayscale,save_colorize
from fractales.palettes import colors

def mandelbrot_gray():
    A = compute_fractal_mandelbrot(1600, 1200, -2.5, 1.0, -1.2, 1.2, 100)
    save_grayscale(A, 100 , "outputs/mandelbrot_gray.png")

def mandelbrot():
    A = compute_fractal_mandelbrot(1600, 1200, -2.5, 1.0, -1.2, 1.2, 100)

    save_colorize(A,100,colors["toxic"],"outputs/mandelbrot_toxic.png")

if __name__ == "__main__":
    mandelbrot()
