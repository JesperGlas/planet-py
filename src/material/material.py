from typing import Dict
from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform
from OpenGL.GL import *

class Material:
    
    def __init__(self, vertex_shader_code, fragments_shader_code):
        
        self._ProgramReference = OpenGLUtils.initializeProgram(vertex_shader_code, fragments_shader_code)
        
        # store uniform objects indexed by name
        self._Uniforms: Dict[str, Uniform] = {}

        # adding typical uniforms
        # additionl uniforms added by extending classes
        self._Uniforms["u_model"] = Uniform("mat4", None)
        self._Uniforms["u_view"] = Uniform("mat4", None)
        self._Uniforms["u_proj"] = Uniform("mat4", None)

        # store OpenGL settings, indexed by variable name.
        # additional settings added by extending classes.
        self._Settings = {}
        self._Settings["drawStyle"] = GL_TRIANGLES
        
    def addUniform(self, data_type, variable_name, data):
        self._Uniforms[variable_name] = Uniform(data_type, data)
        
    def locateUniforms(self):
        for variable_name, uniform_object in self._Uniforms.items():
            uniform_object.locateVariable(self._ProgramReference, variable_name)
            
    def updateRenderSettings(self):
        pass

    def setProperties(self, properties: Dict):
        for name, data in properties.items():
            # update uniforms
            if name in self._Uniforms.keys():
                self._Uniforms[name]._Data = data
            # update settings
            elif name in self._Settings.keys():
                self._Settings[name] = data
            # unknown property type
            else:
                raise Exception(f"Material has no property named: {name}")