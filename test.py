#!/usr/bin/env python3

import random
import sorting_algorithms
import sys

from typing import Callable, List

GREEN = '\033[32m'
RED = '\033[31m'
ENDC = '\033[m'


def _print_test_run_output(name: str, is_sorted: bool, result: List[float]) -> None:
    if is_sorted:
        print(f"{name}{GREEN} PASS {ENDC}")
    else:
        print(f"{name}{RED} FAIL {ENDC}")
        print(f"The array was not sorted:\n{result}\n")


def _print_test_exception_output(name: str, error_message: str) -> None:
    print(f"{name}{RED} FAIL {ENDC}")
    print(f"{error_message}\n")


def _is_algorithm(key: str, value: str) -> bool:
    # Ignore imported typings and helper functions.
    return not value.startswith("typing") and not key.startswith("_")


def _generate_test_input() -> List[float]:
    return [random.random() for _ in range(10)]


def _is_sorted(arr: List[float]) -> bool:
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def _execute_test(algorithm: Callable[[List[float]], List[float]], algorithm_name: str) -> None:
    try:
        result = algorithm(_generate_test_input())
        _print_test_run_output(algorithm_name, _is_sorted(result), result)

    except:
        _print_test_exception_output(algorithm_name, str(sys.exc_info()[1]))


def test_one() -> None:
    algorithm = getattr(sorting_algorithms, sys.argv[1])
    _execute_test(algorithm, algorithm.__name__)


def test_all() -> None:
    for key, value in sorting_algorithms.__dict__.items():
        if callable(value) and _is_algorithm(str(key), str(value)):
            _execute_test(value, key)


if len(sys.argv) == 1:
    test_all()
else:
    test_one()
