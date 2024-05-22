import datetime
import random
import sys
import csv

FILE = 'data.csv'

def read_file(filename):
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cards = []
            for row_number, row in enumerate(reader):
                    try:
                        row['review'] = int(row['review'])
                        row['successful_review'] = int(row['successful_review'])
                        cards.append(dict(row))
                    except:
                        print(f"There was an issue parsing your data file on row {row_number + 2} \n{row}")
                        sys.exit()
        return cards
    except FileNotFoundError:
        print(bold_text + red_color + "File not found! Please make sure you have a "  + FILE + " file in this directory." + reset_text)
        sys.exit()

def update_file(file):
    fieldnames = cards[0].keys()
    with open(file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cards)

def create_card():
    print("Great! Let's add some new cards!")
    while True:
        front = input("Front: ")
        back = input("Back: ")
        pronunciation = input("Pronunciation: ")
        category = input("Category: ")
        example = input("Example: ")
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        card = {'front': front, 'back': back, 'created_at': now, 'review': 0, 'successful_review': 0, 'category':category, 'example':example,'pronunciation': pronunciation}
        cards.append(card)
        update_file(FILE)
        quit = input("Add another? (y/n) ")
        if quit == "n":
            return False

def list_all_cards():
    if not cards:
        print("Sorry! There are no cards to print. Try adding some first.")
        start()

    print(rf'''************************************************************
Total number of cards: {bold_text}{len(cards)}{reset_text} 
************************************************************''')

    sorted_list = sorted(cards, key=lambda x: (x['successful_review'],-x['review']), reverse=True)

    for card in sorted_list:
        if card['review'] > 0:
            percent = card['successful_review'] / card['review'] * 100
        else:
            percent = 0
        
        fraction = f"{card['successful_review']}/{card['review']}"

        print(f"{int(percent):>4}% | {fraction:>6} | {cyan_color} {card['back']} {reset_text} / {orange_color} {card['front']} {reset_text} ")

def check_answer(to_guess, guess):
    # need to consider cases: answer("de vegetariër", "de vegetarier")
    # would be good to consider het/de cases
    if guess == to_guess:
        return True

def user_input():
    guess = input("> ").lower().strip()
    return guess

def quiz(num):
    quiz_length = num

    if not cards or len(cards) < quiz_length:
        print(f"Sorry! You need at least {quiz_length} cards for a quiz. Try creating some more cards and try again.")
        start()
    
    quiz_session = random.sample(cards, quiz_length)

    count = 0
    score = 0

    print(f"# You will be tested on {len(quiz_session)} words")

    while count < len(quiz_session):
        for word in quiz_session:
            print(f"# Score: {score}/{count}")
            print(orange_color + word['front'] + reset_text)
            to_guess = word['back']

            guess = user_input()

            while not guess:
                print("> You can't give a blank response")
                guess = user_input()

            if check_answer(guess, to_guess):
                print(green_color + "CORRECT! " + reset_text)
                score += 1
            else:
                print(red_color + "INCORRECT! " + reset_text)

            count += 1

    percent = round(score / len(quiz_session) * 100)

    if percent == 100:
        print(bold_text + f"🎉🏆 AMAZING JOB! YOU GOT 100% ({score}/{len(quiz_session)}) 🏆🎉\n" + reset_text)
    else:
        print(bold_text + f"You scored {score}/{len(quiz_session)} and got {percent}% \n" + reset_text)

def create_review_session(num_cards):
    for_review = []
    max_new_cards = 5
    new_cards = 0

    for card in cards:
        if card['review'] == 0 and len(for_review) < max_new_cards:
            new_cards += 1
            for_review.append(card)

    session = random.sample(cards, num_cards - new_cards)

    for_review.extend(session)

    return for_review

def review():
    if not cards:
        print("Sorry! There are no cards to review. Try creating some first.")
        start()

    print("Let's Review! (press 'q' to exit review at any time)")

    sorted_list = create_review_session(10)

    count = 0

    while count < len(sorted_list):
        for word in sorted_list:
            word['last_review']
            print(f"#{count+1}")
            print(orange_color + word['front'] + reset_text)
            to_guess = word['back']

            guess = user_input()

            while not guess:
                print("> You can't give a blank response")
                guess = user_input()

            if guess == "q":
                print("Good job! 👍👍👍")
                update_file(FILE)
                start()
            
            word['review'] += 1

            word['last_review']

            if check_answer(guess, to_guess):
                print(green_color + "CORRECT! " + reset_text)
                word['successful_review'] += 1
                now = datetime.datetime.now().strftime('%Y-%m-%d')
                word['last_review'] = now
            else:
                print(red_color + "INCORRECT! " + reset_text + "The correct answer is: " + bold_text + to_guess + reset_text)

            count += 1
 
    update_file(FILE)
    print(f"{len(sorted_list)} words reviewed! Amazing! 🥇")

def start():
    while True:
        choice = input(bold_text + blue_color + "(0) Review / (1) Quiz / (2) Add cards / (3) List cards / (4) Exit"  + reset_text + "\n>>> " )
        if choice == "0":
            review()
        elif choice == "1":
            quiz(10)
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
cyan_color = "\033[36m"
green_color = "\033[32m"
blue_color = "\033[34m"
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

cards = read_file(FILE)

def main() -> None:
    print(bold_text + "\033[1m" "Welcome to Flash! What would you like to do? \n" + reset_text )
    start()

if __name__ == "__main__":
    main()