import random
from text_formatting import colors


class Session:
    def __init__(self, file_ops):
        self.file_ops = file_ops

    def user_input(self):
        self.guess = input("> ").lower().strip()
        return self.guess
    
    def check_answer(self, guess, to_guess):
        # need to consider cases: answer("de vegetariër", "de vegetarier")
        # would be good to consider het/de cases
        if guess.lower() == to_guess.lower():
            
            return True
        else:
            return False
        
    def quiz(self, quiz_length):
        cards = self.file_ops.cards
        if not cards or len(cards) < quiz_length:
            message = f"Sorry! You need at least {quiz_length} cards for a quiz. Try creating some more cards and try again."
            return message
        
        quiz_session = random.sample(cards, quiz_length)

        count, score = 0, 0

        print(f"# You will be tested on {len(quiz_session)} words")

        while count < len(quiz_session):
            for word in quiz_session:
                print(f"# Score: {score}/{count}")
                print(colors['orange_color'] + word['front'] + colors['reset_text'])
                to_guess = word['back']

                guess = self.user_input()

                while not guess:
                    print("> You can't give a blank response")
                    guess = self.user_input()

                if self.check_answer(guess, to_guess):
                    print(colors['green_color'] + "CORRECT! " + colors['reset_text'])
                    score += 1
                else:
                    print(colors['red_color'] + "INCORRECT! " + colors['reset_text'])

                count += 1

        percent = round(score / len(quiz_session) * 100)

        if percent == 100:
            print(colors['bold_text'] + f"🎉🏆 AMAZING JOB! YOU GOT 100% ({score}/{len(quiz_session)}) 🏆🎉\n" + colors['reset_text'])
        else:
            print(colors['bold_text'] + f"You scored {score}/{len(quiz_session)} and got {percent}% \n" + colors['reset_text'])
