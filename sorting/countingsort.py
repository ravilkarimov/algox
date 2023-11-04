def counting_sort(nums: list[int]) -> list[int]:
    if not nums:
        return []
    n, min_val, max_val = len(nums), abs(min(nums)), max(nums)
    counter = [0] * (min_val + max_val + 1)
    for i in range(n):
        counter[nums[i] + min_val] += 1
    for i in range(1, len(counter)):
        counter[i] = counter[i] + counter[i - 1]
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        ans[counter[nums[i] + min_val] - 1] = nums[i]
        counter[nums[i] + min_val] -= 1
    return ans
