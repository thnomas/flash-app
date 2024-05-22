import sys
import csv

red_color = "\033[91m"
bold_text = "\033[1m"
reset_text = "\033[0m"

class FileOperations:
    def __init__(self, filename):
         self.filename = filename
         self.cards = []

    def read_file(self):
        try:
            with open(self.filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.cards = []
                for row_number, row in enumerate(reader):
                        try:
                            row['review'] = int(row['review'])
                            row['successful_review'] = int(row['successful_review'])
                            self.cards.append(dict(row))
                        except:
                            print(f"There was an issue parsing your data file on row {row_number + 2} \n{row}")
                            sys.exit()
            return self.cards
        except FileNotFoundError:
            print(bold_text + red_color + "File not found! Please make sure you have a << " + self.filename + " >> file in this directory." + reset_text)
            sys.exit()

    def update_file(self):
        fieldnames = self.cards[0].keys()
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.cards)