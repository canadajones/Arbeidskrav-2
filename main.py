#!/bin/python

import math as maths
import matplotlib.pyplot as plot

import euler
import regulation
import interactive

params = interactive.run_intro()


# Constants
F_motor_max = params["F_motor_max"]
F_misc = params["F_misc"]

m_car = params["m_car"] # kg
m_load = params["m_load"] # kg
m = m_car + m_load # kg

rho = params["rho"] # kg/m³
A = params["A"] #m²
C_d = params["C_d"] 
C_r = params["C_r"]

slope = params["slope_degrees"] / 180 * maths.pi
g = params["g"] # m/s²

# Time parameters
T = params["T"] #s
dt = params["Ts"] #s
N = maths.ceil(T / dt) # ticks

# Regulation parameters
v_target_kmh = params["v_target_kmh"] # km/h
v_target = v_target_kmh / 3.6

Kc = params["Kc"]
Ti = params["Ti"]
Td = params["Td"]

Kp = Kc # proportional coefficient
Ki = Kc/Ti # integral coefficient
Kd = Kc*Td # derivative coefficient


# Initial values
v_0 = params["v_initial_kmh"] / 3.6 # m/s
u_0 = 0 # N



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
	e = [0]*3
	if (len(vs) < 3):
		e[-1] = v_target - vs[-1]
		e[-2] = v_target - vs[-1]
		e[-3] = v_target - vs[-1]
	else:
		e[-1] = v_target - vs[-1]
		e[-2] = v_target - vs[-2]
		e[-3] = v_target - vs[-3]
	return e

# Derivative functions

def t_deriv(t, v, u, **arrs):
	return 1

def v_deriv(t, v, u, **arrs):
	return (motor(v, u) - drag(v) - roll(v) - gravity() - misc(v))/m

def u_deriv(t, v, u, **arrs):
	return clamp(-F_motor_max, F_motor_max, regulation.pid(make_error(arrs["_v"]), dt, Kp, Ki, Kd))


t = [0]
v = [v_0]
u = [u_0]



fs = [t, v, u]
fds = [t_deriv, v_deriv, u_deriv]
names = ["_t", "_v", "_u"]

euler.run_sim(fs, fds, names, dt, N)

t = fs.pop(0)
names.pop(0)

# post-scaling
v = [ e*3.6 for e in fs[0]]
v_target_line = [v_target_kmh] * N


plot.plot(t, v)
plot.plot(t, v_target_line)

plot.title("Velocity of car")
plot.xlabel("t / s")
plot.ylabel("v / km/t")

plot.grid()
plot.legend(["v", "v_target"])
plot.show()