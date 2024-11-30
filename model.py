"""
Module name: printqueueview.py
Purpose: Contains PrintModel, Priority, and PrintJob classes
Authors: Team1 (Samantha Gephart)
Date: Nov 28, 2024
"""

from listqueue import ListQueue

"""Maintains a priority queue of print jobs"""
class ListPriorityQueue(ListQueue):
    """A list-based priority queue implementation (inherits from
    ListQueue.py)"""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        ListQueue.__init__(self, sourceCollection)

    def add(self, newJob):
        """Inserts newJob after items of greater or equal
        priority or ahead of items of lesser priority.
        A has greater priority than B if A < B."""
        pass

"""Represents 3 possible print job priority levels
   ('low', 'high', 'immediate')"""
class Priority(object):
    """ Represents the print jobs priority"""

    def __init__(self, rank):
        self.rank = rank

    def __ge__(self, other):
        """Used for comparison (>=)"""
        pass

    def __lt__(self, other):
        """Returns True if self's priority < other's priority,
        or False otherwise."""
        pass

    def __str__(self):
        """returns string representation of the priority"""
        pass



"""Represents and maintains print job priority level"""
class PrintJob(object):
    """ Represents the print jobs priority"""

    def __init__(self, filename, priority='low', pages='1'):
        self.filename = filename
        self.priority = priority
        self.pages = pages

    def __ge__(self, other):
        """Used for comparison (>=)"""
        pass

    def __lt__(self, other):
        """Returns True if self's priority < other's priority,
        or False otherwise."""
        pass

    def __str__(self):
        """returns string representation of the rank (Priority)"""
        pass

    def getName(self):
        """returns file name"""
        pass

    def getPriority(self):
        """returns the priority level"""
        pass

    def getPages(self):
        "returns number of pages"
        pass
