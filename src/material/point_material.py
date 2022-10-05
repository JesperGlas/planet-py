from material.basic_material import BasicMaterial
from OpenGL.GL import *

class PointMaterial(BasicMaterial):
    
    def __init__(self, properties={}):
        super().__init__()
        
        # render vertices as points
        self._Settings["drawStyle"] = GL_POINTS
        # width and height of points, in pixels
        self._Settings["pointSize"] = 8
        # draw points as rounded
        self._Settings["roundedPoints"] = False
        
        self.setProperties(properties)
        
    def updateRenderSettings(self):
        glPointSize(self._Settings["pointSize"])
        if self._Settings["roundedPoints"]:
            glEnable(GL_POINT_SMOOTH)
        else:
            glDisable(GL_POINT_SMOOTH)