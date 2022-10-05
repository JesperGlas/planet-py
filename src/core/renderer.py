from OpenGL.GL import *
from core.mesh import Mesh
from core.camera import Camera
from core.scene import Scene
from core.uniform import Uniform

class Renderer:
    
    def __init__(self, clear_color=[0, 0, 0]):
        
        glEnable(GL_DEPTH_TEST)
        # required for anti aliasing
        glEnable(GL_MULTISAMPLE)
        glClearColor(
            clear_color[0],
            clear_color[1],
            clear_color[2])
    
    def render(self, scene: Scene, camera: Camera):
        
        # clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # update camera view (calculate inverse)
        camera.updateViewMatrix()
        
        # extract list of all Mesh objects in scene
        descendant_list = scene.getDescendantList()
        meshFilter = lambda x : isinstance(x, Mesh)
        mesh_list = list(filter(meshFilter, descendant_list))
        
        mesh: Mesh
        for mesh in mesh_list:
            
            # if this object is NOT visible
            # continure to nect object in list
            if not mesh._Visible:
                continue
            
            glUseProgram(mesh._Material._ProgramReference)

            # bind VAO
            glBindVertexArray(mesh._Vao)
            
            # update uniform values stored outside of material
            mesh._Material._Uniforms["u_model"]._Data = mesh.getWorldMatrix()
            mesh._Material._Uniforms["u_view"]._Data = camera._ViewMatrix
            mesh._Material._Uniforms["u_proj"]._Data = camera._ProjectionMatrix
            
            # update uniforms stored in material
            uniform_object: Uniform
            for variable_name, uniform_object in mesh._Material._Uniforms.items():
                uniform_object.uploadData()
                
            # update render settings
            mesh._Material.updateRenderSettings()
            
            glDrawArrays(mesh._Material._Settings["drawStyle"], 0, mesh._Geometry._VertexCount)