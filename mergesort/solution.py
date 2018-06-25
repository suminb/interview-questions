import pytest


def merge(l1, l2):
    i = j = 0
    n, m = len(l1), len(l2)

    merged = []
    while i < n and j < m:
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    return merged + l1[i:] + l2[j:]


def sort(ls):
    n = len(ls)
    if n > 1:
        mid = n // 2  # integer division
        return merge(sort(ls[:mid]), sort(ls[mid:]))
    else:
        return ls


@pytest.mark.parametrize('l1, l2, expected', [
    ([], [], []),
    ([], [1, 2, 3], [1, 2, 3]),
    ([0, 1, 2], [], [0, 1, 2]),
    ([1, 3, 5, 7], [2, 4, 6], [1, 2, 3, 4, 5, 6, 7]),
])
def test_merge(l1, l2, expected):
    assert merge(l1, l2) == expected


@pytest.mark.parametrize('ls, expected', [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([3, 0, 4, -5, 2, 7, 8], [-5, 0, 2, 3, 4, 7, 8]),
])
def test_sort(ls, expected):
    assert sort(ls) == expected
