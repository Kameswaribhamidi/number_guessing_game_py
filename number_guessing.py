'''
1.pick a random number
2.ask to make a guess
3. check if the guesses number is greater or less than picked one
4. maintain lives count
'''
logo="""
   _____                       _   _                                   _                                              _ 
  / ____|                     | | | |                                 | |                                            | |
 | |  __ _   _  ___ ___ ___   | |_| |__   ___    _ __  _   _ _ __ ___ | |__   ___ _ __    __ _  __ _ _ __ ___   ___  | |
 | | |_ | | | |/ _ / __/ __|  | __| '_ \ / _ \  | '_ \| | | | '_ ` _ \| '_ \ / _ | '__|  / _` |/ _` | '_ ` _ \ / _ \ | |
 | |__| | |_| |  __\__ \__ \  | |_| | | |  __/  | | | | |_| | | | | | | |_) |  __| |    | (_| | (_| | | | | | |  __/ |_|
  \_____|\__,_|\___|___|___/   \__|_| |_|\___|  |_| |_|\__,_|_| |_| |_|_.__/ \___|_|     \__, |\__,_|_| |_| |_|\___| (_)
                                                                                          __/ |                         
                                                                                         |___/                          
"""                                                                                       
from random import randint
import sys
EASY_LIVES=10
HARD_LIVES=5
def difficulty():
    """Sets the difficulty level."""
    inp=input("Choose difficulty level {easy/hard}: ")
    if inp=='easy':
        return EASY_LIVES
    else:
        return HARD_LIVES
def play(inp,lifes):
    """Checks the users input and return the final answer"""
    print(f"You have {lifes} chances to guess the number.")
    while lifes!=0:
        ch=int(input("Make a guess: "))
        if ch<0:
            print(f"The guessed number, {ch} not valid.")
        else:
            if ch==inp:
                print(f"You Win!. The answer is {ch}.")
                break 
            elif ch>inp:
                print("Too High!")
                lifes-=1
                print(f"You have {lifes} chances left.")
            elif ch<inp:
                print("Too Low!")
                lifes-=1
                print(f"You have {lifes} chances left.")
    else:
        print(f"The correct number is {inp}. You Loose!")
    print()
    choice = input("Do you want to continue the game?")
    if choice == 'n':
        exit()
    else:
        game()
def game():
    print()
    print("Think of a number between 1 and 100: ")
    lifes=difficulty()
    inp=randint(1,101)
    play(inp,lifes)

print(logo)
print("Welcome!")
print()
game()