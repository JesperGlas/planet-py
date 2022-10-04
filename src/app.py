import glfw
from OpenGL.GL import *
from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute

class App(Base):
    
    def __init__(self, window_title="App Window"):
        super().__init__(window_title)
        
        vert_code = """
        in vec3 a_position;
        in vec3 a_color;

        out vec3 v_color;
        
        void main()
        {
            gl_Position = vec4(a_position, 1.0);
            v_color = a_color;
        }
        """

        frag_code ="""
        in vec3 v_color;
        
        out vec4 fragColor;

        void main()
        {
            fragColor = vec4(v_color, 1.0);
        }
        """
        
        self._ProgramRef = OpenGLUtils.initializeProgram(vert_code, frag_code)

        # set custom line width
        glLineWidth(4)
        glPointSize(10)
        
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)
        
        position_data = [
            [0.8, 0.0, 0.0],    [0.4, 0.6, 0.0],
            [-0.4, 0.6, 0.0],   [-0.8, 0.0, 0.0],
            [-0.4, -0.6, 0.0],  [0.4, -0.6, 0.0]
        ]
        self._VertCount = len(position_data)
        posAttrib = Attribute("vec3", position_data)
        posAttrib.associateVariable(self._ProgramRef, "a_position")
        
        color_data = [
            [1.0, 0.0, 0.0],    [1.0, 0.5, 0.0],
            [1.0, 1.0, 0.0],    [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],    [0.5, 0.0, 1.0]
        ]
        colorAttrib = Attribute("vec3", color_data)
        colorAttrib.associateVariable(self._ProgramRef, "a_color")
        
    def update(self):
        glUseProgram(self._ProgramRef)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self._VertCount)
        
    def keyboardEvents(self, window, key, scancode, action, mods):
        # super().keyboardEvents(window, key, scancode, action, mods)
        if action == glfw.PRESS:
            if key == glfw.KEY_ESCAPE:
                glfw.set_window_should_close(window, True)
        
App().run()