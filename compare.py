#!/usr/bin/env python3

import random
import sorting_algorithms
import sys
import timeit

from typing import Tuple

algorithm1 = getattr(sorting_algorithms, sys.argv[1])
algorithm2 = getattr(sorting_algorithms, sys.argv[2])
trials: int = int(sys.argv[3])
array_len: int = int(sys.argv[4])


def run_trials() -> Tuple[float, float]:
    algorithm1_time_total = 0.0
    algorithm2_time_total = 0.0

    for _ in range(trials):
        random_array = [random.random() for _ in range(array_len + 1)]
        random_array_copy = random_array[:]
        algorithm1_time_total += timeit.timeit(
            lambda: algorithm1(random_array), number=1)
        algorithm2_time_total += timeit.timeit(
            lambda: algorithm2(random_array_copy), number=1)

    return (algorithm1_time_total, algorithm2_time_total)


def main():
    algorithm1_time_total, algorithm2_time_total = run_trials()

    print(f"Trials: {trials}")
    print(f"Input Length: {array_len}")
    print("\nAverage Time:")
    print(f"{algorithm1.__name__}: {algorithm1_time_total/trials:.6f}")
    print(f"{algorithm2.__name__}: {algorithm2_time_total/trials:.6f}")

    if algorithm1_time_total > algorithm2_time_total:
        ratio = algorithm1_time_total / algorithm2_time_total
        print(
            f"\n{algorithm2.__name__} ran {ratio:.1f} times faster than {algorithm1.__name__}.")
    else:
        ratio = algorithm2_time_total / algorithm1_time_total
        print(
            f"\n{algorithm1.__name__} ran {ratio:.1f} times faster than {algorithm2.__name__}.")


main()
