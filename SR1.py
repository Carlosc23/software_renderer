# Carlos Calderon, 15219
# SR1. py
# Module with a class Software Render that use bitmap to abstract a software render and use it to make a file
from Bitmap import *


class SoftwareRender(object):
    """
    Class that use bitmap to abstract a software render
    """

    def __init__(self, filename):
        self.glInit()
        self.filename = filename

    def glInit(self):
        """
        Function that start necessary variables for software renderer
        :return:
        """
        self.window = ""

    def glCreateWindow(self, width, height):
        """
        Function that instantiate a new Object from Bitmap, this initialize the framebuffer
        :param width: width of the image that will be render
        :param height: height of the the image that will be render
        :return:
        """
        self.window = Bitmap(width, height)

    def glViewPort(self, x, y, width, height):
        """
        Function that call glViewPort of Bitmap and create a viewport
        where the image will be visible
        :param x: number that represent the horizontal coord where the viewport will be drawn
        :param y: number that represent the vertical coord where the viewport will be drawn
        :param width: width of the viewport
        :param height: heigth of the viewport
        :return:
        """
        self.window.glViewPort(x, y, width, height)

    def glClear(self):
        """
        Function that use glclear() function from Bitmap
        :return:
        """
        self.window.glclear()

    def glClearColor(self, r, g, b):
        """
        Function that use glClearColor from Bitmap
        :param r: amount of red
        :param g: amount of green
        :param b: amount of blue
        :return:
        """
        self.window.glClearColor(r, g, b)

    def glVertex(self, x, y):
        """
         Function that use glVertex from Bitmap
        :param x: relative horizontal coord of the point
        :param y: relative vertical coord of the point
        :return:
        """
        self.window.glVertex(x, y)

    def glColor(self, r, g, b):
        """
        Function that use glColor from Bitmap
        :param r: amount of red
        :param g: amount of green
        :param b: amount of b
        :return:
        """
        self.window.glColor(r, g, b)

    def glFinish(self):
        """
        Function that use write method from Bitmap, it save the specifications of the image in a file with filename
        specified by the user
        :return:
        """
        self.window.write(self.filename)

    def square(self, size):
        self.window.square(size)

        # draw left line

    def drawLeftLine(self, padding):
        self.window.drawLeftLine(padding)

        # draw rigth line

    def drawRightLine(self, padding):
        self.window.drawRightLine(padding)

        # draw top line

    def drawTopLine(self, padding):
        self.window.drawTopLine(padding)

        # draw botton line

    def drawBottomLine(self, padding):
        self.window.drawBottomLine(padding)

    def diagonal(self):
        self.window.diagonal()

    def random_point(self):
        self.window.random_point()

    def random_point_color(self):
        self.window.random_point_color()

    def sky(self, stars):
        self.window.sky(stars)

    def glLine(self, xo, yo, xf, yf):
        self.window.glLine(xo, yo, xf, yf)

    def load(self, filename, translate, scale,zbuffer_flag,light=[0, 0, 1]):
        self.window.load(filename, translate, scale,zbuffer_flag,light)