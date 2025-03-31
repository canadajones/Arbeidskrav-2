#! /bin/python


def euler(f, f_deriv, dt):
    return f + f_deriv*dt;


def unstack(l):
    ret = [None]*len(l)
    for i in range(len(l)):
        a = l[i][-1]
        if (a < 0) :
            a = 0
        ret[i] = a
    return ret


def run_sim(fs, fds, names, dt, N):
    assert len(fs) == len(fds)
    
    for i in range(N-1):
        fdv = [None] * len(fds)
        for i in range(len(fds)):
            fdv[i] = fds[i](*unstack(fs), **dict(zip(names, fs)))

        for i in range(len(fs)):
            fs[i].append(euler(fs[i][-1], fdv[i], dt))

