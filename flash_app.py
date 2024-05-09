import datetime
import random
import sys

# dummy data
cards = [{'sl': 'the table', 'tl': 'de tafel', 'created_at': '2024-05-09 09:03:48.150230'}, {'sl': 'the child', 'tl': 'het kind', 'created_at': '2024-05-09 09:04:06.584126'}, {'sl': 'the dog', 'tl': 'de hond', 'created_at': '2024-05-09 09:04:17.273715'},{'sl': 'the house', 'tl': 'het huis', 'created_at': '2024-05-09 09:06:15.937622'},{'sl': 'the car', 'tl': 'de auto', 'created_at': '2024-05-09 09:06:45.628731'}]

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
        print(list_cards())

def list_cards():
    # for card in cards:
    return(cards)

def list_all_cards():
    if not cards:
        print("Sorry! There are no cards to print")
    else:
        print(f"Total number of cards: {len(cards)}")
        print("--------------------------")
        for card in cards:
            print(f"> {magenta_color} {card['sl']} {reset_text}\t=\t{orange_color} {card['tl']} {reset_text} ")

def quiz():
    # get a random subset of all cards (10 maybe)
    # present the english version of the word and learner guesses the dutch
    # keep a score
    if not cards or len(cards) < 3:
        print("Sorry! There aren't enough cards to test. Try creating some more.")
    else:
        review_session = random.sample(cards, 3)

        count = 0
        score = 0

        print(f"# You will be tested on {len(review_session)} words")

        while count < len(review_session):
            print(f"# Score: {score}/{len(review_session)}")
            word = random.choice(review_session) # bug
            print(orange_color + word['sl'] + reset_text)
            to_guess = word['tl']
            guess = input("> ")
            if guess == to_guess:
                print(green_color + "correct!" + reset_text)
                score += 1; 
            else:
                print(red_color + "Incorrect!" + reset_text)
            count += 1
        print(bold_text + f"You scored {score}/{len(review_session)} and got {round(score / len(review_session) * 100)}%" + reset_text)

def random_card():
    pass
    # r = random.choice(cards)
    # print(r)

def check_guess():
    # if the key
    pass

# random_card()

def review(cards):
    '''
    Ideally will use Spaced repition - choosing only cards that are due to be reviewed. Not scored like a test.
    '''
    if not cards:
        print("Sorry! There are no cards to review. Try creating some first.")
    else:
        print("Let's Review!")
        # review_session = random.shuffle(words, 1)
        
        count = 0
        while count < len(cards):
            word = random.choice(cards)
            print(word['sl'])
            to_guess = word['tl']
            guess = input("> ")
            if guess == to_guess:
                print(green_color + "correct!" + reset_text)
            else:
                print(red_color + "Incorrect!" + reset_text)
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

while True:
    choice = input(yellow_color + "(0) Review / (1) Test / (2) Add cards / (3) Stats / (4) List cards / (5) Exit"  + reset_text + "\n>>> " )
    if choice == "0":
        review(cards)
    elif choice == "1":
        quiz()
    elif choice == "2":
        create_card()
    elif choice == "3":
        print("Stats:")
        print(f"Cards: 55")
    elif choice == "4":
        list_all_cards()
    elif choice == "5":
        print("Goodbye! / Tot ziens!")
        sys.exit()
    else:
        print("Not a valid choice!")