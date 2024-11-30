"""
Module name: listqueue.py
Purpose: List based priority queue
Authors: Team1 (Samantha Gephart)
Date: Nov 28, 2024
"""

class ListQueue(object):

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        pass

    def isEmpty(self):
        """Returns True if the queue is empty, or False otherwise."""
        pass

    def __len__(self):
        """Returns the number of items in the queue."""
        pass

    def __str__(self):
        """Returns the string representation of the queue."""
        pass

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        pass

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        pass

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        pass

    def peek(self):
        """Returns the item at the front of the queue.
        Raises IndexError if queue is not empty."""
        pass

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def add(self, item):
        """Inserts item at the rear of the queue."""
        pass

    def pop(self):
        """Removes and returns the item at the front of the
        queue. Raises IndexError if queue is empty."""
        pass