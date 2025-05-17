import random

def play_game():
    print("welcome to the gusseing game")
    print("enter a letter")
    correct_key = random.choice(['a','b','c','d'])

    print(f"a  b   c   d")
    guess = input("your guess").lower()

    if guess == correct_key:
        print("your a goat")
    else:
        print("your out of luck")
 
