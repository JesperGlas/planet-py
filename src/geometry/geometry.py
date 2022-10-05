from typing import Dict
from core.attribute import Attribute

class Geometry(Attribute):
    
    def __init__(self):
        # store attribute objects indexed by name
        # of associated shader.
        self._Attributes: Dict[str, Attribute] = {}

        # number of vertices
        self._VertexCount = None
        
    def addAttribute(self, data_type, variable_name, data):
        self._Attributes[variable_name] = Attribute(data_type, data)
        
    def countVertices(self):
        first_attribute: Attribute = list(self._Attributes.values())[0]
        self._VertexCount = len(first_attribute._Data)