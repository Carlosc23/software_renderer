# Carlos Calderon,15219
# Module with functions with matrix operations or linear algebra equations utils for render an obj


def length(v0):
    """
      Input: 1 size 3 vector
      Output: Scalar with the length of the vector
    """
    return sum([(v0[i] ** 2) for i in range(3)]) ** 0.5


def norm(v):
    vl = length(v)

    if not vl:
        return [0, 0, 0]
    return [(v[i] / vl) for i in range(3)]


def cross(vec1, vec2):
    """
    Simple function that is a vectorial product of 2 vectors
    :param vec1:
    :param vec2:
    :return:
    """
    x = vec1[1] * vec2[2] - vec1[2] * vec2[1]
    y = vec1[2] * vec2[0] - vec1[0] * vec2[2]
    z = vec1[0] * vec2[1] - vec1[1] * vec2[0]

    return [x, y, z]


def sub(vec1, vec2):
    return [(vec1[i] - vec2[i]) for i in range(3)]


def dot(v1, v2):
    return sum([(v1[i] * v2[i]) for i in range(3)])


def mult(matrix1, matrix2):
    matrix_r = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(0, 4):
        for y in range(0, 4):
            for z in range(0, 4):
                matrix_r[x][y] += matrix1[x][z] * matrix2[z][y]
    return matrix_r


def calc_intensity(coord_1, coord_2, coord_3, light):
    vp = cross(sub(coord_2, coord_1), sub(coord_3, coord_1))
    normal = norm(vp)
    intensity = dot(normal, light)
    return intensity


def calc_v(vertices, face, pos, vcount):
    faces = [(face[i][pos] - 1) for i in range(vcount)]
    return [(vertices[faces[i]]) for i in range(vcount)]
