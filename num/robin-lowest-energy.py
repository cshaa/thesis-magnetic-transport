import decimal
from mpmath import mp
from itertools import chain

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)



step_p = 0.001
step_e = 0.01
step_a = 0.1

# start searching in the most likely place
# then continue outward
def range_p():
    return chain(
        float_range(-1,  1, step_p),
        float_range( 1,  2, step_p),
        float_range(-2, -1, step_p),
    )


# after reaching this energy, abort
min_e = -5

def F(a, p, e):
    return (
        (a + p)
        * mp.pcfd((e-1)/2, p * mp.sqrt(2))
        -
        mp.sqrt(2)
        * mp.pcfd((e+1)/2, p * mp.sqrt(2))
    )

def is_allowed_energy(a, e):
    for p in range_p():
        if F(a, p, e) >= 0:
            return True
    return False

def find_minimum_energy(a, start_e):
    e = start_e
    while is_allowed_energy(a, e):
        e -= step_e
        if e < min_e:
            return float("nan")

    return e

def print_minimum_energies(min_a, max_a):
    e = 1
    for a in float_range(min_a, max_a, step_a):
        e = find_minimum_energy(a, e)
        print(
            "{0:.1f}, \t {1:.2f}".format(a, e),
            flush=True
        )


print('boundary, \t energy', flush=True)
print_minimum_energies(-2, 2)
