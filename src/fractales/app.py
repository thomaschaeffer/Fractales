from pathlib import Path
from fractales.render import compute_fractal_mandelbrot, save_grayscale

def mandelbrot_gray():
    A = compute_fractal_mandelbrot(1600, 1200, -2.5, 1.0, -1.2, 1.2, 100)
    save_grayscale(A, 100 , "outputs/mandelbrot_gray.png")

if __name__ == "__main__":
    mandelbrot_gray()
