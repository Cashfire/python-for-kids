"""
Monty Hall problem
- Numpy tips: Use `numpy.where()` or `nonzero()` to indexing an array.
- Get familiar with where and for loop.
[The Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) is quite count-intuitive and it is hard to understand for kids. So we just do simulation here and let kids realize that problem and leave the question mark in their heart to be explored latter.
>Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
numpy.where(condition, [x,y]) # detailed explanation: http://pda.readthedocs.io/en/latest/chp4.html
Condition is boolean array.
If condition is ture, yield x, otherwise y.
Return indexing array.
If only condition is given, return tuple of condition.nonzero()
Let's start with the use of nonzero(), which is to find the indices of an array, where a condition is True.
"""
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a > 3
"""
array([[False, False, False],
       [ True,  True,  True],
       [ True,  True,  True]], dtype=bool)
Given an array a, the condition a > 3 is a boolean array and since False is interpreted as 0, np.nonzero(a>3) yields the indices of the a where the condition is true.
"""
np.nonzero(a>3)
"""
(array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))
The nonzero method of the boolean array can also be called.
"""
(a>3).nonzero()  # (array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))

"""
First, write a function called prize_doors. 
This function will simulate the location of the prize in many games.
--------------------
Function: prize_doors
Generate a random array of 0s, 1s, and 2s, representing hiding a prize between door 0, door 1, and door 2
--------------------
Parameters: nsim (int)
The number of simulations to run
--------------------
Returns: prizedoors (array)
Random array of 0s, 1s, and 2s
--------------------
Example
>>> print prize_doors(3)
array([0, 0, 2])
"""

def prize_doors(nsim):
       return np.random.randint(0, 3, (nsim))

"""
Next, write a function that simulates the contestant's guesses for nsim simulations. 
Call this function origin_guess.
----------------------
Function: origin_guesses
Return any strategy for guessing which door a prize is behind. 
This could be a random strategy, one that always guesses 2, whatever.
----------------------
Parameters: nsim (int)
The number of simulations to generate guesses for
-----------------------
Returns: originalguesses (array)
An array of guesses. Each guess is a 0, 1, or 2
-----------------------
Example
>>> print origin_guesses(5)
array([0, 0, 0, 0, 0])
"""

def origin_guesses(nsim):
       return np.zeros(nsim, dtype=np.int)

"""
Next, write a function, open_goats, to simulate randomly revealing one of the goat doors that a contestant didn't pick.
-----------------------
Function: open_goats
Simulate the opening of a goat door that doesn't contain the prize,
and is different from the contestants guess
-----------------------
Parameters: prizedoors (array). The door that the prize is behind in each simulation
            originalguesses (array). The door that the contestant guessed in each simulation
------------------------
Returns: openedgoats (array)
The goat door that is opened for each simulation. Each item is 0, 1, or 2, 
and is different from both prizedoors and guesses
------------------------
Examples
>>> print open_goats(np.array([0, 1, 2]), np.array([1, 1, 1]))
>>> array([2, 2, 0])
"""

def open_goats(prizedoors, originalguesses):
       result = np.random.randint(0, 3, prizedoors.size)
       while True:
              bad = (result == prizedoors) | (result == originalguesses)
              if not bad.any():
                     return result
              result[bad] = np.random.randint(0, 3, bad.sum())
       
"""
Write a function, switch_guess, that represents the strategy of always switching a guess after the goat door is opened.
-----------------------
switch_guess
-----------------------
Parameters: originalguesses (array): Array of original guesses, for each simulation
            openedgoats (array): Array of revealed goat doors for each simulation
-----------------------
Returns: The new door after switching. Should be different from both guesses and goatdoors

Examples
--------
>>> print switch_guess(np.array([0, 1, 2]), np.array([1, 2, 1]))
>>> array([2, 0, 0])
"""
def switch_guess(originalguesses, openedgoats):
       result = np.zeros(originalguesses.size)
       switch = {(0, 1): 2, (0, 2): 1, (1, 0): 2, (1, 2): 0, (2, 0): 1, (2, 1): 0}
       for i in [0,1,1]:
              for j in [0,1,2]:
                     mask = (originalguesses == i) & (openedgoats ==j)
                     if not mask.any():
                            continue
                     result = np.where(mask, np.ones_like(result) * switch[(i,j)], result)
       return result

"""
Last function: write a win_percentage function Calculate how much percent of times is correct, 
and returns the percent of correct guesses.
------------------
win_percentage
------------------
Parameters: guesses (array). Guesses for each simulation
            prizedoors (array). Location of prize for each simulation
-------------------
Returns: percentage (number between 0 and 100). The win percentage
-------------------
Examples
>>> print win_percentage(np.array([0, 1, 2]), np.array([0, 0, 0]))
33.333
"""

def win_percentage(guesses, prizedoors):
       return 100 * (guesses == prizedoors).mean()
"""
Now, put it together. Simulate 10000 games where contestant keeps his original guess, 
and 10000 games where the contestant switches his door after a goat door is revealed. 
Compute the percentage of time the contestant wins under either strategy. 
Is one strategy better than the other?
"""

nsim = 10000
### keep guesses
print "Win percentage when keeping original door"
print win_percentage(prize_doors(nsim), origin_guesses(nsim))
### switch
pd = prize_doors(nsim)
guess = origin_guesses(nsim)
goat = open_goats(pd, guess)
newguess = switch_guess(guess, goat)
print "Win percentage when switching doors"
print win_percentage(pd, newguess).mean()
"""
Win percentage when keeping original door
33.21
Win percentage when switching doors
66.61
"""
       

