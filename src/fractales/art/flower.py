import math
from fractales.art.motifs import make_petal_path

def draw_flower(draw,center,petals=10,radius=250,width=38,rotation=0.0):
    root_radius = radius *0.15
    tip_radius = radius

    for i in range(petals):
        angle = rotation +2*math.pi*i/petals
        path = make_petal_path(center=center,angle=angle,root_radius=root_radius,tip_radius=tip_radius,half_width=width)
        draw.polygon(path,fill=(35,20,65))