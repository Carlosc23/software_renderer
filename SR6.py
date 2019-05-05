from SR1 import SoftwareRender
from obj_loader import Texture

def medium():
    x = SoftwareRender('out.bmp')
    x.glCreateWindow(800, 600)
    x.glViewPort(0, 0, 800, 600)
    x.glClear()
    t = Texture('./models/mushroom2.bmp')
    x.load_img_texture2('./models/mushroom.obj', (16, 9, 0), (25, 25, 1), t, [0, 0, 1],[0,0,1],[0,0,0],[0,1,0])
    x.glFinish()

def low():
    pass

def dutch():
    pass

def high():
    pass

medium()