"""
Module name: printqueueview.py
Purpose: View for print queue prioritized list
Authors: Team1 - Samantha Gephart
Date: Nov 28, 2024
"""
import sys

from model import PrintModel, PrintJob

class PrintQueueView(object):
    """the view class for the prioritized print queue application.
    Manages priority queue given user commands. """

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
        while True:
            print("Main Menu")
            print("1 Send file to print queue\n2 Print next file\n3 Print all files\n4 Exit the program")
            action = int(input("Key number to make a selection [1-4]: "))
            if action == 1:
                self.schedulePrint()
            elif action == 2:
                if self.model.isEmpty():
                    print("The printer queue is empty")
                    break
                else:
                    self.printNext()
            elif action == 3:
                if self.model.isEmpty():
                    print("The printer queue is empty")
                    break
                else:
                    self.printAll()
            elif action == 4:
                print("Printer Queue program closed")
                sys.exit(0)
            else:
                print("Invalid selection number")
                continue


    def printNext(self):
        """
        Prints next file (if there is one)
        Raises exception if there are no files in PrintModel
        """
        if self.model.isEmpty():
            raise Exception("No files are in queue to print")
        else:
            print("Printing next file... ")
            printed = self.model.pop()
            print("File printed: ", printed)
            self.getQueue()



    def printAll(self):
        """
        Prints remaining files (print jobs)
        Raises exception if there are no files in PrintModel
        """
        if self.model.isEmpty():
            raise Exception("No files are in queue to print")
        else:
            print("Printing all files...")
            print("Files printed")
            while not self.model.isEmpty():
                for item in self.model:
                    printed = self.model.pop()
                    print(printed)
            self.getQueue()

    def schedulePrint(self):
        """
            Obtains print job information and places it in queue based on priority
            Raises/excepts error if file name with incorrect extension is added
        """
        valid = False
        while not valid:
            filename = input("Enter the file to print with a valid format (.pdf, .doc, .txt):")
            file = filename.split(".", 2)
            name = file[0]
            extension = file[1]
            invalid = r'[ <>:/."\|?*]'
            if any(char in name for char in invalid):
                print("File name contains invalid character")
                continue
            elif (extension != "pdf") and (extension != "doc") and (extension != "txt"):
                print("Incorrect file extension")
            else:
                filename = name + '.' + extension
                valid = True
                priority = self.getPriority()
                if priority == 0:
                    print(filename, " printed")
                    self.getQueue()
                else:
                    job = PrintJob(filename, priority)
                    self.model.add(job)
                    self.getQueue()


    @staticmethod
    def getPriority():
        """Obtains priority info

            Send to queue
            0  Print immediately
            1  Add to next up
            2  Add to queue
            ----------------------
            page count
            3  1-10 pages 
            4  11-50 pages
            5  50+ pages   
        """
        print("Print job priority")
        print("--------------------")
        print("0  Print immediately\n1  Add to next up\n2  Add to queue")

        urgency = int(input("Key number to make a selection [0-2]: "))
        while urgency < 0 or urgency > 2:
            print("Invalid selection")
            urgency = int(input("Key number to make a selection [0-2]: "))
        print("File page count")
        print("--------------------")
        print("3  1-10 pages\n4  11-50 pages\n5  50+ pages  ")
        pages = int(input("Key number to make a selection [3-5]: "))
        while pages < 3 or pages > 5:
            print("Invalid selection")
            pages = int(input("Key number to make a selection [3-5]: "))
        priority = urgency * pages
        return priority

    def getQueue(self):
        """Prints the print jobs in the queue"""
        print("--------------------")
        print("Jobs in Print Queue: ")
        copyQueue = PrintModel()
        printQueue = ""
        for item in self.model:
            copyQueue.add(item)
        while not copyQueue.isEmpty():
            copyPop = copyQueue.pop()
            printQueue += str(copyPop) + "\n"
        print(printQueue)
        print("--------------------")


#Main function to start application
def main():
    model = PrintModel()
    view = PrintQueueView(model)
    view.run()

if __name__ == "__main__":
    main()