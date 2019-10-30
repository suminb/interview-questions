"""A solution using Set. Time Complexity is O(N)."""
from typing import List, Set


def is_possible(nums: List[int], k: int):
    nums_set: Set[int] = set(nums)  # It takes O(n).
    for num in nums:  # It takes O(n) as well.
        remain = k - num
        if remain in nums_set:  # It takes O(1).
            return True
    return False


def test_1():
    nums = [-5, 0, 2, 3, 7, 8]
    k = 9
    assert is_possible(nums, k) is True


def test_2():
    nums = [-5, 0, 2, 3, 7, 8]
    k = 1
    assert is_possible(nums, k) is False
