from mpmath import mp
import numpy as np

sqrt2 = mp.sqrt(2)

def D(ν, w):
    return mp.pcfd(ν, w)

def F_delta(α, p, ε):
    # α√b, p/√b, ε/b
    a = α * sqrt2
    w = p * sqrt2
    ν = (ε+1)/2

    # see eq. 3.12
    return \
        D(ν, w) * D(ν+1, -w) + \
        D(ν, -w) * D(ν+1, w) + \
        a * D(ν, w) * D(ν, -w)

def F_robin(α, p, ε):
    # α/√b, p/√b, ε/b
    ν = (ε+1)/2

    # see eq. 4.4
    return (α+p) * D(ν, p*sqrt2) - sqrt2 * D(ν+1, p*sqrt2)

def F_dirichlet(p, ε):
    # p/√b, ε/b
    ν = (ε+1)/2

    # see discussion under eq. 4.3
    return D(ν, p*sqrt2)


