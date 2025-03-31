

def p(e, dt):
	return (e[-2] - e[-3])/dt

def i(e, dt):
	return e[-1]

def d(e, dt):
	return (e[-3] + e[-1] - 2*e[-2])/(dt**2)


def pid(e, dt, kp, ki, kd):
	e_vals = [0]*3
	if (len(e) < 3):
		e_vals[-1] = e[-1]
		e_vals[-2] = e[-1]
		e_vals[-3] = e[-1]
	else:
		e_vals[-1] = e[-1]
		e_vals[-2] = e[-2]
		e_vals[-3] = e[-3]


	return kp*p(e_vals, dt) + ki*i(e_vals, dt) + kd*d(e_vals, dt)


def onoff(e):
	if (e > 3):
		return 1
	else:
		return 0