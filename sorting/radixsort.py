def counting_sort(nums: list[str], d: int) -> list[str]:
    n = len(nums)
    counter = [0] * 10
    for num in nums:
        counter[int(num[d])] += 1
    for i in range(1, 10):
        counter[i] += counter[i - 1]
    ans = [''] * n
    for num in reversed(nums):
        pos = int(num[d])
        ans[counter[pos] - 1] = num
        counter[pos] -= 1
    return ans


def radix_sort(nums: list[int]) -> list[int]:
    if len(nums) == 0:
        return nums

    negatives = [-num for num in nums if num < 0]
    non_negatives = [num for num in nums if num >= 0]

    max_length = max(len(str(x)) for x in nums)

    arr_negatives = [str(num).zfill(max_length) for num in negatives]
    arr_non_negatives = [str(num).zfill(max_length) for num in non_negatives]

    for i in range(max_length - 1, -1, -1):
        arr_non_negatives = counting_sort(arr_non_negatives, i)
        arr_negatives = counting_sort(arr_negatives, i)

    sorted_negatives = [-int(num) for num in reversed(arr_negatives)]
    sorted_non_negatives = [int(num) for num in arr_non_negatives]

    return sorted_negatives + sorted_non_negatives


radix_sort([-1, -101, 23, 23, 11, 2, 324, -231, 432, 123])
