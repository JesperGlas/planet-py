import glfw
from OpenGL.GL import *
from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.box_geo import BoxGeo
from material.surface_material import SurfaceMaterial

class App(Base):
    
    def __init__(self, window_title="App Window"):
        super().__init__(window_title, screen_size=(800, 600))
        
        self._Renderer = Renderer()
        self._Scene = Scene()
        self._Camera = Camera(aspect_ratio=800/600)
        self._Camera.setPosition([0, 0, 4])
        
        geometry = BoxGeo()
        material = SurfaceMaterial(
            {"u_useVertexColors": True}
        )
        self._Mesh = Mesh(geometry, material)
        self._Scene.add(self._Mesh)
        
    def update(self):
        self._Mesh.rotateY(0.0514)
        self._Mesh.rotateX(0.0337)
        self._Renderer.render(self._Scene, self._Camera)     

        
    def keyboardEvents(self, window, key, scancode, action, mods):
        # super().keyboardEvents(window, key, scancode, action, mods)
        if action == glfw.PRESS:
            if key == glfw.KEY_ESCAPE:
                glfw.set_window_should_close(window, True)
        
App().run()