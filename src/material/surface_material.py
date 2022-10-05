from material.basic_material import BasicMaterial
from OpenGL.GL import *

class SurfaceMaterial(BasicMaterial):
    
    def __init__(self, properties={}):
        super().__init__()
        
        # render vertices as surface
        self._Settings["drawStyle"] = GL_TRIANGLES
        # render both sides? default: front side only
        self._Settings["doubleSide"] = False
        # render triangles as wireframe?
        self._Settings["wireFrame"] = False
        # line thickness for wireframe rendering
        self._Settings["lineWidth"] = 1
        
        self.setProperties(properties)
        
    def updateRenderSettings(self):

        if self._Settings["doubleSide"]:
            glDisable(GL_CULL_FACE)
        else:
            glEnable(GL_CULL_FACE)
            
        if self._Settings["wireFrame"]:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            
        glLineWidth(self._Settings["lineWidth"])