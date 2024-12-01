"""
Module name: printqueueview.py
Purpose: Contains PrintModel, Priority, and PrintJob classes
Authors: Team1 (Samantha Gephart)
Date: Nov 28, 2024
"""
#TODO switch to array implementation
from listqueue import ListQueue

"""Maintains a priority queue of print jobs"""
class PrintModel(ListQueue):
    """A list-based priority queue implementation (inherits from
    ListQueue.py)"""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        ListQueue.__init__(self, sourceCollection)

    def add(self, printJob):
        """Inserts newJob after items of greater or equal
        priority or ahead of items of lesser priority
        A has greater priority than B if A < B."""
        # TODO first item appended to list
        # TODO compare new element w/ parent, swap if rank/priority # < than parents
        # TODO
        pass

    def parent(self, printItem):
        pass

    def leftChild(self, printItem):
        pass

    def rightChild(self, printItem):
        pass

    def getMin(self):
        pass

    def moveDown(self, printItem):
        pass

    def moveUp(self, printItem):
        pass

    def updatePriority(self, printItem, newPriority):
        pass

    def insert(self, printJob):
        pass

    def remove(self, printItem):
        pass
    def swap(self, itemI, itemJ):
        pass


"""Represents and maintains print job priority level"""
class PrintJob(object):
    """ Represents the print jobs priority"""

    def __init__(self, filename, rank, pages):

        #Check filename is valid
        file = filename.split(".",2)
        name = file[0]
        extension = file[1]

        invalid = r'[<>:/."\|?*]'
        if any(char in name for char in invalid):
            raise Exception("File name contains invalid character")
        elif (extension != "pdf") and (extension != "doc") and (extension != "txt"):
            raise Exception("Incorrect file extension")
        else:
            self.filename = name + '.' + extension
        self.rank = rank
        self.pages = pages
        self.priority = rank * pages


    def __ge__(self, other):
        """Used for comparison (>=)"""
        return self.priority >= other.priority


    def __lt__(self, other):
        """Returns True if self's priority < other's priority,
        or False otherwise."""
        return self.priority < other.priority





