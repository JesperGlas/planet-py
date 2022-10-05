from material.basic_material import BasicMaterial
from OpenGL.GL import *

class LineMaterial(BasicMaterial):
    
    def __init__(self, properties={}):
        super().__init__(self, properties={})
        
        # render verticies as continues lines
        self._Settings["drawStyle"] = GL_LINE_STRIP
        # line thickness
        self._Settings["lineWidth"] = 1
        # line type: "connected" | "loop" | "segments"
        self._Settings["lineType"] = "connected"
        
        self.setProperties(properties)
        
    def updateRenderSettings(self):
        glLineWidth(self._Settings["lineWidth"])
        
        if self._Settings["lineType"] == "connected":
            self._Settings["drawStyle"] = GL_LINE_STRIP
        elif self._Settings["lineType"] == "loop":
            self._Settings["drawStyle"] = GL_LINE_LOOP
        elif self._Settings["lineType"] == "segments":
            self._Settings["drawStyle"] = GL_LINES
        else:
            raise Exception("Unknown LineMaterial draw style.")