**This is my playground to experiment with and analyze the performance (currently just the execution times) of various sorting algorithm implementations I have written in Python.**

Uses the [timeit](https://docs.python.org/3/library/timeit.html) library for measuring the execution time.

## sorting_algorithms
This module contains all of the sorting algorithms used for comparisons. Each algorithm takes a single list of floats as the input so that the `compare` script can depend on that signature and treat them the same. Each implementation is simple to change to be mutating or non-mutating depending on your preference. That trade-off is not relevant to the testing I am doing, so most of them opt to mutate. Functions that begin with an underscore are helper functions and are ignored by the `test` script because of that naming convention. 

The sorting algorithms currently implemented are:
- Top-down mergesort with insertion sort optimization
- Bottom-up mergesort
- Insertion sort
- Shellsort with Knuth's increment sequence (https://oeis.org/A003462)
- Quicksort (two-way partition with simple pivot selection)

## compare
This script uses the `timeit` library to compare the execution times of two sorting algorithms. It makes the assumption that the algorithms are contained in a `sorting_algorithms` module.

The call signature of the script is as follows:

<pre>
./compare.py &lt;<i>sorting_function_name</i>&gt; &lt;<i>sorting_function_name</i>&gt; &lt;<i>number_of_trials</i>&gt; &lt;<i>list_length</i>&gt;
</pre>


For example, executing `./compare.py top_down_mergesort insertion_sort 3 10000` produces the output:

```
Trials: 3
Input Length: 10000

Average Time:
top_down_mergesort: 0.016301
insertion_sort: 2.191806

top_down_mergesort ran 134.5 times faster than insertion_sort.
```

## test
This script runs a simple test suite to ensure the algorithms are correctly sorting (only tests on a single, randomized data input for now). The script finds all callable, non-helper functions from the `sorting_algorithms` module and runs each one against the randomly generated array, or if provided a function name from `sorting_modules`, tests just that algorithm. This script was added to alleviate the drudgery of manually testing each algorithm in the python shell whenever I wanted or needed to make changes.

The call signature of the script is as follows:
```
./test.py [ sorting_function_name ]
```
For example, executing `./test.py` with no argument produces the output:

![image](https://user-images.githubusercontent.com/16121610/129670103-69c76483-0f78-44e3-930b-10aee8393adb.png)

## Locally

To experiment locally, remember to give execute permissions to `test.py` and `compare.py`.

```
chmod +x ./test.py ./compare.py
```
