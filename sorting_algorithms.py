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
