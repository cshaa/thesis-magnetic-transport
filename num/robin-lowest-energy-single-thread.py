import sys
from decimal import Decimal
exec(open("./robin-lowest-energy.py").read())

min_a = Decimal(sys.argv[1]) if len(sys.argv) == 3 else -2
max_a = Decimal(sys.argv[2]) if len(sys.argv) == 3 else 2

# print header
print_estimates([])

e = 1.
for a in float_range(min_a, max_a, 0.1):
    e = find_minimum_energy(a, e, 0.0001, 0.001)
    print(
        "{0:.1f}, \t {1:.3f}".format(a, e),
        flush=True
    )
