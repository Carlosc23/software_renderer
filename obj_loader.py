# Carlos Calderon, 15219
# obj_loader. py
# Module based of Obj.py of Graphics course
# with a class obj_loader that is used to parse the vertex and faces in the blender obj file

class obj_loader(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        self.vertices = []
        self.vfaces = []
        self.read()

    def read(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    self.vfaces.append([list(map(int, face.split('/'))) for face in value.split(' ')])
