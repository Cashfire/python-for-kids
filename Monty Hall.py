"""
Monty Hall problem
- Numpy tips: Use `numpy.where()` or `nonzero()` to indexing an array.
- Get familiar with where and for loop.
[The Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) is quite count-intuitive and it is hard to understand for kids. So we just do simulation here and let kids realize that problem and leave the question mark in their heart to be explored latter.
>Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
```
numpy.where(condition, [x,y])
Condition is boolean array.
If condition is ture, yield x, otherwise y.
Return indexing array.
If only condition is given, return tuple of condition.nonzero()
Let's start with the use of nonzero(), which is to find the indices of an array, where a condition is True.
```
"""

import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a > 3
```
Out[5]:
array([[False, False, False],
       [ True,  True,  True],
       [ True,  True,  True]], dtype=bool)
Given an array a, the condition a > 3 is a boolean array and since False is interpreted as 0, np.nonzero(a>3) yields the indices of the a where the condition is true.
```
np.nonzero(a>3)
Out[6]:
(array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))
The nonzero method of the boolean array can also be called.
In [8]:

(a>3).nonzero()
Out[8]:
(array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))


