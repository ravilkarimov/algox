def is_palindrome_slow(s: str, left: int, right: int) -> bool:
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


cases = [
    ["", True],
    ["a", True],
    ["ab", False],
    ["aba", True],
    ["ababa", True],
    ["aaaa", True],
    ["aaccaa", True],
    ["aacdaa", False],
]

for inp, ans in cases:
    res = is_palindrome_slow(inp, 0, len(inp) - 1)
    assert res == ans, (inp, ans, res)


def odd_count(s: str) -> int:
    num_palinromes = 0
    for i in range(len(s)):
        left, right = i - 1, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            num_palinromes += 1
    return num_palinromes


def even_count(s: str) -> int:
    num_palinromes = 0
    for i in range(len(s)):
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            num_palinromes += 1
    return num_palinromes


def count_palindromes_slow(s: str):
    return odd_count(s) + even_count(s) + len(s)
