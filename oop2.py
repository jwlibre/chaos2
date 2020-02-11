import math
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pdb

class Particle():

    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def perform_iteration(self, it):
        self.x = self.x + (it.f[0][0] + 2 * it.f[0][1] + 2 * it.f[0][2] + it.f[0][3]) * it.dt/6.0
        self.y = self.y + (it.f[1][0] + 2 * it.f[1][1] + 2 * it.f[1][2] + it.f[1][3]) * it.dt/6.0
        self.z = self.z + (it.f[2][0] + 2 * it.f[2][1] + 2 * it.f[2][2] + it.f[2][3]) * it.dt/6.0
        self.t = self.t + it.dt
        return self

    def print_attributes(self):
        print("x: {}".format(self.x))
        print("y: {}".format(self.y))
        print("z: {}".format(self.z))
        print("t: {}".format(self.t))

class Iteration():

    def __init__(self, a, b, r, dt):
        self.f = np.empty([3,4])
        self.a = a
        self.b = b
        self.r = r
        self.dt = dt

    def iterate(self, p):
        self.f[0][0] = self.a * (p.y - p.x)
        self.f[1][0] = self.r * p.x - p.y - (p.x * p.z)
        self.f[2][0] = (p.x * p.y) - (self.b * p.z)

        self.f[0][1] = self.a * (p.y + self.f[1][0] * 0.5 * self.dt) - self.a * (p.x + self.f[0][0] * 0.5*(self.dt))
        self.f[1][1] = self.r * (p.x + (self.f[0][0]) * (0.5 * self.dt)) - (p.y + (self.f[1][0]) * (0.5 * self.dt)) - (p.x + (self.f[0][0]) * (0.5 * self.dt)) * (p.z + (self.f[2][0]) * (0.5 * self.dt))
        self.f[2][1] = (p.x + (self.f[0][0]) * (0.5 * self.dt)) * (p.y + (self.f[1][0]) * (0.5 * self.dt)) - self.b * (p.z + (self.f[2][0]) * (0.5 * self.dt))

        self.f[0][2] = self.a * (p.y + self.f[1][1] * 0.5 * self.dt) - self.a * (p.x + self.f[0][1] * 0.5*(self.dt))
        self.f[1][2] = self.r * (p.x + (self.f[0][1]) * (0.5 * self.dt)) - (p.y + (self.f[1][1]) * (0.5 * self.dt)) - (p.x + (self.f[0][1]) * (0.5 * self.dt)) * (p.z + (self.f[2][1]) * (0.5 * self.dt))
        self.f[2][2] = (p.x + (self.f[0][1]) * (0.5 * self.dt)) * (p.y + (self.f[1][1]) * (0.5 * self.dt)) - self.b * (p.z + (self.f[2][1]) * (0.5 * self.dt))

        self.f[0][3] = self.a * (p.y + (self.f[1][2]) * (self.dt)) - self.a * (p.x + (self.f[0][2]) * (self.dt))
        self.f[1][3] = self.r * (p.x + (self.f[0][2]) * (self.dt)) - (p.y + (self.f[1][2]) * (self.dt)) - (p.x + (self.f[0][2]) * (self.dt)) * (p.z + (self.f[2][2]) * (self.dt))
        self.f[2][3] = (p.x + (self.f[0][2]) * (self.dt)) * (p.y + (self.f[1][2]) * (self.dt)) - self.b * (p.z + (self.f[2][2]) * (self.dt))
        return self

    def print_attributes(self):
        print("f: {}".format(self.f))
        print("a: {}".format(self.a))
        print("b: {}".format(self.b))
        print("r: {}".format(self.r))


if __name__ == '__main__':
    x_list = []
    y_list = []
    z_list = []

    max_iterations = 1000000
    t = 0
    x = 0.8
    y = 0.3
    z = 0.4

    p = Particle(x, y, z, t)

    a = 10
    b = 8/3
    r = 14
    dt = 0.05

    it = Iteration(a, b, r, dt)

    for k in range(max_iterations):
        it = it.iterate(p)
        p = p.perform_iteration(it)
        x_list.append(p.x)
        y_list.append(p.y)
        z_list.append(p.z)

    fig, ax = plt.subplots()
    ax.plot(x_list, z_list)
    plt.show()
