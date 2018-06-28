def count_islands(world, x, y):
    h = len(world)
    w = len(world[0])

    count = 0
    for j in range(0, h):
        for i in range(0, w):
            if world[j][i] != 0:
                count += 1
            mark_world(world, i, j)

    return count


def mark_world(world, x, y):
    queue = []
    queue.append((x, y))
    while queue:
        i, j = queue.pop(0)
        if in_boundary(world, i, j):
            if world[j][i] != 0:
                world[j][i] = 0
                queue.append((i - 1, j))
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))


def in_boundary(world, x, y):
    h = len(world)
    w = len(world[0])

    return (0 <= x < w) and (0 <= y < h)


def test():
    world = [
        [1, 1, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 0],
    ]

    assert count_islands(world, 0, 0) == 5
