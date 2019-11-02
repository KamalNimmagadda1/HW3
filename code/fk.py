import numpy as np

def matricize(t,r):
    c = np.cos(t)
    s = np.sin(t)
    T = np.array([[c, -s, 0, (r*c)], [s, c, 0, (r*s)], [0, 0, 1, 0], [0, 0, 0, 1]])
    return T

def fk(angles, link_lengths):
    """
    Computes the forward kinematics of a planar, n-joint robot arm.

    Given below is an illustrative example. Note the end effector frame is at
    the tip of the last link.

        q[0]   l[0]   q[1]   l[1]   end_eff
          O-------------O--------------C

    you would call:
        fk(q, l)

    :param angles: list of angle values for each joint, in radians.
    :param link_lengths: list of lengths for each link in the robot arm.
    :returns: The end effector position (not pose!) with respect to the base
        frame (the frame at the first joint) as a numpy array with dtype
        np.float64
    """
    # FILL in your code here
    P = np.eye(4)
    angle = 0
    for i in range(len(link_lengths)):
	T = matricize(angles[i], link_lengths[i])
	P = np.dot(P,T)
    pos = np.array([P[0][3],P[1][3],P[2][3]])
    return pos

if __name__ == '__main__':
    np.set_printoptions(suppress=True)

    print("A:")
    print(fk([0.0, 0.0, 0.0], [1.0, 1.0, 1.0]))
    print("B:")
    print(fk([0.3, 0.4, 0.8], [0.8, 0.5, 1.0]))
    print("C:")
    print(fk([1.0, 0.0, 0.0], [3.0, 1.0, 1.0]))
