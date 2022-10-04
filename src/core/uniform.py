from OpenGL.GL import *

class Uniform:
    
    def __init__(self, data_type, data):
        
        # supported data types
        # int | float | vec2 | vec3 | vec4
        self._DataType = data_type
        
        # set uniform data
        self._Data = data
        
        # reference for data in program
        self._VariableReference = None
        
    # get and store reference for program variable with given name
    def locateVariable(self, program_ref, variable_name):
        self._VariableReference = glGetUniformLocation(program_ref, variable_name)
        
    def uploadData(self):
        # if program does not reference variable, raise error
        if self._VariableReference == -1:
            raise RuntimeError(f"Variable not references...")
        if self._DataType == "int":
            glUniform1i(self._VariableReference, self._Data)
        elif self._DataType == "bool":
            glUniform1i(self._VariableReference, self._Data)
        elif self._DataType == "float":
            glUniform1f(self._VariableReference, self._Data)
        elif self._DataType == "vec2":
            glUniform2f(self._VariableReference, self._Data[0], self._Data[1])
        elif self._DataType == "vec3":
            glUniform3f(self._VariableReference, self._Data[0], self._Data[1], self._Data[2])
        elif self._DataType == "vec4":
            glUniform4f(self._VariableReference, self._Data[0], self._Data[1], self._Data[2], self._Data[3])
        elif self._DataType == "mat4":
            glUniformMatrix4fv(self._VariableReference, 1, GL_TRUE, self._Data)