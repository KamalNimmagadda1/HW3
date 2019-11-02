import numpy as np


def line_sphere_intersection(p1, p2, c, r):
    """
    Implements the line-sphere intersection algorithm.
    https://en.wikipedia.org/wiki/Line-sphere_intersection

    :param p1: start of line segment
    :param p2: end of line segment
    :param c: sphere center
    :param r: sphere radius
    :returns: discriminant (value under the square root) of the line-sphere
        intersection formula, as a np.float64 scalar
    """
    # FILL in your code here
    
    l = p1 - p2
    s = 0
    for i in range(len(l)):
	s += np.power(l[i], 2)
    mag = np.power(s, 0.5)
    for i in range(len(l)):
	l[i]= (l[i]/mag)
    a1 = c - p1
    a = np.dot(l, a1)
    b1 = np.dot(a1, a1)
    b = b1 - np.power(r, 2)
    d = np.power(a, 2) - b
    return -d

p1 = np.array([0.0, 0.0, 0.0])
p2 = np.array([0.7, 0.0, 0.0])
c = np.array([1.0,0.3,0.0])
r = 0.2
d = line_sphere_intersection(p1, p2, c, r)
print(d)
