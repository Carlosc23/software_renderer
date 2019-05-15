from SR1 import SoftwareRender
from obj_loader import Texture


x = SoftwareRender('space.bmp')
x.glCreateWindow(2720, 1680)
x.glViewPort(0, 0, 2720, 1680)
#x.glColor(1, 1, 0)
#x.glClearColor(1, 1, 0)
x.glClear()
#x.load2('./models/planet.obj', (0, 0, 0), (0.1, 0.15, 0.1),(0, 0, 0),[0, 0.75, 1.5],[20, 1, 20],[0, 0, 0],[0, 1, 0])
#x.set_planet(False)
#x.load2('./models/moon.obj', (0.8, 0.3, 0), (0.02, 0.03, 0.02),(0, 0, 0),[0, 0.75, 1.5],[0, 0,0],[0, 0, 0],[0, 0, 0])
#x.load2('./models/moon.obj', (0.7, -0.3, 0), (0.015, 0.008, 0.01),(0.015, 0.008, 0.01),[0, 0.75, 1.5],[0, 0, 0],[0, 0, 0],[0, 0, 0])

x.load_shader('./models/planet.obj', (13.5, 10, 0), (70, 70, 40),False)
x.set_planet(False)
x.load_shader('./models/moon.obj', (63.5, 36, 0), (22, 22, 20),False)
x.load_shader('./models/moon.obj', (98.5, 26, 0), (13, 13, 20),False)
x.glFinish()