import pytest


# TODO: Deal with negative integers
def find(seq, target):
    n = len(seq)
    s = 0
    i = j = 0

    while True:
        if s == target:
            break
        elif s < target and j < n:
            s += seq[j]
            j += 1
        elif s > target and i < n:
            s -= seq[i]
            i += 1

    return seq[i:j]


@pytest.mark.parametrize('seq, target, expected', [
    ([1, 2, 3, 4], -1, []),
    ([1, 2, 3, 4], 1, [1]),
    ([1, 2, 3, 4], 7, [3, 4]),
])
def test_find(seq, target, expected):
    assert find(seq, target) == expected
