"""
Module name: model.py
Purpose: Contains PrintModel and PrintJob classes
Authors: Team1 Samantha Gephart, Claudia Dorin, Ethan Bevier, Rachel Mizer
Date: Nov 28, 2024
"""

"""
Class: PrintJob
Author: Samantha Gephart

"""
class PrintJob(object):
    """ Represents the print jobs and their respective priorities"""

    def __init__(self, filename, priority):
        #Check filename is valid
        file = filename.split(".",2)
        name = file[0]
        extension = file[1]

        invalid = r'[<>:/ ."\|?*]'
        if any(char in name for char in invalid):
            raise Exception("File name contains invalid character")
        elif (extension != "pdf") and (extension != "doc") and (extension != "txt"):
            raise Exception("Incorrect file extension")
        else:
            self.filename = name + '.' + extension
        self.priority = priority


    def __repr__(self):
        """Returns a string representation of the file (the file name)"""
        return self.filename

    def __ge__(self, other):
        """Used for comparison (>=)"""
        return self.priority >= other.priority

    def __lt__(self, other):
        """Returns True if self's priority < other's priority,
        or False otherwise."""
        return self.priority < other.priority


"""
class: PrintModel
Author: Samantha Gephart
Date: 12/1/2024
Purpose: Maintains a priority queue of files to be printed
"""
class PrintModel(object):
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        self.heap = []
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        """Returns true if heap is empty and false otherwise"""
        if not self.heap:
            return True
        else:
            return False

    def __iter__(self):
        """visits the items from least to greatest"""
        return iter(self.heap)

    def __len__(self):
        """Returns number of items in heap (same as len(heap))"""
        return len(self.heap)

    def __str__(self):
        """Returns a string showing shape of the heap when printed !"""
        def recurse(index, level):
            parent = index
            rightChild = 2 * index + 2
            leftChild = 2 * index + 1
            lastIndex = len(self.heap) - 1
            s =""
            if index <= lastIndex:
                s += recurse(rightChild, level +1)
                s += "| " * level
                s += str(self.heap[parent]) + "\n"
                s += recurse(leftChild, level +1)
            return s
        return recurse(0,0)

    def __contains__(self, item):
        """Returns a True if item in heap, false otherwise"""
        if item in self.heap:
            return True
        else:
            return False

    def __add__(self, other):
        """Returns new tree containing items in previous heap and the new item """
        added_heap = PrintModel(self.heap)
        for item in other:
            added_heap.add(item)
        return added_heap

    def __eq__(self, other):
        """Returns true if heap equals other or false otherwise.
        Equivalent to heap == object, equal if contain the same items"""
        if self.heap == other:
            return True
        else:
            return False

    def peak(self):
        """Returns the topmost item in heap"""
        return self.heap[0]

    def add(self, item):
        """Inserts item into proper place in heap"""
        self.heap.append(item) #inserts item at the bottom of the heap
        curPos = len(self.heap) - 1
        while curPos > 0:
            parent = (curPos - 1) // 2
            parentItem = self.heap[parent]
            if parentItem <= item: #correct spot for item
                break
            else:                   #continue traversing
                self.heap[curPos] = self.heap[parent] #swap element with parent
                self.heap[parent] = item
                curPos = parent

    def pop(self):
        """Removes and returns the topmost item in the heap.
        Raises exception if heap is empty"""
        if self.isEmpty():
            raise AttributeError("Heap is empty")
        topItem = self.heap[0]                          #pointer to top element
        bottomItem = self.heap.pop(len(self.heap) - 1)  #pointer to bottom element
        if self.isEmpty():                              #returns the item if only 1 in heap
            return bottomItem
        self.heap[0] = bottomItem           #bottom moved to top
        lastIndex = len(self.heap) - 1      #index updated
        curPos = 0
        while True:
            # curses through heap from top to bottom, moving smallest
            # child up one level at each step until getting to bottom
            leftChild = 2 * curPos + 1      #index of left child
            rightChild = 2 * curPos + 2     #index of right child
            if leftChild > lastIndex:       #bottom has been reached
                break
            if rightChild > lastIndex:      # If there is no child at the right child index
                maxChild = leftChild        # maxChild is the left child
                maxItem = self.heap[maxChild]
                break
            else:
                leftItem = self.heap[leftChild]     #Item set to object at the leftChild index of heap
                rightItem = self.heap[rightChild]   #Item set to object at the rightChild index of heap
                #shfit right
            if leftItem < rightItem:
                maxChild = leftChild           #index of smaller child saved
                maxItem = self.heap[maxChild]
            else:
                maxChild = rightChild
                maxItem = self.heap[maxChild]
            if bottomItem <= maxItem:           #bottom reached
                break
            else:
                # smaller child moved up a level
                self.heap[curPos] = self.heap[maxChild]     #the lesser child moved to current position
                self.heap[maxChild] = bottomItem            #previous location of moved child replaced with bottomItem
                curPos = maxChild                           # current position is index of previous index of shifted child
        return topItem

