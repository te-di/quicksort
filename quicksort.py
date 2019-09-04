# A recursive function that sorts a list using quicksort

from random import randint

def quick(l):
'''Takes a list as an argument, uses quicksort algorithm to sort it.'''
    # Base case:
    if len(l) == 0:
        return l
    elif len(l) == 1:
        return l
    elif len(l) == 2:
        if l[0] > l[1]:
            l[0], l[1] = l[1], l[0]
        return l
    else:
        # Removing the pivot (random number from the list, splits it in
        # half) from the list:
        pivot = l.pop(randint(0, len(l) - 1))
        # Creating a list of numbers less or equal to the pivot:
        less_eq = [i for i in l if i <= pivot]
        # Creating a list of numbers greater than the pivot:
        greater = [i for i in l if i > pivot]
        # Everything less or equal than the pivot is now on its left.
        # Everything greater is on its right.
        # Concatenating in one list again:
        l = quick(less_eq) + [pivot] + quick(greater)
        return l
