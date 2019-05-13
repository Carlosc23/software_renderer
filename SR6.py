from SR1 import SoftwareRender
from obj_loader import Texture


def medium():
    x = SoftwareRender('medium.bmp')
    x.glCreateWindow(800, 600)
    x.glViewPort(0, 0, 800, 600)
    x.glClear()
    t = Texture('./models/mushroom2.bmp')
    x.load2("./models/mushroom.obj", (-0.05, -0.45, 0), (1.2, 1.2, 1.2), (0, 0, 0), [0, 0.75, 1.5], [0.1, 0.5, 1],
            [0, 0.5, 0],
            [0, 1, 0])
    x.glFinish()


def low():
    x = SoftwareRender('low.bmp')
    x.glCreateWindow(800, 600)
    x.glViewPort(0, 0, 800, 600)
    x.glClear()
    t = Texture('./models/mushroom2.bmp')
    x.load2("./models/mushroom.obj", (-0.05, -0.45, 0), (0.8, 0.8, 0.8), (-1.15, 0.2, -0.05), [0, 0.75, 1.5],
            [0.1, 0.5, 1], [0, -0.3, 0.2],
            [0, 1, 0])
    x.glFinish()


def high():
    x = SoftwareRender('high.bmp')
    x.glCreateWindow(800, 600)
    x.glViewPort(0, 0, 800, 600)
    x.glClear()
    t = Texture('./models/mushroom2.bmp')
    x.load2("./models/mushroom.obj", (-0.05, -0.8, 0), (0.8, 0.8, 0.8), (0, 0.5, 0), [0, 0.75, 1.5], [0, 1.7, 1.5],
            [0, 0, 0],
            [0, 1, 0])
    x.glFinish()


def base():
    x = SoftwareRender('high.bmp')
    x.glCreateWindow(800, 600)
    x.glViewPort(0, 0, 800, 600)
    x.glClear()
    x.load2("./models/mushroom.obj", (0, 0, 0), (0.5, 0.5, 0.5), (0, 0, 0), [0, 0.75, 1.5], [0.1, 0.5, 1], [0, 0, 0],
            [0, 1, 0])


def dutch():
    x = SoftwareRender('dutch.bmp')
    x.glCreateWindow(800, 600)
    x.glClear()
    x.glViewPort(0, 0, 800, 600)
    #x.load2("./models/mushroom.obj", (-0.05, -0.15, 0), (1, 0.8, 1), (0.2, 0.5, 0.5), [0, 0.75, 1.5], [0, 0, 1], [0.05, 0.2, 0.1],
    #        [0.1, 0.1, 0])
    x.load2("./models/mushroom.obj", (0, 0, 0), (0.8, 0.8, 0.8), (0, 0, 0), [0, 0.75, 1.5], [0.1, 0.5, 1], [-0.2, 0.2, 0],
            [0.1, 0.1, 0])
    x.glFinish()

dutch()
