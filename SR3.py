# Carlos Calderon, 15219
# SR3 Models
# Program that renders an obj of blender into simple lines
# In this case is an simple mushroom of mario bros game

from SR1 import SoftwareRender


xo, yo, xf, yf = -1, -1, 1, 1
x = SoftwareRender('out.bmp')
x.glCreateWindow(800, 600)
x.glViewPort(0, 0, 800, 600)
x.glClear()
x.glColor(1, 0, 0)
x.glVertex(0, 0)
# Render the mushroom
x.load('./models/mushroom.obj', (10, 2, 0), (45, 40, 40))

x.glFinish()
