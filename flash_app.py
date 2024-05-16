import datetime
import random
import sys
import csv

cards = []

# read file of words
FILE = 'data.csv'

def read_file():
    with open(FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                row['review'] = int(row['review'])
                row['successful_review'] = int(row['successful_review'])
                cards.append(dict(row))

def update_file():
    fieldnames = cards[0].keys()
    with open(FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cards)

def create_card():
    print("Great! Let's add some new cards!")
    while True:
        sl = input("Front: ")
        tl = input("Back: ")
        pronunciation = input("Pronunciation: ")
        category = input("Category: ")
        example = input("Example: ")
        now = str(datetime.datetime.now())
        card = {'sl': sl, 'tl': tl, 'created_at': now, 'review': 0, 'successful_review': 0, 'successful_review': 0, 'category':category, 'example':example,'pronunciation': pronunciation}
        cards.append(card)
        update_file()
        quit = input("Add another? (y/n) ")
        if quit == "n":
            return False

def list_all_cards():
    if not cards:
        print("Sorry! There are no cards to print")
        start()

    print(f"Total number of cards: {len(cards)}")
    print("--------------------------")
    sorted_list = sorted(cards, key=lambda x: (x['successful_review'],-x['review']), reverse=True)

    for card in sorted_list:
        if card['review'] > 0:
            percent = card['successful_review'] / card['review'] * 100
        else:
            percent = 0

        print(f"{int(percent):>5}% | {card['successful_review']}/{card['review']} | {magenta_color} {card['sl']} {reset_text}\t=\t{orange_color} {card['tl']} {reset_text} ")

def quiz():
    '''
    get a random subset of all cards (10 maybe)
    present the english version of the word and learner guesses the dutch
    keep a score
    ''' 
    quiz_length = 10
    if not cards or len(cards) < quiz_length:
        print("Sorry! There aren't enough cards to test. Try creating some more.")
        start()
    
    quiz_session = random.sample(cards, quiz_length)

    count = 0
    score = 0

    print(f"# You will be tested on {len(quiz_session)} words")

    while count < len(quiz_session):
        for word in quiz_session:
            print(f"# Score: {score}/{len(quiz_session)}")
            print(orange_color + word['sl'] + reset_text)
            to_guess = word['tl']
            guess = input("> ")
            if guess == to_guess:
                print(green_color + "correct!" + reset_text)
                score += 1; 
            else:
                print(red_color + "Incorrect!" + reset_text)
            count += 1
    print(bold_text + f"You scored {score}/{len(quiz_session)} and got {round(score / len(quiz_session) * 100)}%" + reset_text)

def review():
    if not cards:
        print("Sorry! There are no cards to review. Try creating some first.")
        start()

    print("Let's Review! (press q to exit review at any time)")

    sorted_list = sorted(cards, key=lambda x: (x['successful_review'],-x['review']),)

    count = 0

    while count < len(cards):
        for word in sorted_list:
            print(orange_color + word['sl'] + reset_text)
            to_guess = word['tl']
            guess = input("> ").lower()

            if guess == "q":
                print("Good job!")
                update_file()
                start()

            word['review'] += 1


            if guess == to_guess:
                print(green_color + "correct!" + reset_text)
                word['successful_review'] += 1
            else:
                print(red_color + "Incorrect! " + reset_text + "The correct answer is: " + bold_text + to_guess + reset_text)

            count += 1
            print(f"#{count}")
    update_file()
    print("All words reviewed!")

def start():
    while True:
        choice = input(yellow_color + "(0) Review / (1) Quiz / (2) Add cards / (3) List cards / (4) Exit"  + reset_text + "\n>>> " )
        if choice == "0":
            review()
        elif choice == "1":
            quiz()
        elif choice == "2":
            create_card()
        elif choice == "3":
            list_all_cards()
        elif choice in ["4", "q", "quit"]:
            print("Goodbye!")
            sys.exit()
        else:
            print("Not a valid choice!")

red_color = "\033[91m"
green_color = "\033[32m"
yellow_color = "\033[33m"
orange_color = "\033[38;5;208m"
magenta_color = "\033[35m"
# Green: \033[32m
# Yellow: \033[33m
# Blue: \033[34m
# Magenta: \033[35m
# Cyan: \033[36m
bold_text = "\033[1m"
reset_text = "\033[0m"

print(
r'''


     _,---.              ,---.        ,-,--.  ,--.-,,-,--,
  .-`.' ,  \   _.-.    .--.'  \     ,-.'-  _\/==/  /|=|  |
 /==/_  _.-' .-,.'|    \==\-/\ \   /==/_ ,_.'|==|_ ||=|, |
/==/-  '..-.|==|, |    /==/-|_\ |  \==\  \   |==| ,|/=| _|
|==|_ ,    /|==|- |    \==\,   - \  \==\ -\  |==|- `-' _ |
|==|   .--' |==|, |    /==/ -   ,|  _\==\ ,\ |==|  _     |
|==|-  |    |==|- `-._/==/-  /\ - \/==/\/ _ ||==|   .-. ,|
/==/   \    /==/ - , ,|==\ _.\=\.-'\==\ - , //==/, //=/  |
`--`---'    `--`-----' `--`         `--`---' `--`-' `-`--`
      ''')

print(bold_text + "\033[1m" "Welcome to Flash! What would you like to do? \n" + reset_text )

try: 
    read_file()
except:
    print(red_color + "Please make sure you have a " + FILE + " file in this directory." + reset_text)
    sys.exit()
else:
    start()