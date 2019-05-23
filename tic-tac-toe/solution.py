import pytest


def judge(board) -> bool:
    """Make a judgement whether there is a winner.

    :param board: N-by-N array
    """
    if not board:
        return False

    n = len(board)
    # Check for horizontal lines
    if any([judge_line([board[i][j] for j in range(n)]) for i in range(n)]):
        return True
    # Check for vertical lines
    if any([judge_line([board[i][j] for i in range(n)]) for j in range(n)]):
        return True
    # Check for diagonal lines
    if judge_line([board[i][i] for i in range(n)]):
        return True
    if judge_line([board[i][n - i - 1] for i in range(n)]):
        return True

    return False


def judge_line(line) -> bool:
    return all([x == y for x, y in zip(line[:-1], line[1:])])


@pytest.mark.parametrize('board, expected', [
    ([], False),
    ([
        ['O'],
    ], True),
    ([
        ['O', 'X'],
        ['X', 'O'],
    ], True),
    ([
        ['O', 'X', 'O'],
        ['O', 'X', 'X'],
        ['X', 'X', 'O'],
    ], True),
    ([
        ['O', 'X', 'O', 'X'],
        ['O', 'X', 'X', 'O'],
        ['X', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'X'],
    ], False),
])
def test_judge(board, expected):
    actual = judge(board)
    assert expected == actual