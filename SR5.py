from SR1 import SoftwareRender
from obj_loader import Texture

x = SoftwareRender('out.bmp')
x.glCreateWindow(800, 600)
x.glViewPort(0, 0, 800, 600)
x.glClear()
# Render the mushroom with flat shading and texture
t = Texture('./models/mushroom2.bmp')
x.load('./models/mushroom.obj', (16, 9, 0), (25, 25, 1), False, [0, 0, 1], t)
x.glFinish()
