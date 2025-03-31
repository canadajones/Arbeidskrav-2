

def p(e, dt):
	return (e[-2] - e[-3])/dt

def i(e, dt):
	return e[-1]

def d(e, dt):
	return (e[-3] + e[-1] - 2*e[-2])/(dt**2)


def pid(e, dt, kp, ki, kd):
	return kp*p(e, dt) + ki*i(e, dt) + kd*d(e, dt)


def onoff(e):
	if (e > 3):
		return 1
	else:
		return 0