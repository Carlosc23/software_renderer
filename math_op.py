def length(v0):
    """
      Input: 1 size 3 vector
      Output: Scalar with the length of the vector
    """
    return sum([(v0[i] ** 2) for i in range(3)]) ** 0.5


def norm(V):
    vl = length(V)

    if not vl:
        return [0, 0, 0]
    return [(V[i] / vl) for i in range(3)]


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
