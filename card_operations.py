import datetime
from text_formatting import colors


class CardOperations:
    def __init__(self, file_ops):
        self.file_ops = file_ops

    def create_card(self):
        print("Great! Let's add some new cards!")
        while True:
            front = input("Front: ")
            back = input("Back: ")
            category = input("Category: ")
            example = input("Example: ")
            now = datetime.datetime.now().strftime('%Y-%m-%d')
            card = {
                'front': front, 
                'back': back, 
                'created_at': now, 
                'review': 0, 
                'successful_review': 0, 
                'category': category,
                'example': example,
                'last_review': ""
            }
            self.file_ops.cards.append(card)
            self.file_ops.update_file()

            quit_add = input("Add another? (y/n) ")
            if quit_add.lower() == "n":
                return False
            
    def list_all_cards(self):
        cards = self.file_ops.cards

        if not cards:
            print("Sorry! There are no cards to print. Try adding some first.")
            return
        
        print(rf'''************************************************************
Total number of cards: {colors['bold_text']}{len(cards)}{colors['reset_text']} 
************************************************************''')

        sorted_list = sorted(cards, key=lambda x: (x['successful_review'], -x['review']), reverse=True)

        for card in sorted_list:
            if card['review'] > 0:
                percent = card['successful_review'] / card['review'] * 100
            else:
                percent = 0
            
            fraction = f"{card['successful_review']}/{card['review']}"

            print(f"{int(percent):>4}% | {fraction:>6} | {colors['cyan_color']} {card['back']}"
                  f"{colors['reset_text']} / {colors['orange_color']} {card['front']} {colors['reset_text']} ")
