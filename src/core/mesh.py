from core.object3D import Object3D
from OpenGL.GL import *
from core.attribute import Attribute

class Mesh(Object3D):
    
    def __init__(self, geometry, material):
        super().__init__()
        
        self._Geometry = geometry
        self._Material = material

        # render flag
        self._Visible = True
        
        # set up association between attributes stored in geometry
        # and shader program stored in material
        self._Vao = glGenVertexArrays(1)
        glBindVertexArray(self._Vao)
        for variable_name, attribute_object in geometry.attributes.items():
            attribute_object.associateVariable(material.program_ref, variable_name)
        # unbind vao
        glBindVertexArray(0)