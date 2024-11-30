"""
Module name: listqueue.py
Purpose: List based priority queue
Authors: Team1 (Samantha Gephart)
Date: Nov 28, 2024
"""

class ListQueue(object):

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = []
        if sourceCollection:
            for item in sourceCollection: #appends each item to self
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the queue is empty, or False otherwise."""
        if not self.items:
            return True
        else:
            return False

    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the queue."""
        return "{" + ", ".join(map(str,self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        cursor = 0
        while cursor < len(self.items):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        added_list = ListQueue(self.items)
        for item in other:
            added_list.add(item)
        return added_list

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self.items == other:
            return True
        else:
            return False

    def peek(self):
        """Returns the item at the front of the queue.
        Raises IndexError if queue is not empty."""
        return self.items[0]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = []

    def add(self, item):
        """Inserts item at the rear of the queue."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at the front of the
        queue. Raises IndexError if queue is empty."""
        if not self.items:
            raise IndexError("Queue is empty")
        popped = self.items[0]
        self.items = self.items[1:]
        return popped