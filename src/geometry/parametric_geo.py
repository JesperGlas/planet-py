from turtle import position
from geometry.geometry import Geometry

class ParametricGeo(Geometry):
    
    def __init__(self, u_start, u_end, u_resolution, v_start, v_end, v_resolution, surface_func):

        # generate set of points on function
        delta_u = (u_end - u_start) / u_resolution
        delta_v = (v_end - v_start) / v_resolution
        positions = []

        for u_index in range(u_resolution +1):
            v_array = []
            for v_index in range(v_resolution +1):
                u = u_start + u_index * delta_u
                v = v_start + v_index * delta_v
                v_array.append(surface_func(u, v))
            positions.append(v_array)

        # store vertex data
        position_data = []
        color_data = []
        
        # default vertex colors
        c1, c2, c3 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
        c4, c5, c6 = [0, 1, 1], [1, 0, 1], [1, 1, 0]
        
        # group vertex data into triangle
        # note: copy() is necessary to avoid storing references
        for x_index in range(u_resolution):
            for y_index in range(v_resolution):
                # position data
                pA = positions[x_index +0][y_index +0]
                pB = positions[x_index +1][y_index +0]
                pD = positions[x_index +0][y_index +1]
                pC = positions[x_index +1][y_index +1]
                position_data += [pA.copy(), pB.copy(), pC.copy(), pA.copy(), pC.copy(), pD.copy()]
                color_data += [c1, c2, c3, c4, c5, c6]
                
        self.addAttribute("vec3", "a_position", position_data)
        self.addAttribute("vec3", "a_color", color_data)
        self.countVertices()