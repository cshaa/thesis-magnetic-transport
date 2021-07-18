import decimal
from mpmath import mp
from itertools import chain

def float_range(start, stop, step):
  while start <= stop:
    yield float(start)
    start += decimal.Decimal(step)


# start searching in the most likely place
# then continue outward
def range_p(step_p: float):
    return chain(
        float_range(-1,  1, step_p),
        float_range( 1,  2, step_p),
        float_range(-2, -1, step_p),
    )


# after reaching this energy, abort
min_e = -5

# F(...) = 0 if e is an eigenvalue
def F(a, p, e) -> float:
    return (
        (a + p)
        * mp.pcfd((e-1)/2, p * mp.sqrt(2))
        -
        mp.sqrt(2)
        * mp.pcfd((e+1)/2, p * mp.sqrt(2))
    )

# checks whether e is is an eigenvalue for any p
def is_allowed_energy(a, e, step_p) -> float:
    for p in range_p(step_p):
        if F(a, p, e) >= 0:
            return True
    return False

# finds the lowest allowed e
def find_minimum_energy(
    a: float, start_e: float,
    step_p: float, step_e: float
) -> float:
    e = start_e
    while is_allowed_energy(a, e, step_p):
        e -= step_e
        if e < min_e:
            return float("nan")

    return e

# returns a tuple (a, e)
def boundary_minimum_energy_tuple(
    a: float, start_e: float,
    step_p: float, step_e: float
) -> tuple[float, float]:
    return (
        a,
        find_minimum_energy(a, start_e, step_p, step_e)
    )

# prints an array of estimates as CSV
def print_estimates(
    estimates: list[tuple[float, float]],
    prec: int = 1
):
    print('boundary, \t energy', flush=True)
    for (a, e) in estimates:
        print(
            "{0:.1f}, \t {1:.{p}f}".format(a, e, p=prec),
            flush=True
        )
