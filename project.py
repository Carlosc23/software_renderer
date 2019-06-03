from SR1 import SoftwareRender
from obj_loader import Texture

x = SoftwareRender('bosqueshaders.bmp')
x.glCreateWindow(1280, 1280)
x.glViewPort(0, 0, 1280, 1280)
x.glClear()
t = Texture('./models/bosque7.bmp')
print(t.pixels)
x.set_fondo(t.pixels)
# Agregar modelos
x.set_name("Deer")
t = Texture('./models/deertx.bmp')
x.load4("./models/deer2.obj", t, translate=(-1.3, -0.7, 0), scale=(0.15, 0.15, 0.15), rotate=(0, -0.5, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
x.set_name("Deer2")
t = Texture('./models/deertx.bmp')
x.load4("./models/deer2.obj", t, translate=(-1.0, -0.7, 0), scale=(0.09, 0.09, 0.09), rotate=(0, -0.5, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
x.set_name("Bird")
t = Texture('./models/birdtx.bmp')
x.load4("./models/bird3.obj", t, translate=(0.97, 0.1, 0), scale=(0.15, 0.15, 0.15), rotate=(0, 0, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
x.set_name("Bird2")
t = Texture('./models/birdtx.bmp')
x.load4("./models/bird3.obj", t, translate=(0.87, 0.1, 0), scale=(0.10, 0.10, 0.10), rotate=(0, 0, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
x.set_name("frog")
t = Texture('./models/frogtx.bmp')
x.load3("./models/frog.obj", t, translate=(1.6, -0.87, 0), scale=(0.25, 0.25, 0.25), rotate=(0, 0.5, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
x.set_name("raccoon")
t = Texture('./models/raccoontx.bmp')
x.load4("./models/raccoon2.obj", t, translate=(-0.2, -0.65, -0.5), scale=(0.1, 0.1, 0.1), rotate=(0, 0, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
t = Texture('./models/monkeytx.bmp')
x.load3("./models/monkey3.obj", t, translate=(0.3, 0, 0), scale=(0.2, 0.2, 0.2), rotate=(1.2, 0, 0),
        light=[0, 0.75, 1.5], eye=[0, 0, 1], center=[0, 0, 0],
        up=[0, 1, 0])
x.glFinish()


