import math
from fractales.art.geometry import polar_to_cartesian,cubic_bezier

def make_petal_path(center,angle,root_radius,tip_radius,half_width,curvature=1.9,samples=40):
    perpendicular = (-math.sin(angle),math.cos(angle))

    root=polar_to_cartesian(center,root_radius,angle)

    root_left = ( root[0] - half_width * perpendicular[0],root[1] - half_width * perpendicular[1])
    root_right = ( root[0] + half_width * perpendicular[0],root[1] + half_width * perpendicular[1])

    tip = polar_to_cartesian(center, tip_radius,angle)

    control_distance = (tip_radius - root_radius)* curvature

    control_left_1 = (root_left[0]+ control_distance * math.cos(angle), root_left[1]+ control_distance*math.sin(angle))
    control_left_2 = (tip[0] -control_distance * math.cos(angle) - half_width*perpendicular[0], tip[1]- control_distance*math.sin(angle)-half_width*perpendicular[1])

    control_right_1 = (root_right[0]+ control_distance * math.cos(angle), root_right[1]+ control_distance*math.sin(angle))
    control_right_2 = (tip[0] -control_distance * math.cos(angle) + half_width*perpendicular[0], tip[1]- control_distance*math.sin(angle)+half_width*perpendicular[1])

    side_left = cubic_bezier(root_left,control_left_1,control_left_2,tip,samples)
    side_right=cubic_bezier(tip,control_right_2,control_right_1,root_right,samples)

    return side_left+side_right[1:]
    