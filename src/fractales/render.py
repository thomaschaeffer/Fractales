import numpy as np
from pathlib import Path
from PIL import Image
from fractales.core import mandelbrot_escape_iterations,julia_escape_iterations, burning_ship_escape_iterations,smooth_iterations
from fractales.palettes import colorize

def mandelbrot_compute_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    A = np.zeros((height,width),dtype=float)
    for y in range(height):
        for x in range(width):
            x_c = x_min + x/(width -1) * (x_max - x_min)
            y_c = y_min + y/ (height -1) * (y_max - y_min)
            c = complex(x_c,y_c)
            n,z = mandelbrot_escape_iterations(c,max_iter)
            A[y,x] = smooth_iterations(n,z,max_iter)
    return A

def julia_compute_fractal(width, height, x_min, x_max, y_min, y_max, max_iter,c):
    A = np.zeros((height,width),dtype=float)
    for y in range(height):
        for x in range(width):
            x_c = x_min + x/(width -1) * (x_max - x_min)
            y_c = y_min + y/ (height -1) * (y_max - y_min)
            z0 = complex(x_c,y_c)
            n,z = julia_escape_iterations(z0,c,max_iter)
            A[y,x] = smooth_iterations(n,z,max_iter)
    return A

def burning_ship_compute_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    A = np.zeros((height,width),dtype=float)
    for y in range(height):
        for x in range(width):
            x_c = x_min + x/(width -1) * (x_max - x_min)
            y_c = y_min + y/ (height -1) * (y_max - y_min)
            c = complex(x_c,y_c)
            n,z = burning_ship_escape_iterations(c,max_iter)
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

