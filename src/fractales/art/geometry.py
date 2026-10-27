import math
import numpy as np

def polar_to_cartesian(center,radius,angle):
    cx,cy = center
    x =cx + radius*math.cos(angle)
    y= cy + radius * math.sin(angle)
    return (x,y)

def rotate_point(point,center,angle):
    cx,cy = center
    mx,my=point
    x=cx + (mx-cx)*math.cos(angle)-(my-cy)*math.sin(angle)
    y=cy + (mx-cx)*math.sin(angle)+(my-cy)*math.cos(angle)
    return (x,y)

def cubic_bezier(p0,p1,p2,p3,samples=50):
    B=[]
    for i in np.linspace(0,1,samples):
        x =  (1-i)**3 * p0[0] + 3*(1-i)**2 *i* p1[0] + 3*(1-i) * i**2 * p2[0] + i**3 * p3[0]
        y =  (1-i)**3 * p0[1] + 3*(1-i)**2 *i* p1[1] + 3*(1-i) * i**2 * p2[1] + i**3 * p3[1]
        B.append((x,y))
    return B