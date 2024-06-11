import datetime
import random
import sys
from file_operations import FileOperations
from card_operations import CardOperations
from session import Session
from text_formatting import colors

FILE = 'data.csv'


def create_review_session(num_cards):
    
    for_review = []
    max_new_cards = 5
    new_cards = 0

    for card in cards:
        if card['review'] == 0 and len(for_review) < max_new_cards:
            new_cards += 1
            for_review.append(card)

    sess = random.sample(cards, num_cards - new_cards)

    for_review.extend(sess)

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
            print(f"#{count+1}")
            print(colors['orange_color'] + word['front'] + colors['reset_text'])
            to_guess = word['back']

            guess = session.user_input()

            while not guess:
                print("> You can't give a blank response")
                guess = session.user_input()

            if guess == "q":
                print("Good job! 👍👍👍")
                file_ops.update_file()
                return
            
            word['review'] += 1

            if session.check_answer(guess, to_guess):
                print(colors['green_color'] + "CORRECT! " + colors['reset_text'])
                word['successful_review'] += 1
                now = datetime.datetime.now().strftime('%Y-%m-%d')
                word['last_review'] = now
            else:
                print(colors['red_color'] + "INCORRECT! " + colors['reset_text'] + "The correct answer is: " + colors['bold_text'] + to_guess + colors['reset_text'])

            count += 1
 
    file_ops.update_file()
    print(f"{len(sorted_list)} words reviewed! Amazing! 🥇")


def menu():
    while True:
        choice = input(colors['bold_text'] + colors['blue_color'] + "(0) Review / (1) Quiz / (2) Add cards / (3) List cards / (4) Exit" + colors['reset_text'] + "\n>>> ")
        if choice == "0":
            review()
        elif choice == "1":
            message = session.quiz(7)
            if message:
                print(message)
        elif choice == "2":
            card_manager.create_card()
        elif choice == "3":
            card_manager.list_all_cards()
        elif choice in ["4", "q", "quit"]:
            print("Goodbye!")
            sys.exit()
        else:
            print("Not a valid choice!")


print(r'''


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
session = Session(file_ops)


def main() -> None:
    print(colors['bold_text'] + "\033[1m" "Welcome to Flash! What would you like to do? \n" + colors['reset_text'])
    menu()


if __name__ == "__main__":
    main()
