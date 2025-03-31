

def dpid(e, dt, kp, ki, kd):

	e_vals = [0]*3
	if (len(e) < 3):
		e_vals[-1] = e[-1]
		e_vals[-2] = e[-1]
		e_vals[-3] = e[-1]
	else:
		e_vals[-1] = e[-1]
		e_vals[-2] = e[-2]
		e_vals[-3] = e[-3]

	return (kp + ki*dt + kd/dt)*e_vals[-1] + (-kp - 2*kd/dt)*e_vals[-2] + (kd/dt)*e_vals[-3] 

def pid(u, e, dt, kp, ki, kd):
	return u + dpid(e, dt, kp, ki, kd)




def onoff(e):
	if (e > 3):
		return 1
	else:
		return 0