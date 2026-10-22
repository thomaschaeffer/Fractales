import numpy as np
from pathlib import Path
from PIL import Image
from core import escape_iterations

def compute_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    A = np.zeros((height,width),dtype=int)
    for y in range(height):
        for x in range(width):
            x_c = x_min + x/(width -1) * (x_max - x_min)
            y_c = y_min + y/ (height -1) * (y_max - y_min)
            c = complex(x_c,y_c)
            A[y,x] = escape_iterations(c,max_iter)
    return A

def save_grayscale(iterations, max_iter , output_path):
    row = len(iterations)
    column = len(iterations.T)
    A = np.zeros((row,column),dtype=np.uint8)
    for y in range(row):
        for x in range(column):
            A[y,x]= (1 - iterations[y,x]/max_iter) * 255

    output_path= Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    image = Image.fromarray(A)
    image.save(output_path)

A = compute_fractal(1600, 1200, -2.5, 1.0, -1.2, 1.2, 100)
save_grayscale(A, 100 , "outputs/mandelbrot_gray.png")