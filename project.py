from SR1 import SoftwareRender
from obj_loader import Texture

x = SoftwareRender('bosque2.bmp')
x.glCreateWindow(1280, 1280)
x.glViewPort(0, 0, 1280, 1280)
x.glClear()
t = Texture('./models/bosque6.bmp')
# print(t.pixels)
x.set_fondo(t.pixels)
t = Texture('./models/deertx.bmp')
x.load3("./models/deer2.obj", t, translate=(-1.2, -0.7, 0), scale=(0.15, 0.15, 0.15), rotate=(0, -0.5, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
t = Texture('./models/birdtx.bmp')
x.load3("./models/bird3.obj", t, translate=(0.97, 0.1, 0), scale=(0.15, 0.15, 0.15), rotate=(0, 0, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
t = Texture('./models/frogtx.bmp')
x.load3("./models/frog.obj", t, translate=(1.6, -0.87, 0), scale=(0.25, 0.25, 0.25), rotate=(0, 0.5, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
t = Texture('./models/raccoontx.bmp')
x.load3("./models/raccoon2.obj", t, translate=(-0.2, -0.65, -0.5), scale=(0.1, 0.1, 0.1), rotate=(0, 0, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
x.glFinish()

