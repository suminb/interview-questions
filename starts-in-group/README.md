Stars In Group
==============

Problem: There is an N by N grid and a set of letters in the grid. The value of
`N` ranges from `MIN_INT` to `MAX_INT`, so in a 64-bit architecture the grid
would represent a quite large space and the letters are sparsely located. A
group is defined as adjacent letters in the grid, except that diagonally
neighboring letters are not considered belonging to the same group. Given a
coordinate `(x, y)`, write a function to return a list of all letters in the
group to which the letter is belonging.

For example, let's suppose the letters are located as follows:

    (-1, 0): A
    (0, 0): B
    (0, 1): C
    (2, 0): X
    (3, 1): Y

Visually speaking, letters are located as:

      C     Y
    A B   X

Given a coordinate `(0, 0)`, all letters belonging in that particular group are
A, B, and C and thus the function shall return `[A, B, C]`. If the coordinate
is given as `(2, 0)` then the function should return `[X]` as `Y` is diagonally
adjacent to `X` and hence belonging to a different group. If a coordinate of an
empty space, say `(1, 1)`, if given then the function should return an empty
list.

Time limit: 20 min