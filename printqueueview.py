"""
Module name: printqueueview.py
Purpose: View for print queue prioritized list
Authors: Team1 (Samantha Gephart)
Date: Nov 28, 2024
"""

from model import PrintModel, PrintJob

class PrintQueueView(object):
    """the view class for the prioritized print queue application"""

    def __init__(self, model):
        self.model = model

    def run(self):
        """Menu-driven command loop for the app.
        Main Menu
        1 Send file to print queue
        2 Print next file
        3 Print all files
        4 Exit the program
        """
        #TODO: Error handling, if 3 or 4 selected and there are no files to print,
        # tell user there are no files to print prompt them to try again
        pass

    def printNext(self):
        """
        Prints next file (if there is one)
        Raises exception if there are no files in PrintModel
        """
        #TODO: raise exception if there are no files in the PrintModel (Priority Queue)
        #TODO: print the highest priority printJob with getMin method (from PrintModel)
        # (getMin removes the highest priority, restructures queue accordingly, and
        # returns printJob removed)

        pass

    def printNow(self, printJob):
        """
        Prints given filename immediately
        """
        #TODO print "'filename' printed immediately"
        #TODO print "filename" of file printed
        # this one is your choice if you want to keep it as a separate method
        # or handle it in the schedulePrint method below
        pass


    def printAll(self):
        """
        Prints remaining files (print jobs)
        Raises exception if there are no files in PrintModel
        """
        #TODO: raise exception if there are no files in the PrintModel (Priority Queue)
        #TODO: print: "Files printed:" followed by a list of all the print jobs in the priority queue
        #TODO: clear priority queue (clear method)
        pass

    def schedulePrint(self):
        """
            Obtains print job information and places it in queue based on priority
            Raises/excepts error if file name with incorrect extension is added
        """
        #TODO: Prompt user to enter file name ending in '.pdf', '.doc' or '.txt'
        #TODO: Error handling (raise error if filename already is in print queue, wrong extension, invalid char (e.g. ' ')
        #TODO: get the Priority (If 0 (print immediately) do not construct or schedule)
        #TODO: Construct and add printJob to PrintModel
        pass

    def getPriority(self):
        """Obtains priority info

            Send to queue
            0  Print immediately
            1  Add to next up
            2  Add to queue
            ------------
            page count
            3  1-10 pages 
            4  11-50 pages
            5  50+ pages   
        """
        # TODO: Ask user if file should be added to queue, if it's higher priority, or printed immediately
        # TODO: Prompt user to enter page count of a given file from selection
        pass

    def getCommand(self, high, menu):
        """
        Obtains and returns a command number
        Raises error if out of bounds for each selection
        """
        # TODO: Provide prompt to enter a number
        # TODO: prompt user to try again if number is out of bounds
        #  NOTE: 0 in bounds only if high == 2
        # TODO: return prompt
        pass

#Main function to start application
def main():
    model = PrintModel()
    view = PrintQueueView(model)
    view.run()

if __name__ == "__main__":
    main()