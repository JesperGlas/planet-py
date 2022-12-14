from core.object3D import Object3D
from core.matrix import Matrix
from numpy.linalg import inv

class Camera(Object3D):
    
    def __init__(self, angle_of_view=60, aspect_ratio=1, near=0.1, far=1000):
        super().__init__()
        self._ProjectionMatrix = Matrix.makePerspective(angle_of_view, aspect_ratio, near, far)
        self._ViewMatrix = Matrix.makeIdentity()

    def updateViewMatrix(self):
        self._ViewMatrix = inv(self.getWorldMatrix())