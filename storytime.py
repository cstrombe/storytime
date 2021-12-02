#!/usr/bin/evn python3

ALL_QUESTIONS = {
     "0": {"question": "What do you want to be?", "answers": {"1": "banker", "2": "investor"}},
     # 1 = they chose banker
     "1": {"question": "What bank do you work at?", "answers": {"3": "Wells Fargo", "4": "Bank of America"}},
     # 2 = they chose investor
     "2": {"question": "What's your favorite stock?", "answers": {"5": "AAPL", "6": "TSLA"}},
     # 3 = they chose wells fargo bank
     "3": {"question": "Go into the vault at the bank?", "answers": {"7": "yes", "8": "no"}},
     #..... etc!
     }

# Show the next question to the user, and get their answer.
# Only let them enter one of the specified number choices for the question, or "q" if they want to quit.
def ask_question(question_info):
     print(question_info["question"])
     print(question_info["answers"])
     answer = None
     while answer not in question_info["answers"].keys() and answer != "q":
          answer = input("? ")
     return answer


def main():
     keep_going = True
     answer = "0"

     while keep_going:
          answer = ask_question(ALL_QUESTIONS[answer])
          if answer == "q": # q for "quit"
               keep_going = False

     print("Thanks for playing!")


if __name__ == '__main__':
     main()
