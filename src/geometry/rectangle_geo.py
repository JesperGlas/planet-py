from turtle import position
from geometry.geometry import Geometry

class RectangleGeo(Geometry):
    
    def __init__(self, width=1, height=1):
        super().__init__()
        
        p0 = [-width/2, -height/2]
        p1 = [width/2, -height/2]
        p2 = [-width/2, height/2]
        p3 = [width/2, height/2]
        
        c0, c1, c2, c3 = [1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]
        
        position_data = [p0, p1, p2, p0, p3, p2]
        color_data = [c0, c1, c3, c0, c3, c2]
        
        self.addAttribute("vec3", "a_position")
        self.addAttribute("vec3", "a_color")
        self.countVertices()