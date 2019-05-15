from SR1 import SoftwareRender
from obj_loader import Texture


x = SoftwareRender('space.bmp')
x.glCreateWindow(2420, 1480)
x.glViewPort(0, 0, 2420, 1480)
x.glClear()

x.load_shader('./models/planet.obj', (13.5, 10, 0), (65, 65, 40),False)
x.set_planet(False)
x.load_shader('./models/moon.obj', (61.5, 36, 0), (22, 22, 20),False)
x.load_shader('./models/moon.obj', (95.5, 26, 0), (13, 13, 20),False)
x.glFinish()