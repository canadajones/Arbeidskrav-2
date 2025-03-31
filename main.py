#!/bin/python

import math as maths
import matplotlib.pyplot as plot

import euler
import regulation

# Constants
F_motor_max = 10779
F_misc = 80 # N

m_car = 1979 # kg
m_load = 150 # kg
m = m_car + m_load # kg

rho = 1.29 # kg/m³
A = 2.5 #m²
C_d = 0.24 
C_r = 0.01

slope = 0 # degrees
g = 9.81 # m/s²

# Parameters
T = 60 #s
dt = 0.01 #s
N = maths.ceil(T / dt) # ticks


v_target_kmh = 70 # km/h
v_target = v_target_kmh / 3.6

v_0 = 50 # m/s
u_0 = 0 # N

Kc = 2129 
Ti = 2.0 # s

Kp = 0.6 # proportional coefficient
Ki = 0.1 # integral coefficient


def signum(a):
    return 1 if a > 0 else -1

def clamp(a, b, v):
    if (v < a):
        return a
    if (v > b):
        return b
    else:
        return v


# Physical system structure
def motor(v, u):
    return clamp(-F_motor_max, F_motor_max, u)

def drag(v):
    return signum(v) * 0.5 * rho * C_d * A * v**2

def roll(v):
    return signum(v) * C_r * m * g * maths.cos(slope)

def gravity():
    return m * g * maths.sin(slope)

def misc(v):
    return signum(v) * F_misc

def make_error(vs):
    e = []
    for v in vs:
        e.append(v_target - v)
    return e

# Derivative functions

def t_deriv(t, v, u, **arrs):
    return 1

def v_deriv(t, v, u, **arrs):
    return (motor(v, u) - drag(v) - roll(v) - gravity() - misc(v))/m

def u_deriv(t, v, u, **arrs):
    return 0


t = [0]
v = [v_0]
u = [u_0]



fs = [t, v, u]
fds = [t_deriv, v_deriv, u_deriv]
names = ["_t", "_v", "_u"]

euler.run_sim(fs, fds, names, dt, N)
print(u)

t = fs.pop(0)
names.pop(0)
for f in fs:
    plot.plot(t, f)

plot.grid()
plot.legend(["v", "u"])
plot.show()