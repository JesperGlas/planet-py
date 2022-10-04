import glfw
from OpenGL.GL import *
from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from core.matrix import Matrix
from math import pi

class App(Base):
    
    def __init__(self, window_title="App Window"):
        super().__init__(window_title)
        
        vert_code = """
        uniform mat4 u_proj;
        uniform mat4 u_model;
        
        in vec3 a_position;
        
        void main()
        {
            gl_Position = u_proj * u_model * vec4(a_position, 1.0);
        }
        """

        frag_code ="""
        out vec4 fragColor;

        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """
        # create shader program
        self._ProgramRef = OpenGLUtils.initializeProgram(vert_code, frag_code)

        # render settings
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        
        # init and bind vertex array object
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)
        
        # vertex data
        position_data = [
            [0.0, 0.2, 0.0],
            [0.1, -0.2, 0.0], 
            [-0.1, -0.2, 0.0]
        ]
        self._VertCount = len(position_data)
        posAttrib = Attribute("vec3", position_data)
        posAttrib.associateVariable(self._ProgramRef, "a_position")

        # uniform data
        model_matrix = Matrix.makeTranslation(0, 0, -1)
        self._ModelMatrix = Uniform("mat4", model_matrix)
        self._ModelMatrix.locateVariable(self._ProgramRef, "u_model")
        
        projection_matrix = Matrix.makePerspective()
        self._ProjectionMatrix = Uniform("mat4", projection_matrix)
        self._ProjectionMatrix.locateVariable(self._ProgramRef, "u_proj")

        self._MoveSpeed = 0.5
        self._TurnSpeed = 90 * (pi/180)
        
    def update(self):
        delta = self.deltaTime()
        self._MoveAmount = self._MoveSpeed * delta
        self._TurnAmount = self._TurnSpeed * delta
        
        # render
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self._ProgramRef)
        self._ProjectionMatrix.uploadData()
        self._ModelMatrix.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self._VertCount)        

        
    def keyboardEvents(self, window, key, scancode, action, mods):
        # super().keyboardEvents(window, key, scancode, action, mods)
        if action == glfw.PRESS:
            if key == glfw.KEY_ESCAPE:
                glfw.set_window_should_close(window, True)
        
App().run()