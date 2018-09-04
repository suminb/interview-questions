def is_monotonic(xs):
    delta = [x - y for x, y in zip(xs[1:], xs[:-1])]
    return all([d >= 0 for d in delta]) or all([d <= 0 for d in delta])


def test_is_monotonic():
    assert is_monotonic([1, 2, 3, 4])
    assert is_monotonic([4, 3, 2, 1])
    assert is_monotonic([0, 0, 0, 0])
    assert not is_monotonic([1, 2, 1, 2])
