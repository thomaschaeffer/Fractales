import cupy as cp

def compute_mandelbrot_gpu(width, height, x_min, x_max, y_min, y_max, max_iter):
    xs = cp.linspace(x_min,x_max,width,False,False,float)
    ys = cp.linspace(y_min,y_max,height,False,False,float)
    X,Y = cp.meshgrid(xs,ys)
    C=X + 1j*Y
    Z=cp.zeros_like(C)
    iterations = cp.full(C.shape,max_iter,dtype=cp.float64)
    mask = cp.ones(C.shape, dtype=bool)
    for i in range(max_iter):
        Z[mask]=Z[mask]**2 +C[mask]
        new_div=mask & (cp.abs(Z)>2)
        iterations[new_div]= i+1
        mask[new_div] = False
    mask = ~mask
    smooth = iterations.copy()
    smooth[mask] = (iterations[mask] +1 - cp.log(cp.log(cp.abs(Z[mask])))/cp.log(2))
    return smooth

def compute_burning_ship_gpu(width, height, x_min, x_max, y_min, y_max, max_iter):
    xs = cp.linspace(x_min,x_max,width,False,False,float)
    ys = cp.linspace(y_min,y_max,height,False,False,float)
    X,Y = cp.meshgrid(xs,ys)
    C=X + 1j*Y
    Z=cp.zeros_like(C)
    iterations = cp.full(C.shape,max_iter,dtype=cp.float64)
    mask = cp.ones(C.shape, dtype=bool)
    for i in range(max_iter):
        Z[mask]= (cp.abs(Z[mask].real) + 1j * cp.abs(Z[mask].imag))**2 + C[mask]
        new_div=mask & (cp.abs(Z)>2)
        iterations[new_div]= i+1
        mask[new_div] = False
    mask = ~mask
    smooth = iterations.copy()
    smooth[mask] = (iterations[mask] +1 - cp.log(cp.log(cp.abs(Z[mask])))/cp.log(2))
    return smooth

def compute_julia_gpu(width, height, x_min, x_max, y_min, y_max, max_iter,c):
    xs = cp.linspace(x_min,x_max,width,False,False,float)
    ys = cp.linspace(y_min,y_max,height,False,False,float)
    X,Y = cp.meshgrid(xs,ys)
    Z=X + 1j*Y
    C=cp.full(Z.shape,c)
    iterations = cp.full(Z.shape,max_iter,dtype=cp.float64)
    mask = cp.ones(C.shape, dtype=bool)
    for i in range(max_iter):
        Z[mask]=Z[mask]**2 +C[mask]
        new_div=mask & (cp.abs(Z)>2)
        iterations[new_div]= i+1
        mask[new_div] = False
    mask = ~mask
    smooth = iterations.copy()
    smooth[mask] = (iterations[mask] +1 - cp.log(cp.log(cp.abs(Z[mask])))/cp.log(2))
    return smooth
