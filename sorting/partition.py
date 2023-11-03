def partition(nums: list[int], left: int, right: int, pivot_index: int) -> tuple[int, int]:
    """
    Accepts: list of integers and predicate
    Mutates: list of integers such like:
            [a_i, ..., a_k, ..., a_j, ...], where
            - a in [i, k)  <  nums[pivot_index]
            - a in [k, j)  == nums[pivot_index]
            - a in [j, ..] >  nums[pivot_index]
    Returns: two indexes k, z where
            - all elems before k are less than pivot
            - all elems after z are bigger than pivot
    """
    if not nums or left > right or pivot_index < left or pivot_index > right:
        return -1, -1
    # place (swap) pivot elem at the end of arr
    pivot = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    less_index = left
    # form left part of arr where each elem less than pivot
    for i in range(left, right):
        if nums[i] < pivot:
            nums[less_index], nums[i] = nums[i], nums[less_index]
            less_index += 1
    dubl_index = less_index
    # form middle part of arr where each elem equal than pivot
    for i in range(less_index, right):
        if nums[i] == pivot:
            nums[dubl_index], nums[i] = nums[i], nums[dubl_index]
            dubl_index += 1
    # return pivot to correct position
    nums[right], nums[dubl_index] = nums[dubl_index], nums[right]
    return less_index, dubl_index
