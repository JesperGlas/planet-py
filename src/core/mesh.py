from core.object3D import Object3D
from OpenGL.GL import *
from core.attribute import Attribute
from material.material import Material
from geometry.geometry import Geometry

class Mesh(Object3D):
    
    def __init__(self, geometry: Geometry, material: Material):
        super().__init__()
        
        self._Geometry: Geometry = geometry
        self._Material: Material = material

        # render flag
        self._Visible = True
        
        # set up association between attributes stored in geometry
        # and shader program stored in material
        self._Vao = glGenVertexArrays(1)
        glBindVertexArray(self._Vao)
        
        attribute_object: Attribute
        for variable_name, attribute_object in geometry.attributes.items():
            attribute_object.associateVariable(material.program_ref, variable_name)
        # unbind vao
        glBindVertexArray(0)