import datetime
import random
import sys
from file_operations import FileOperations
from card_operations import CardOperations

FILE = 'data.csv'


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
        return
    
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
        return

    print("Let's Review! (press 'q' to exit review at any time)")

    sorted_list = create_review_session(5)

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
                file_ops.update_file()
                return
            
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
 
    file_ops.update_file()
    print(f"{len(sorted_list)} words reviewed! Amazing! 🥇")

def start():
    while True:
        choice = input(bold_text + blue_color + "(0) Review / (1) Quiz / (2) Add cards / (3) List cards / (4) Exit"  + reset_text + "\n>>> " )
        if choice == "0":
            review()
        elif choice == "1":
            quiz(10)
        elif choice == "2":
            card_manager.create_card()
        elif choice == "3":
            card_manager.list_all_cards()
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

file_ops = FileOperations(FILE)
cards = file_ops.read_file()
card_manager = CardOperations(file_ops)

def main() -> None:
    print(bold_text + "\033[1m" "Welcome to Flash! What would you like to do? \n" + reset_text )
    start()

if __name__ == "__main__":
    main()