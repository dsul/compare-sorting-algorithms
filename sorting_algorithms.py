from typing import List


def top_down_mergesort(arr: List[float]) -> List[float]:
    # Cutoff chosen based on execution time improvement consistency
    # after various tests.
    insertion_sort_cutoff = 15

    def sort(lo: int, hi: int):
        if lo >= hi:
            return

        # Optimize by running an insertion sort on small arrays.
        if ((hi - lo) + 1) <= insertion_sort_cutoff:
            return _subsequence_insertion_sort(arr, lo, hi)

        # Sort the left half and the right half of the array.
        mid = lo + (hi - lo) // 2
        sort(lo, mid)
        sort(mid + 1, hi)

        # The array is already sorted.
        if arr[mid] <= arr[mid + 1]:
            return

        _merge(arr, lo, mid, hi)

    sort(0, len(arr) - 1)
    return arr


def bottom_up_mergesort(arr: List[float]) -> List[float]:
    arr_length = len(arr)
    curr_subarray_length = 1

    # Continue until a merge encompasses the entire array.
    while curr_subarray_length < arr_length:

        # Complete passes of {curr_subarray_len}-by-{curr_subarray_len} merges.
        for i in range(0, arr_length - curr_subarray_length, curr_subarray_length * 2):
            mid = (i + curr_subarray_length) - 1
            hi = min(mid + curr_subarray_length, arr_length - 1)
            _merge(arr, i, mid, hi)

        # Double the size of the subarrays being merged after
        # each iteration through the array.
        curr_subarray_length *= 2

    return arr


def insertion_sort(arr: List[float]) -> List[float]:
    for i, curr_num in enumerate(arr):
        prev_elements_ptr = i - 1

        # Compare the current element with all previously considered elements,
        # moving the considered element to the right if the current is smaller.
        while prev_elements_ptr >= 0 and curr_num < arr[prev_elements_ptr]:
            arr[prev_elements_ptr + 1] = arr[prev_elements_ptr]
            prev_elements_ptr -= 1

        # Now set the current element to its sorted location.
        arr[prev_elements_ptr + 1] = curr_num

    return arr


def shellsort(arr: List[float]) -> List[float]:
    gap_size = 1

    # Using Knuth's increment sequence due to ease of generation.
    # https://oeis.org/A003462
    while gap_size < len(arr) // 3:
        gap_size = 3 * gap_size + 1

    # The final gap size of 1 will perform an insertion sort and guarantee
    # that the array is sorted.
    while gap_size >= 1:

        # h-sort the array by the gap size.
        for i, curr_num in enumerate(arr):
            prev_elements_ptr = i - gap_size

            # Compare the current element with all previously considered
            # elements in the current gap sequence, moving the considered
            # element to the right by the gap size if the current is smaller.
            while prev_elements_ptr >= 0 and curr_num < arr[prev_elements_ptr]:
                arr[prev_elements_ptr + gap_size] = arr[prev_elements_ptr]
                prev_elements_ptr -= gap_size

            # Now set the current element to its h-sorted location.
            arr[prev_elements_ptr + gap_size] = curr_num

        gap_size //= 3

    return arr


def quicksort(arr: List[float]) -> List[float]:
    def sort(lo: int, hi: int):
        # Instead of recursing to this base case, you can also opt for
        # an insertion sort at some cutoff point. I omitted that
        # potential optimization as I was seeing negligible speed
        # gains at < 10,000 elements and minor speed losses > 10,000 elements.
        if lo >= hi:
            return

        j = _partition(arr, lo, hi)
        sort(lo, j - 1)
        sort(j + 1, hi)

    sort(0, len(arr) - 1)
    return arr


def _partition(arr: List[float], lo: int, hi: int) -> int:
    # One of the most important aspects of quicksort - selecting the pivot.
    # I am current selecting the first element as the pivot since I am
    # guaranteeing that the input is randomized and likely void of duplicates.
    pivot = arr[lo]
    forward_ptr = lo + 1
    reverse_ptr = hi

    while True:
        # Find an element larger than the pivot moving left => right.
        while arr[forward_ptr] < pivot and forward_ptr < hi:
            forward_ptr += 1

        # Find an element smaller than the pivot moving right => left.
        while arr[reverse_ptr] > pivot and reverse_ptr > lo:
            reverse_ptr -= 1

        # Do not swap the elements when the pointers have crossed.
        # This means the sorted location for the pivot has been found.
        if forward_ptr >= reverse_ptr:
            break

        # Swap the larger elements on the left with the smaller elements
        # on the right.
        arr[forward_ptr], arr[reverse_ptr] = arr[reverse_ptr], arr[forward_ptr]

    # Place the pivot located at arr[lo] into its sorted position.
    arr[lo], arr[reverse_ptr] = arr[reverse_ptr], arr[lo]

    # Return the location of the pivot's final destination as it
    # acts as the anchor for subsequent partitions.
    return reverse_ptr


# Insertion sort for any subsequence. Helper for other
# sorting algorithms like mergesort and quicksort.
def _subsequence_insertion_sort(arr: List[float], lo: int, hi: int) -> None:
    for i in range((hi - lo) + 1):
        normalized_index = i + lo
        current_num = arr[normalized_index]
        prev_elements_ptr = normalized_index - 1

        while prev_elements_ptr >= lo and current_num < arr[prev_elements_ptr]:
            arr[prev_elements_ptr + 1] = arr[prev_elements_ptr]
            prev_elements_ptr -= 1

        arr[prev_elements_ptr + 1] = current_num


def _merge(arr: List[float], lo: int, mid: int, hi: int):
    # Copy the values to be merged in a temp array. Alternatively,
    # iterate over the original array and populate the temp array
    # with the sorted values, and copy the temp array back in sequence.
    temp_arr = arr[lo:hi + 1]

    # Initialize the pointers needed to modify the original array.
    left_half_ptr = lo
    right_half_ptr = mid + 1
    original_arr_index = lo

    # If both halves of the array have values left, compare their values
    # and merge back into the correct place in the original array.
    while left_half_ptr <= mid and right_half_ptr <= hi:
        if temp_arr[left_half_ptr - lo] <= temp_arr[right_half_ptr - lo]:
            arr[original_arr_index] = temp_arr[left_half_ptr - lo]
            left_half_ptr += 1
        else:
            arr[original_arr_index] = temp_arr[right_half_ptr - lo]
            right_half_ptr += 1

        original_arr_index += 1

    # One half of the array has run out of values, so just merge the
    # remaining values from the left or right half.
    while right_half_ptr <= hi:
        arr[original_arr_index] = temp_arr[right_half_ptr - lo]
        right_half_ptr += 1
        original_arr_index += 1

    while left_half_ptr <= mid:
        arr[original_arr_index] = temp_arr[left_half_ptr - lo]
        left_half_ptr += 1
        original_arr_index += 1
