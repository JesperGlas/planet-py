from typing import List
from core.matrix import Matrix

class Object3D(Matrix):
    
    def __init__(self):
        self._Transform = Matrix.makeIdentity()
        self._Parent: Object3D = None
        self._Children: List[Object3D] = []
        
    def add(self, child):
        self._Children.append(child)
        child._Parent = self
    
    def remove(self, child):
        self._Children.remove(child)
        child._Parent = None
        
    def getWorldMatrix(self):
        if self._Parent == None:
            return self._Transform
        else:
            return self._Parent.getWorldMatrix() @ self._Transform
        
    def getDescendantList(self):
        descendants = []
        nodes_to_process = [self]
        while len(nodes_to_process) > 0:
            node = nodes_to_process.pop(0)
            descendants.append(node)
            nodes_to_process = node._Children + nodes_to_process
        
        return descendants
    
    def applyMatrix(self, matrix: Matrix, local_coord=True):
        if local_coord:
            self._Transform = self._Transform @ matrix
        else:
            self._Transform = matrix @ self._Transform
            
    def translate(self, x, y, z, local_coord=True):
        m = Matrix.makeTranslation(x, y, z)
        self.applyMatrix(m, local_coord)
        
    def rotateX(self, angle, local_coord=True):
        m = Matrix.makeRotationX(angle)
        self.applyMatrix(m, local_coord)
        
    def rotateY(self, angle, local_coord=True):
        m = Matrix.makeRotationY(angle)
        self.applyMatrix(m, local_coord)
        
    def rotateZ(self, angle, local_coord=True):
        m = Matrix.makeRotationZ(angle)
        self.applyMatrix(m, local_coord)
        
    def scale(self, s, local_coord=True):
        m = Matrix.makeScale(s)
        self.applyMatrix(m, local_coord)
        
    def getPosition(self):
        return [
            self._Transform.item((0, 3)),
            self._Transform.item((1, 3)),
            self._Transform.item((2, 3)),
        ]
        
    def getWorldPosition(self):
        world_transform = self.getWorldMatrix()
        return [
            world_transform.item((0, 3)),
            world_transform.item((1, 3)),
            world_transform.item((2, 3))
        ]
        
    def setPosition(self, position):
        self._Transform.itemset((0, 3), position[0])
        self._Transform.itemset((1, 3), position[1])
        self._Transform.itemset((2, 3), position[2])

    