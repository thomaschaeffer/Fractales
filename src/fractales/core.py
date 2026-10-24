import math
def mandelbrot_escape_iterations ( c , max_iter):
    z=0
    cmp=0
    while abs(z)<=2 and cmp < max_iter : 
         z= z*z + c
         cmp = cmp +1
    return cmp,z

def julia_escape_iterations (z0, c , max_iter):
     z=z0
     cmp=0
     while abs(z)<=2 and cmp < max_iter : 
          z= z*z + c
          cmp = cmp +1
     return cmp,z

def burning_ship_escape_iterations (c , max_iter):
     z=0
     cmp=0
     while abs(z)<=2 and cmp < max_iter : 
          z= (complex(abs(z.real),abs(z.imag)))**2 + c
          cmp = cmp +1
     return cmp,z

def smooth_iterations(n , z , max_iter):
     if n >= max_iter:
          return max_iter
     return n+1 - math.log(math.log(abs(z)))/math.log(2)

