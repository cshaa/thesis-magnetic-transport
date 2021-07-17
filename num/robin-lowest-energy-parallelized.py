from multiprocessing import cpu_count, Pool, set_start_method
exec(open("./robin-lowest-energy.py").read())

num_threads = 8

if __name__ == '__main__':
    set_start_method("spawn")

    e = 1.
    rough_estimates = [
        (a, e := find_minimum_energy(a, e, 0.01, 0.1))
        for a in float_range(-2, 2, 0.1)
    ]

    print_estimates(rough_estimates)

    with Pool(num_threads) as pool:
        good_estimates = pool.starmap(
            boundary_minimum_energy_tuple,
            [(a, e + 0.1, 0.00001, 0.001) for (a, e) in rough_estimates]
        )

        pool.close()
        pool.join()

        print_estimates(good_estimates, 4)
