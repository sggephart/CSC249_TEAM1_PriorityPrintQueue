"""
Module name: model.py
Purpose: Contains PrintModel and PrintJob classes
Authors: Team1 (Samantha Gephart)
Date: Nov 28, 2024
"""
from minheap import MinHeap

"""Maintains a priority queue of print jobs"""
class PrintModel(MinHeap):
    """A list-based priority queue implementation (inherits from
    MinHeap.py)"""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        MinHeap.__init__(self, sourceCollection)
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __str__(self):
        copyQueue = PrintModel()
        printQueue = ""
        for item in self:
            copyQueue.add(item)
        while not copyQueue.isEmpty():
            copyPop = copyQueue.pop()
            printQueue += str(copyPop) + "\n"
        return printQueue


def main():
    h1 = MinHeap()
    h1.add(3)
    h1.add(8)
    h1.add(6)
    h1.add(4)
    h1.add(3)
    print(h1)
    p1 = PrintModel()
    p1.add(3)
    p1.add(8)
    p1.add(6)
    p1.add(4)
    p1.add(3)
    print(p1)



if __name__ == "__main__":
    main()

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





