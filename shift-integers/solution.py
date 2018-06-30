def shift(ls):
    i = c = 0
    n = len(ls)

    while i < n:
        m = ls[i]
        if c > 0:
            ls[i - c] = ls[i]
        if m == 0:
            c += 1
        i += 1

    for i in range(n - c, n):
        ls[i] = 0

    return ls


def test():
    data = [1, 3, -4, 0, 9, 2, 0, 5]
    expected = [1, 3, -4, 9, 2, 5, 0, 0]
    assert shift(data) == expected
