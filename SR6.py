from SR1 import SoftwareRender
from obj_loader import Texture

x = SoftwareRender('bosque.bmp')
x.glCreateWindow(1800,993)
x.glViewPort(0, 0, 1800,993)
x.glClear()
t = Texture('./models/bosque6.bmp')
#print(t.pixels)
x.set_fondo(t.pixels)
x.glFinish()
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
    print("mario")
    x = SoftwareRender('mario.bmp')
    x.glCreateWindow(800, 600)
    x.glViewPort(0, 0, 800, 600)
    x.glClearColor(1,1,1)
    x.glClear()
    x.load2("./models/Mariop.obj", (0, -0.5, 0), (0.5, 0.5, 0.5), (0, 0, 0), [0, 0.75, 1.5], [0.1, 0.5, 1], [0, 0, 0],
            [0, 1, 0])
    x.glFinish()

def base2():
    print("mario")
    x = SoftwareRender('mario2.bmp')
    x.glCreateWindow(800, 600)
    x.glViewPort(0, 0, 800, 600)
    #x.glClearColor(1,1,1)
    x.glClear()
    t = Texture('./models/Color.bmp')
    x.load_img_texture('./models/Orange.obj', (0.4, -0.5, 0), (0.2, 0.2, 0.5), t, [1, 0, 1])
    #x.load('./models/spiderman2.obj', (200.5, 100.5, 0), (3.5, 2.5, 1), False)
    #load("spiderman2.obj", translate=(0, -0.8, 0), scale=(0.2, 0.2, 0.5), rotate=(0, 0, 0), eye=[0, 0, 7],
    #     center=[0, 0.5, -0.11], up=[0, 1, 0])
    #x.load2("./models/Orange.obj", (0, -0.8, 0), (0.2, 0.2, 0.5), (0, 0, 0), [0, 0.75, 1.5], [0, 0, 7], [0, 0.5, -0.11],
    #        [0, 1, 0])
    x.glFinish()

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

#base2()
