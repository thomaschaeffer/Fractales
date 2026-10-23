import numpy as np

colors= {"toxic" : [(255,255,0),(150,35,230),(150,35,230),(0,255,0),(0,230,0),(5,8,35),(5,8,8)],"sunset" : [(255,0,0),(255,128,0),(255,128,0),(255,255,0),(5,8,35)]}

def colorize(iterations, max_iter,palette,):

    palette = np.array(palette,dtype=float)

    row = len(iterations)
    column = len(iterations.T)
    A = np.zeros((row,column),dtype=float)
    for y in range(row):
        for x in range(column):
            A[y,x]= (1 - iterations[y,x]/max_iter)
    position = A * (len(palette)-1)
    index=np.minimum(position.astype(int),len(palette) -2)
    fraction = position - index

    rgb = palette[index] * (1-fraction[...,None])+ palette[index+1]*fraction[...,None]

    image = np.zeros((row,column,3),dtype=np.uint8)
    image[:]= np.clip(rgb,0,255).astype(np.uint8)

    image[iterations >= max_iter] = (0,0,0)
    return image


