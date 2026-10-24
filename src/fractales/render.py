import numpy as np
from pathlib import Path
from PIL import Image
from fractales.core import escape_iterations__mandelbrot, smooth_iterations
from fractales.palettes import colorize

def compute_fractal_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    A = np.zeros((height,width),dtype=int)
    for y in range(height):
        for x in range(width):
            x_c = x_min + x/(width -1) * (x_max - x_min)
            y_c = y_min + y/ (height -1) * (y_max - y_min)
            c = complex(x_c,y_c)
            n,z = escape_iterations__mandelbrot(c,max_iter)
            A[y,x] = smooth_iterations(n,z,max_iter)
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

def save_colorize(iteration,max_iter,colors,outputpath):
    image = colorize(iteration,max_iter,colors)
    Image.fromarray(image).save(outputpath)

