import random
from sorting.partition import partition


def quicksort(arr: list[int], left: int, right: int) -> list[int]:
    if left < right:
        pivot_index = random.randint(left, right)
        mid_1, mid_2 = partition(arr, left, right, pivot_index)
        if -1 in (mid_1, mid_2):
            return arr
        quicksort(arr, left, mid_1 - 1)
        quicksort(arr, mid_2 + 1, right)
    return arr
