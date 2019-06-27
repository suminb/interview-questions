Consecutive Subsequence
=======================

Problem: Given a list of integers and a target number, which is an integer,
determine whether there exists a consecutive subsequence that adds up to the
target number. You may assume all integers in the list are non-negative for
now.

For example,

    list = [1, 4, 5, 3, 2], target = 8

then your function returns `true`. If there is no such subsequence that adds
up to `target` then it returns `false`.

Time limit: 15 min

Variation 1
-----------
Find the subsequence. For example,

    list = [1, 4, 5, 3, 2], target = 8

then your function returns `[5, 3]`. If there are multiple subsequences
satisfying the constraint, you may return one of the valid solutions.

Variation 2
-----------

The list may contain negative numbers. Hint: there is a solution that runs in linear time.
