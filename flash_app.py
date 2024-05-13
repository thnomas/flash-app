import datetime
import random
import sys
import csv

# dummy data
# cards = [{'sl': 'the table', 'tl': 'de tafel', 'created_at': '2024-05-09 09:03:48.150230', 'review': 0, 'successful_review': 0}, {'sl': 'the child', 'tl': 'het kind', 'created_at': '2024-05-09 09:04:06.584126', 'review': 0, 'successful_review': 0}, {'sl': 'the dog', 'tl': 'de hond', 'created_at': '2024-05-09 09:04:17.273715', 'review': 0, 'successful_review': 0},{'sl': 'the house', 'tl': 'het huis', 'created_at': '2024-05-09 09:06:15.937622', 'review': 0, 'successful_review': 0},{'sl': 'the car', 'tl': 'de auto', 'created_at': '2024-05-09 09:06:45.628731', 'review': 0, 'successful_review': 0}]
cards = [
    {'sl': 'the table', 'tl': 'de tafel', 'created_at': '2024-05-09 09:03:48.150230', 'review': 0, 'successful_review': 0},
    {'sl': 'the child', 'tl': 'het kind', 'created_at': '2024-05-09 09:04:06.584126', 'review': 0, 'successful_review': 0},
    {'sl': 'the dog', 'tl': 'de hond', 'created_at': '2024-05-09 09:04:17.273715', 'review': 0, 'successful_review': 0},
    {'sl': 'the house', 'tl': 'het huis', 'created_at': '2024-05-09 09:06:15.937622', 'review': 0, 'successful_review': 0},
    {'sl': 'the car', 'tl': 'de auto', 'created_at': '2024-05-09 09:06:45.628731', 'review': 0, 'successful_review': 0},
    {'sl': 'the book', 'tl': 'het boek', 'created_at': '2024-05-09 09:07:05.821362', 'review': 0, 'successful_review': 0},
    {'sl': 'the cat', 'tl': 'de kat', 'created_at': '2024-05-09 09:07:23.453810', 'review': 0, 'successful_review': 0},
    {'sl': 'the tree', 'tl': 'de boom', 'created_at': '2024-05-09 09:07:45.967224', 'review': 0, 'successful_review': 0},
    {'sl': 'the man', 'tl': 'de man', 'created_at': '2024-05-09 09:08:07.392714', 'review': 0, 'successful_review': 0},
    {'sl': 'the woman', 'tl': 'de vrouw', 'created_at': '2024-05-09 09:08:28.651729', 'review': 0, 'successful_review': 0},
    {'sl': 'the boy', 'tl': 'de jongen', 'created_at': '2024-05-09 09:08:47.926815', 'review': 0, 'successful_review': 0},
    {'sl': 'the girl', 'tl': 'het meisje', 'created_at': '2024-05-09 09:09:06.207432', 'review': 0, 'successful_review': 0},
    {'sl': 'the chair', 'tl': 'de stoel', 'created_at': '2024-05-09 09:09:24.476128', 'review': 0, 'successful_review': 0},
    {'sl': 'the phone', 'tl': 'de telefoon', 'created_at': '2024-05-09 09:09:42.720921', 'review': 0, 'successful_review': 0},
    {'sl': 'the computer', 'tl': 'de computer', 'created_at': '2024-05-09 09:10:00.981555', 'review': 0, 'successful_review': 0},
    {'sl': 'the pen', 'tl': 'de pen', 'created_at': '2024-05-09 09:10:19.210713', 'review': 0, 'successful_review': 0},
    {'sl': 'the pencil', 'tl': 'het potlood', 'created_at': '2024-05-09 09:10:37.418005', 'review': 0, 'successful_review': 0},
    {'sl': 'the desk', 'tl': 'het bureau', 'created_at': '2024-05-09 09:10:55.667824', 'review': 0, 'successful_review': 0},
    {'sl': 'the lamp', 'tl': 'de lamp', 'created_at': '2024-05-09 09:11:13.937418', 'review': 0, 'successful_review': 0},
    {'sl': 'the door', 'tl': 'de deur', 'created_at': '2024-05-09 09:11:32.169715', 'review': 0, 'successful_review': 0},
    {'sl': 'the window', 'tl': 'het raam', 'created_at': '2024-05-09 09:11:50.376214', 'review': 0, 'successful_review': 0},
    {'sl': 'the cup', 'tl': 'de kop', 'created_at': '2024-05-09 09:12:08.590615', 'review': 0, 'successful_review': 0},
    {'sl': 'the chair', 'tl': 'de stoel', 'created_at': '2024-05-09 09:12:45.001729', 'review': 0, 'successful_review': 0},
    {'sl': 'the desk', 'tl': 'het bureau', 'created_at': '2024-05-09 09:13:03.221542', 'review': 0, 'successful_review': 0}
]

difficult_cards = []
# output to csv
# fieldnames = cards[0].keys()
# csv_file = "output.csv"
# with open(csv_file, mode="w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(cards)


def create_card():
    '''
    Create a new card.
    '''
    print("Great! Let's add some new words!")
    while True:
        sl = input("English: ")
        tl = input("Nederlands: ")
        now = str(datetime.datetime.now())
        card = {'sl': sl, 'tl': tl, 'created_at': now}
        cards.append(card)
        quit = input("Add another? (y/n) ")
        if quit == "n":
            return False

def list_all_cards():
    if not cards:
        print("Sorry! There are no cards to print")
        main()

    print(f"Total number of cards: {len(cards)}")
    print("--------------------------")
    sorted_list = sorted(cards, key=lambda x: (x['successful_review'],x['review']), reverse=True)

    for card in sorted_list:
        print(f"{card['successful_review']}/{card['review']} | {magenta_color} {card['sl']} {reset_text}\t=\t{orange_color} {card['tl']} {reset_text} ")

def quiz():
    '''
    get a random subset of all cards (10 maybe)
    present the english version of the word and learner guesses the dutch
    keep a score
    ''' 
    quiz_length = 10
    if not cards or len(cards) < quiz_length:
        print("Sorry! There aren't enough cards to test. Try creating some more.")
        main()
    
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

def review(cards):
    '''
    Ideally will use Spaced repition - choosing only cards that are due to be reviewed. Not scored like a test.
    '''
    if not cards:
        print("Sorry! There are no cards to review. Try creating some first.")
        main()

    print("Let's Review! (press q to exit review at any time)")

    # decide what to review
    # 
    a = input("Choose you review session: (0) Regular / (1) Difficult words / (2) By category  \n>>> ")
    print(a)

    if a == '1':
        print(difficult_cards)
    
    count = 0
    while count < len(cards):
        word = random.choice(cards)
        print(orange_color + word['sl'] + reset_text)
        to_guess = word['tl']
        guess = input("> ")
        word['review'] += 1

        if guess == "q":
            break

        if guess == to_guess:
            print(green_color + "correct!" + reset_text)
            word['successful_review'] += 1
        else:
            print(red_color + "Incorrect!" + reset_text)
            if word['successful_review'] / word['review'] < 20:
                print(word['successful_review'] / word['review'])
                difficult_cards.append(word)
            print(difficult_cards)
        count += 1

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
# White: \033[37m
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

def main():
    while True:
        choice = input(yellow_color + "(0) Review / (1) Quiz / (2) Add cards / (3) List cards / (4) Stats / (5) Exit"  + reset_text + "\n>>> " )
        if choice == "0":
            review(cards)
        elif choice == "1":
            quiz()
        elif choice == "2":
            create_card()
        elif choice == "3":
            list_all_cards()
        elif choice == "4":
            print("Stats:")
            print(f"Cards: 55")
        elif choice in ["5", "q", "quit"]:
            print("Goodbye! / Tot ziens!")
            sys.exit()
        else:
            print("Not a valid choice!")

main()