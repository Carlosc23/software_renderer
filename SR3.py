# Carlos Calderon, 15219
# SR3 Models
# Program that renders an obj of blender into simple lines
# In this case is an simple mushroom of mario bros game

from SR1 import SoftwareRender


xo, yo, xf, yf = -1, -1, 1, 1
x = SoftwareRender('out.bmp')
x.glCreateWindow(1000, 1000)
x.glViewPort(0, 0, 1000, 1000)
x.glClear()
x.glColor(1, 0, 0)
x.glVertex(0, 0)
# Render the mushroom
x.load('./models/Charmander-text2.obj', (4, 3), (100, 100))

x.glFinish()
