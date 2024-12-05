"""
Module name: printqueueview.py
Purpose: View for print queue prioritized list
Authors: Team1 Samantha Gephart, Claudia Dorin, Ethan Bevier, Rachel Mizer
Date: Nov 28, 2024
"""
import sys

from model import PrintModel, PrintJob

class PrintQueueView(object):
    """The view class for the prioritized print queue application.
    Manages priority queue given user commands."""

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
            try:
                print("Main Menu")
                print("1 Send file to print queue\n2 Print next file\n3 Print all files\n4 Exit the program")
                action = int(input("Key number to make a selection [1-4]: "))
                if action == 1:
                    self.schedulePrint()
                elif action == 2:
                    self.printNext()
                elif action == 3:
                    self.printAll()
                elif action == 4:
                    print("Printer Queue program closed")
                    sys.exit(0)
                else:
                    print("Invalid selection number")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def printNext(self):
        """Prints next file (if there is one)"""
        try:
            if self.model.isEmpty():
                print("No files are in the queue to print")
            else:
                print("Printing next file... ")
                printed = self.model.pop()
                print("File printed: ", printed)
                self.getQueue()
        except Exception as e:
            print(f"An error occurred while printing the next file: {e}")

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
        """Obtains print job information and places it in the queue based on priority"""
        valid = False
        while not valid:
            try:
                filename = input("Enter the file to print with a valid format (.pdf, .doc, .txt):")
                file = filename.split(".", 1)
                if len(file) != 2:
                    print("Invalid file format. Please provide a file with an extension (e.g., file.txt).")
                    continue

                name, extension = file
                invalid = r'[ <>:/."\|?*]'
                if any(char in name for char in invalid):
                    print("File name contains invalid character")
                    continue
                elif extension not in ["pdf", "doc", "txt"]:
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
            except Exception as e:
                print(f"An error occurred while scheduling the print job: {e}")

    @staticmethod
    def getPriority():
        """Obtains priority info"""
        try:
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
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the options.")
            return PrintQueueView.getPriority()

    def getQueue(self):
        """Prints the print jobs in the queue"""
        try:
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
        except Exception as e:
            print(f"An error occurred while getting the print queue: {e}")

# Main function to start application
def main():
    try:
        model = PrintModel()
        view = PrintQueueView(model)
        view.run()
    except Exception as e:
        print(f"An error occurred while running the application: {e}")

if __name__ == "__main__":
    main()


