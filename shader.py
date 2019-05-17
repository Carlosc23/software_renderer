from SR1 import SoftwareRender
from obj_loader import Texture

x = SoftwareRender('space4.bmp')
x.glCreateWindow(2520, 1680)
x.glViewPort(0, 0, 2520, 1680)
# x.glColor(1, 1, 0)
# x.glClearColor(1, 1, 0)
x.glClear()
x.glColor(1, 1, 1)
x.sky(200)
x.load2('./models/planet.obj', (-0.31, -0.42, 0), (0.1, 0.12, 0.1), (0, 0, 0), [0, 0.75, 1.5], [20, 1, 20], [0, 0, 0],
        [0, 0.5, 0])
x.set_planet(False)
x.load_shader('./models/moon.obj', (69.5, 36, 0), (22, 22, 20), False)
x.load_shader('./models/moon.obj', (115.5, 26, 0), (13, 13, 20), False)
x.glFinish()
