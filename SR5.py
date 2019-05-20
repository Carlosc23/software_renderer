# Carlos Calderon, 15219
# SR5 Textures
# Program that renders an obj of blender into simple lines filled with gray
# And also use a texture in bmp to apply on the model
# In this case is an simple mushroom of mario bros game



from SR1 import SoftwareRender
from obj_loader import Texture

x = SoftwareRender('out.bmp')
x.glCreateWindow(800, 600)
x.glViewPort(0, 0, 800, 600)
x.glClear()
# Render the mushroom with flat shading and texture
t = Texture('./models/Batman3tx.bmp')
#x.load('./models/mushroom.obj', (16, 9, 0), (25, 25, 1), False, [0, 0, 1], t)
x.load_img_texture('./models/bat.obj', (16, 9, 0), (25, 25, 1),t,[0, 0, 1])
x.glFinish()
