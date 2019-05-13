# Carlos Calderon, 15219
# Bitmap.py
# Inspired in the class render made in Graphics Course C3044
import math
import random
import sys
from math import ceil
from utils import *
from math_op import *
from obj_loader import Obj as obj_loader


class Bitmap(object):
    """
    Class that abstract a bitmap
    """

    def __init__(self, width, height):
        """
        Constructor that initialize necessary variables for
        render images
        :param width: width of the image that will be render
        :param height: height of the image that will be render
        """
        self.width = width
        self.height = height
        self.pixels = []
        self.r = 0
        self.g = 0
        self.b = 0
        self.pointSize = 30
        self.vr = 255
        self.vg = 200
        self.vb = 200
        self.zbuffer_flag = False
        self.View = 0
        self.projection = 0
        self.model = 0
        self.viewPort = 0
        self.glclear()

    def glclear(self):
        """
        Fill the the pixels object with a color
        :return:
        """
        self.pixels = [
            [color(self.r, self.g, self.b) for x in range(self.width)]
            for y in range(self.height)
        ]
        self.zbuffer = [
            [-float('inf') for x in range(self.width)]
            for y in range(self.height)
        ]

        self.zbuffer_color = [
            [color(0, 0, 0) for x in range(self.width)]
            for y in range(self.height)
        ]

    def fill_zbuffer_color(self):
        max_z_value = max([max(r) for r in self.zbuffer])
        for x in range(self.height):
            for y in range(self.width):
                color_zbuffer = int(self.zbuffer[x][y] * 255 / max_z_value) if self.zbuffer[x][y] > 0 else 0
                try:
                    self.zbuffer_color[y][x] = color(color_zbuffer, color_zbuffer, color_zbuffer)
                except:
                    pass

    def glViewPort(self, x, y, width, height):
        """
        Define the area of the image where the glVertex will draw
        :param x: number that represent the horizontal coord where the viewport will be drawn
        :param y: number that represent the vertical coord where the viewport will be drawn
        :param width: width of the viewport
        :param height: heigth of the viewport
        :return:
        """
        if height <= 0 or width <= 0:
            print('Height and width must be positives')
        elif x < 0 or y < 0 or x > self.width or y > self.height:
            print('x and y must be positives and smaller tha height and width')
        else:
            self.vpWidth = width
            self.vpHeight = height
            self.vpX = x
            self.vpY = y

    def glClearColor(self, r, g, b):
        """
        change the default colors that uses glClear to fill
        :param r: amount of red
        :param g: amount of green
        :param b: amount of blue
        :return:
        """
        if 0 <= r <= 1 or 0 <= g <= 1 or 0 <= b <= 1:
            self.r = ceil(r * 255)
            self.g = ceil(g * 255)
            self.b = ceil(b * 255)
        else:
            print("Please insert numbers between 0 and 1")
            sys.exit()

    def glVertex(self, x, y):
        """
        Change the color of a point of the screen, relative to ViewPort
        :param x: relative horizontal coord of the point
        :param y: relative vertical coord of the point
        :return:
        """

        if self.vpHeight != 0 and self.vpWidth != 0:
            xx = x * ((self.vpWidth - self.pointSize) / 2)
            yy = y * ((self.vpHeight - self.pointSize) / 2)
            localX = self.vpX + int((self.vpWidth - self.pointSize) / 2) + int(xx)
            localY = self.vpY + int((self.vpHeight - self.pointSize) / 2) + int(yy)

            for x in range(self.pointSize):
                for y in range(self.pointSize):
                    self.point(localX + x, localY + y, color(self.vr, self.vb, self.vg))
        else:
            print('Initialize glViewPort')
            sys.exit()

    def set_point_size(self, pointSize):
        """
        change the size of the global point, default is 5
        :param pointSize: size of the class point
        :return:
        """
        self.pointSize = pointSize

    def glColor(self, r, g, b):
        """
        Change the color of glVertex
        :param r: amount of red
        :param g: amount of green
        :param b: amount of b
        :return:
        """
        if 0 <= r <= 1 or 0 <= g <= 1 or 0 <= b <= 1:
            self.vr = ceil(r * 255)
            self.vg = ceil(g * 255)
            self.vb = ceil(b * 255)
        else:
            print("Please insert numbers between 0 and 1")
            sys.exit()

    def write(self, filename):
        """
        Save the image in a file
        :param filename: name of the file that will be saved
        :return:
        """

        f = open(filename, 'wb')

        # file header (14)
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # image header (40)
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        # f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        if self.zbuffer_flag:
            self.fill_zbuffer_color()
            for x in range(self.height):
                for y in range(self.width):
                    f.write(self.zbuffer_color[x][y])
        else:
            for x in range(self.height):
                for y in range(self.width):
                    f.write(self.pixels[x][y])
        f.close()

    def point(self, x, y, color=None):
        """
        function that fills a pixel of a color
        :param x: position of the pixel
        :param y: position of the pixel
        :param color: color that will fill the pixel
        :return:
        """
        try:
            self.pixels[y][x] = color or color(255, 255, 255)
        except:
            # To avoid index out of range exceptions
            pass

    def square(self, size):
        cordx = int((self.vpWidth / 2)) - int(size / 2)
        cordy = int((self.vpWidth / 2)) - int(size / 2)
        for x in range(cordx, cordx + size):
            for y in range(cordy, cordy + size):
                self.point(x, y)

    def drawLeftLine(self, padding):
        x = padding
        for y in range(padding, self.vpHeight - padding):
            self.point(x, y)

    def drawRightLine(self, padding):
        x = self.vpWidth - padding
        for y in range(padding, self.vpHeight - padding):
            self.point(x, y)

    def drawTopLine(self, padding):
        y = padding
        for x in range(padding, self.vpWidth - padding):
            self.point(x, y)

    def drawBottomLine(self, padding):
        y = self.vpHeight - padding
        for x in range(padding, self.vpWidth - padding):
            self.point(x, y)

    def diagonal(self):
        for cord in range(self.vpX, self.vpWidth):
            self.point(cord, cord)

    def random_point(self):
        whiteColor = [1, 1, 1]
        blackColor = [0, 0, 0]
        for y in range(self.height):
            for x in range(self.width):
                self.glColor(*random.choice([whiteColor, blackColor]))
                self.point(x, y, color(self.vr, self.vg, self.vb))

    def random_point_color(self):

        for y in range(self.height):
            for x in range(self.width):
                list_random = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                list_random_norm = [float(i) / 255 for i in list_random]
                self.glColor(list_random_norm[0], list_random_norm[1], list_random_norm[2])
                self.point(x, y, color(self.vr, self.vg, self.vb))

    def sky(self, stars):
        counter = 0
        while counter < stars:
            counter += 1
            size = random.randint(1, 3)
            x = random.randint(0, self.vpWidth - size - 2)
            y = random.randint(0, self.vpHeight - size - 2)
            self.printStar(x, y, size)

    def printStar(self, x, y, size):
        for cordX in range(size):
            for cordY in range(size):
                self.point(cordX + x, cordY + y)

    def transform_x(self, x):
        dx = x * (self.vpWidth / 2)
        realX_vp_size = (self.vpWidth / 2) + dx
        realX = realX_vp_size + self.vpX
        return realX

    def transform_y(self, y):
        dy = y * (self.vpHeight / 2)
        realY_vp_size = (self.vpHeight / 2) + dy
        realY = realY_vp_size + self.vpY
        return realY

    def transform_xn(self, realX):
        """
        This method transform a x coord into a normalized coord
        :param realX: x coord
        :return: x normalized coord
        """
        realX_vp_size = realX - self.vpX
        dx = realX_vp_size - ((self.vpWidth / 2))
        x = dx / (self.vpWidth / 2)
        return x

    def transform_yn(self, realY):
        """
        This method transform a y coord into a normalized coord
        :param realY: y coord
        :return: y normalized coord
        """
        realY_vp_size = realY - self.vpY
        dy = realY_vp_size - ((self.vpHeight / 2))
        y = dy / (self.vpHeight / 2)
        return y

    def glLine(self, xo, yo, xf, yf):
        """
                This method transform coords on a line with bresenham
                :param xo: initial x
                :param yo: initial y
                :param xf: final x
                :param yf final y
                """

        x1 = math.floor(self.transform_x(xo))
        x2 = math.floor(self.transform_x(xf))
        y1 = math.floor(self.transform_y(yo))
        y2 = math.floor(self.transform_y(yf))

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)
        if dx == 0:
            print("Undefined slope")
            # sys.exit()
        steep = dy > dx

        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

        offset = 0 * 2 * dx
        threshold = 0.5 * 2 * dx

        y = y1
        for x in range(x1, x2 + 1):
            if steep:
                self.point(y, x)
            else:
                self.point(x, y)

            offset += dy * 2
            if offset >= threshold:
                y += 1 if y1 < y2 else -1
                threshold += 1 * 2 * dx

    def transform_img(self, coords, translate=(0, 0, 0), scale=(1, 1, 1)):
        """
        This method transform in size and in coords the original image
        :param coords: The original coords of the vertex
        :param translate: the params that translates the vertex
        :param scale: the params that make bigger or smaller the vertex
        :return: the coords transformated
        """
        x1, y1, z1, x2, y2, z2, x3, y3, z3 = coords

        x1 = math.floor((x1 + translate[0]) * scale[0])
        y1 = math.floor((y1 + translate[1]) * scale[1])
        z1 = math.floor((z1 + translate[2]) * scale[2])

        x2 = math.floor((x2 + translate[0]) * scale[0])
        y2 = math.floor((y2 + translate[1]) * scale[1])
        z2 = math.floor((z2 + translate[2]) * scale[2])

        x3 = math.floor((x3 + translate[0]) * scale[0])
        y3 = math.floor((y3 + translate[1]) * scale[1])
        z3 = math.floor((z3 + translate[2]) * scale[2])

        return x1, y1, z1, x2, y2, z2, x3, y3, z3

    def transform_img2(self, coords, translate=(0, 0, 0), scale=(1, 1, 1)):
        """
        This method transform in size and in coords the original image
        :param coords: The original coords of the vertex
        :param translate: the params that translates the vertex
        :param scale: the params that make bigger or smaller the vertex
        :return: the coords transformated
        """
        x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = coords
        x1 = math.floor((x1 + translate[0]) * scale[0])
        y1 = math.floor((y1 + translate[1]) * scale[1])
        z1 = math.floor((z1 + translate[2]) * scale[2])

        x2 = math.floor((x2 + translate[0]) * scale[0])
        y2 = math.floor((y2 + translate[1]) * scale[1])
        z2 = math.floor((z2 + translate[2]) * scale[2])

        x3 = math.floor((x3 + translate[0]) * scale[0])
        y3 = math.floor((y3 + translate[1]) * scale[1])
        z3 = math.floor((z3 + translate[2]) * scale[2])

        x4 = math.floor((x4 + translate[0]) * scale[0])
        y4 = math.floor((y4 + translate[1]) * scale[1])
        z4 = math.floor((z4 + translate[2]) * scale[2])

        return x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4

    def multiplicacion(self, matriz1, matriz2):
        matrizR = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for x in range(0, 4):
            for y in range(0, 4):
                for z in range(0, 4):
                    matrizR[x][y] += matriz1[x][z] * matriz2[z][y]
        return matrizR

    def loadProjectionMatriz(self, coef):
        self.projection = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, coef, 1]
        ]

    def loadViewMatriz(self, x, y, z, center):
        M = [
            [x[0], x[1], x[2], 0],
            [y[0], y[1], y[2], 0],
            [z[0], z[1], z[2], 0],
            [0, 0, 0, 1]

        ]

        O = [
            [1, 0, 0, -center[0]],
            [0, 1, 0, -center[1]],
            [0, 0, 1, -center[2]],
            [0, 0, 0, 1]
        ]

        self.View = self.multiplicacion(O, M)

    def lookAt(self, eye=[0, 0, 1], center=[0, 0, 0], up=[0, 1, 0]):
        z = norm(sub(eye, center))
        x = norm(cross(up, z))
        y = norm(cross(z, x))
        self.loadViewMatriz(x, y, z, center)
        self.loadProjectionMatriz(-1 / length(norm(sub(eye, center))))

    def loadModelMatriz(self, translate, scale, rotate):
        translate_matrix = [
            [1, 0, 0, translate[0]],
            [0, 1, 0, translate[1]],
            [0, 0, 1, translate[2]],
            [0, 0, 0, 1],
        ]

        scale_matrix = [
            [scale[0], 0, 0, 0],
            [0, scale[1], 0, 0],
            [0, 0, scale[2], 0],
            [0, 0, 0, 1]

        ]

        a = rotate[0]
        rotation_matrix_x = [
            [1, 0, 0, 0],
            [0, math.cos(a), -(math.sin(a)), 0],
            [0, math.sin(a), math.cos(a), 0],
            [0, 0, 0, 1]
        ]

        b = rotate[1]
        rotation_matrix_y = [
            [math.cos(b), 0, math.sin(b), 0],
            [0, 1, 0, 0],
            [-(math.sin(b)), 0, math.cos(b), 0],
            [0, 0, 0, 1]
        ]

        c = rotate[2]

        rotation_matrix_z = [
            [math.cos(c), -(math.sin(c)), 0, 0],
            [0, 1, 0, 0],
            [math.sin(c), 0, math.cos(c), 0],
            [0, 0, 0, 1]
        ]

        res1 = self.multiplicacion(rotation_matrix_z, rotation_matrix_y)
        rotation_matrix = self.multiplicacion(res1, rotation_matrix_x)
        res2 = self.multiplicacion(rotation_matrix, translate_matrix)
        self.model = self.multiplicacion(res2, scale_matrix)

    def loadViewportMatrix(self, x=0, y=0):
        self.viewPort = [[self.vpWidth / 2, 0, 0, x + self.vpWidth / 2],
                    [0, self.vpHeight / 2, 0, y + self.vpHeight / 2],
                    [0, 0, 128, 128],
                    [0, 0, 0, 1]]

    def transform_img_sr6(self, coords, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0), eye=[0, 0, 1],
                          center=[0, 0, 0],
                          up=[0, 1, 0]):
        """
        This method transform in size and in coords the original image
        :param coords: The original coords of the vertex
        :param translate: the params that translates the vertex
        :param scale: the params that make bigger or smaller the vertex
        :return: the coords transformated
        """
        x1, y1, z1, x2, y2, z2, x3, y3, z3 = coords

        aumented1 = [[x1, 0, 0, 0], [y1, 0, 0, 0], [z1, 0, 0, 0], [1, 0, 0, 0]]
        aumented2 = [[x2, 0, 0, 0], [y2, 0, 0, 0], [z2, 0, 0, 0], [1, 0, 0, 0]]
        aumented3 = [[x3, 0, 0, 0], [y3, 0, 0, 0], [z3, 0, 0, 0], [1, 0, 0, 0]]

        self.lookAt(eye, center, up)

        self.loadModelMatriz(translate, scale, rotate)
        self.loadViewportMatrix()

        prueba1 = self.multiplicacion(self.viewPort, self.projection)
        prueba2 = self.multiplicacion(prueba1, self.View)
        final = self.multiplicacion(prueba2, self.model)
        final2 = self.multiplicacion(final, aumented1)

        x1 = math.floor((final2[0][0] / final2[3][0]))
        y1 = math.floor((final2[1][0] / final2[3][0]))
        z1 = math.floor((final2[2][0] / final2[3][0]))

        prueba1 = self.multiplicacion(self.viewPort, self.projection)
        prueba2 = self.multiplicacion(prueba1, self.View)
        final = self.multiplicacion(prueba2, self.model)
        final2 = self.multiplicacion(final, aumented2)

        x2 = math.floor((final2[0][0] / final2[3][0]))
        y2 = math.floor((final2[1][0] / final2[3][0]))
        z2 = math.floor((final2[2][0] / final2[3][0]))

        prueba1 = self.multiplicacion(self.viewPort, self.projection)
        prueba2 = self.multiplicacion(prueba1, self.View)
        final = self.multiplicacion(prueba2, self.model)
        final2 = self.multiplicacion(final, aumented3)

        x3 = math.floor((final2[0][0] / final2[3][0]))
        y3 = math.floor((final2[1][0] / final2[3][0]))
        z3 = math.floor((final2[2][0] / final2[3][0]))

        return x1, y1, z1, x2, y2, z2, x3, y3, z3

    def transform_img_sr6_2(self, coords, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0), eye=[0, 0, 1],
                            center=[0, 0, 0],
                            up=[0, 1, 0]):
        """
        This method transform in size and in coords the original image
        :param coords: The original coords of the vertex
        :param translate: the params that translates the vertex
        :param scale: the params that make bigger or smaller the vertex
        :return: the coords transformated
        """
        x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = coords

        aumented1 = [[x1, 0, 0, 0], [y1, 0, 0, 0], [z1, 0, 0, 0], [1, 0, 0, 0]]
        aumented2 = [[x2, 0, 0, 0], [y2, 0, 0, 0], [z2, 0, 0, 0], [1, 0, 0, 0]]
        aumented3 = [[x3, 0, 0, 0], [y3, 0, 0, 0], [z3, 0, 0, 0], [1, 0, 0, 0]]
        aumented4 = [[x4, 0, 0, 0], [y4, 0, 0, 0], [z4, 0, 0, 0], [1, 0, 0, 0]]

        self.lookAt(eye, center, up)
        self.loadModelMatriz(translate, scale, rotate)
        self.loadViewportMatrix()

        prueba1 = self.multiplicacion(self.viewPort, self.projection)
        prueba2 = self.multiplicacion(prueba1, self.View)
        final = self.multiplicacion(prueba2, self.model)
        final2 = self.multiplicacion(final, aumented1)

        x1 = math.floor((final2[0][0] / final2[3][0]))
        y1 = math.floor((final2[1][0] / final2[3][0]))
        z1 = math.floor((final2[2][0] / final2[3][0]))

        prueba1 = self.multiplicacion(self.viewPort, self.projection)
        prueba2 = self.multiplicacion(prueba1, self.View)
        final = self.multiplicacion(prueba2, self.model)
        final2 = self.multiplicacion(final, aumented2)

        x2 = math.floor((final2[0][0] / final2[3][0]))
        y2 = math.floor((final2[1][0] / final2[3][0]))
        z2 = math.floor((final2[2][0] / final2[3][0]))

        prueba1 = self.multiplicacion(self.viewPort, self.projection)
        prueba2 = self.multiplicacion(prueba1, self.View)
        final = self.multiplicacion(prueba2, self.model)
        final2 = self.multiplicacion(final, aumented3)

        x3 = math.floor((final2[0][0] / final2[3][0]))
        y3 = math.floor((final2[1][0] / final2[3][0]))
        z3 = math.floor((final2[2][0] / final2[3][0]))

        prueba1 = self.multiplicacion(self.viewPort, self.projection)
        prueba2 = self.multiplicacion(prueba1, self.View)
        final = self.multiplicacion(prueba2, self.model)
        final2 = self.multiplicacion(final, aumented4)

        x4 = math.floor((final2[0][0] / final2[3][0]))
        y4 = math.floor((final2[1][0] / final2[3][0]))
        z4 = math.floor((final2[2][0] / final2[3][0]))

        return x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4

    def load_img_texture(self, filename, translate, scale, texture, light=[1, 0, 0]):
        model = obj_loader(filename)
        for face in model.vfaces:
            vcount = len(face)
            v = calc_v(model.vertices, face, 0, vcount)
            if vcount == 3:
                coords = tuple([(v[i][j]) for i in range(vcount) for j in range(vcount)])
                x1, y1, z1, x2, y2, z2, x3, y3, z3 = self.transform_img(coords, translate, scale)
                intensity = calc_intensity([x1, y1, z1], [x2, y2, z2], [x3, y3, z3], light)
                v2 = calc_v(model.tvertices, face, 1, vcount)
                self.triangle([x1, y1, z1], [x2, y2, z2], [x3, y3, z3], color=None, texture=texture,
                              texture_coords=v2, intensity=intensity)
            else:
                coords = tuple([(v[j][i]) for j in range(vcount) for i in range(vcount - 1)])
                x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = self.transform_img2(coords, translate, scale)
                vertices = [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3], [x4, y4, z4]]
                intensity = calc_intensity(vertices[0], vertices[1], vertices[2], light)
                a, b, c, d = vertices
                v2 = calc_v(model.tvertices, face, 1, vcount)
                self.triangle(a, b, c, color=None, texture=texture, texture_coords=[v2[0], v2[1], v2[2]],
                              intensity=intensity)
                self.triangle(a, c, d, color=None, texture=texture, texture_coords=[v2[0], v2[2], v2[3]],
                              intensity=intensity)

    def load_img_texture2(self, filename, translate, scale, rotate, texture, light=[1, 0, 0], eye=[0, 0, 1],
                          center=[0, 0, 0],
                          up=[0, 1, 0]):
        model = obj_loader(filename)
        for face in model.vfaces:
            vcount = len(face)
            v = calc_v(model.vertices, face, 0, vcount)
            if vcount == 3:
                coords = tuple([(v[i][j]) for i in range(vcount) for j in range(vcount)])
                x1, y1, z1, x2, y2, z2, x3, y3, z3 = self.transform_img_sr6(coords, translate, scale, rotate, eye,
                                                                            center, up)
                intensity = calc_intensity([x1, y1, z1], [x2, y2, z2], [x3, y3, z3], light)
                v2 = calc_v(model.tvertices, face, 1, vcount)
                self.triangle([x1, y1, z1], [x2, y2, z2], [x3, y3, z3], color=None, texture=texture,
                              texture_coords=v2, intensity=intensity)
            else:
                coords = tuple([(v[j][i]) for j in range(vcount) for i in range(vcount - 1)])
                x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = self.transform_img_sr6_2(coords, translate, scale,
                                                                                          rotate, eye, center, up)
                vertices = [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3], [x4, y4, z4]]
                intensity = calc_intensity(vertices[0], vertices[1], vertices[2], light)
                a, b, c, d = vertices
                v2 = calc_v(model.tvertices, face, 1, vcount)
                self.triangle(a, b, c, color=None, texture=texture, texture_coords=[v2[0], v2[1], v2[2]],
                              intensity=intensity)
                self.triangle(a, c, d, color=None, texture=texture, texture_coords=[v2[0], v2[2], v2[3]],
                              intensity=intensity)

    def load2(self, filename, translate, scale, rotate, light=[1, 0, 0], eye=[0, 0, 1], center=[0, 0, 0],
              up=[0, 1, 0]):
        """
        Based on example of Graphics Course
        Loads an obj file in the screen
        wireframe only
        Input:
          filename: the full path of the obj file
          translate: (translateX, translateY) how much the model will be translated during render
          scale: (scaleX, scaleY) how much the model should be scaled
        """
        light = norm(light)
        model = obj_loader(filename)
        for face in model.vfaces:
            vcount = len(face)
            v = calc_v(model.vertices, face, 0, vcount)
            if vcount == 3:
                coords = tuple([(v[i][j]) for i in range(vcount) for j in range(vcount)])
                x1, y1, z1, x2, y2, z2, x3, y3, z3 = self.transform_img_sr6(coords, translate, scale, rotate, eye,
                                                                            center, up)
                intensity = calc_intensity([x1, y1, z1], [x2, y2, z2], [x3, y3, z3], light)
                grey = round(255 * intensity)
                if grey < 0:
                    continue
                self.triangle([x1, y1, z1], [x2, y2, z2], [x3, y3, z3], None, [], color(grey, grey, grey),
                              intensity)
            elif vcount == 4:
                coords = tuple([(v[j][i]) for j in range(vcount) for i in range(vcount - 1)])
                x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = self.transform_img_sr6_2(coords, translate, scale,
                                                                                          rotate, eye, center, up)
                vertices = [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3], [x4, y4, z4]]
                intensity = calc_intensity(vertices[0], vertices[1], vertices[2], light)
                grey = round(255 * intensity)
                A, B, C, D = vertices
                if grey < 0:
                    continue
                print(grey)
                col = color(grey, grey, grey)
                self.triangle(A, B, C, None, [], col, intensity)
                self.triangle(A, C, D, None, [], col, intensity)

    def load(self, filename, translate, scale, zbuffer_flag=False, light=[1, 0, 0]):
        """
        Based on example of Graphics Course
        Loads an obj file in the screen
        wireframe only
        Input:
          filename: the full path of the obj file
          translate: (translateX, translateY) how much the model will be translated during render
          scale: (scaleX, scaleY) how much the model should be scaled
        """
        self.zbuffer_flag = zbuffer_flag
        model = obj_loader(filename)
        for face in model.vfaces:
            vcount = len(face)
            v = calc_v(model.vertices, face, 0, vcount)
            if vcount == 3:
                coords = tuple([(v[i][j]) for i in range(vcount) for j in range(vcount)])
                x1, y1, z1, x2, y2, z2, x3, y3, z3 = self.transform_img(coords, translate, scale)
                intensity = calc_intensity([x1, y1, z1], [x2, y2, z2], [x3, y3, z3], light)
                grey = round(255 * intensity)
                if grey < 0:
                    continue
                self.triangle([x1, y1, z1], [x2, y2, z2], [x3, y3, z3], None, [], color(grey, grey, grey),
                              intensity)
            elif vcount == 4:
                print(vcount)
                coords = tuple([(v[j][i]) for j in range(vcount) for i in range(vcount - 1)])
                x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = self.transform_img2(coords, translate, scale)
                vertices = [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3], [x4, y4, z4]]
                intensity = calc_intensity(vertices[0], vertices[1], vertices[2], light)
                grey = round(255 * intensity)
                A, B, C, D = vertices
                if grey < 0:
                    continue
                col = color(grey, grey, grey)
                self.triangle(A, B, C, None, [], col, intensity)
                self.triangle(A, C, D, None, [], col, intensity)

    def barycentric(self, vec1, vec2, vec3, P):
        vect1 = [vec3[0] - vec1[0], vec2[0] - vec1[0], vec1[0] - P[0]]
        vect2 = [vec3[1] - vec1[1], vec2[1] - vec1[1], vec1[1] - P[1]]
        u = cross(vect1, vect2)
        if abs(u[2]) < 1:
            return [-1, -1, -1]

        else:
            return [
                1 - (u[0] + u[1]) / u[2],
                u[1] / u[2],
                u[0] / u[2]
            ]

    def triangle(self, vec1, vec2, vec3, texture=None, texture_coords=[], color=None, intensity=0):
        bbox_min, bbox_max = self.bounding_box(vec1, vec2, vec3)
        lim_loop1 = bbox_max[0] + 1
        lim_loop2 = bbox_max[1] + 1
        for x in range(bbox_min[0], lim_loop1):
            for y in range(bbox_min[1], lim_loop2):
                w, v, u = self.barycentric(vec1, vec2, vec3, [x, y])
                if w < 0 or v < 0 or u < 0:
                    continue
                if texture:
                    tA, tB, tC = texture_coords[0], texture_coords[1], texture_coords[2]
                    tx = tA[0] * w + tB[0] * v + tC[0] * u
                    ty = tA[1] * w + tB[1] * v + tC[1] * u

                    color = texture.get_color(tx, ty, intensity)
                z = vec1[2] * w + vec2[2] * v + vec3[2] * u

                if x < 0 or y < 0:
                    continue

                if x < len(self.zbuffer) and y < len(self.zbuffer[x]) and z > self.zbuffer[x][y]:
                    self.point(x, y, color)
                    self.zbuffer[x][y] = z

    def bounding_box(self, *vertices):
        """
        This method is used to calculate a bounding box around a triangle
        """

        vec1 = [(vertex[0]) for vertex in vertices]
        vec2 = [(vertex[1]) for vertex in vertices]
        vec1.sort()
        vec2.sort()
        return [vec1[0], vec2[0]], [vec1[-1], vec2[-1]]
