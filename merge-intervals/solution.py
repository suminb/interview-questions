import pytest


def merge(interval1, interval2):
    min1, max1 = interval1
    min2, max2 = interval2

    min_ = min(min1, min2)
    max_ = max(max1, max2)

    if max_ - min_ <= (max1 - min1) + (max2 - min2):
        return [(min_, max_)]
    else:
        return [interval1, interval2]


def merge_all(*intervals):
    raise NotImplemented


@pytest.mark.parametrize('interval1, interval2, expected', [
    ((1, 3), (2, 5), [(1, 5)]),
    ((3, 8), (2, 5), [(2, 8)]),
    ((1, 2), (5, 7), [(1, 2), (5, 7)]),
    ((5, 6), (1, 2), [(5, 6), (1, 2)]),
])
def test_merge(interval1, interval2, expected):
    assert merge(interval1, interval2) == expected


@pytest.mark.skip
def test_merge_all():
    intervals = [(1, 4), (2, 5), (3, 4), (7, 8), (8, 9)]
    expected = [(1, 5), (7, 9)]
    assert merge_all(*intervals) == expected
