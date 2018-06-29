stack1, stack2 = [], []


def enqueue(x):
    stack1.append(x)


def dequeue():
    if stack2:
        return stack2.pop()

    while stack1:
        stack2.append(stack1.pop())

    return stack2.pop()


def test_1():
    enqueue(1)
    enqueue(2)
    enqueue(3)

    assert dequeue() == 1
    assert dequeue() == 2
    assert dequeue() == 3


def test_2():
    enqueue(1)
    assert dequeue() == 1

    enqueue(2)
    enqueue(3)
    assert dequeue() == 2

    enqueue(4)
    assert dequeue() == 3
    assert dequeue() == 4
