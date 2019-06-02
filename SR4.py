# Carlos Calderon, 15219
# SR4 Flat Shading
# Program that renders an obj of blender into simple lines filled with gray
# In this case is an simple mushroom of mario bros game


from SR1 import SoftwareRender
import cProfile
def main():
    print("With barycentric")
    x = SoftwareRender('out.bmp')
    x.glCreateWindow(800, 600)
    x.glViewPort(0, 0, 800, 600)
    x.glClear()
    x.glColor(1, 0, 0)
    x.glVertex(0, 0)
    # Render the mushroom with flat shading
    x.load('./models/mushroom.obj', (8.5, 4, 0), (45, 45, 40),False)
    x.glFinish()
# Render the mushroom only zbuffer
"""
x2 = SoftwareRender('outz.bmp')
x2.glCreateWindow(800, 600)
x2.glViewPort(0, 0, 800, 600)
x2.glClear()
x2.glColor(1, 0, 0)
x2.glVertex(0, 0)
x2.load('./models/mushroom.obj', (8.5, 4, 0), (45, 45, 40),True)
x2.glFinish()
"""
cProfile.run('main()')