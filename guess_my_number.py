import random
import argparse


def guess_number(name):
    play_game = True
    game_count = 0
    wins_count = 0

    while play_game == True:
        guess = input(f"{name}, guess the number I'm thinking of from 1 to 3\n")
        while guess not in ["1", "2", "3"]:
            guess = input("I said a number from 1 to 3 you brute, guess properly!\n")
        number = random.randint(1,3)
        if int(guess) == number:
            print(f"{name} wins")
            wins_count += 1
        else:
            print(f"🐍 wins")
        game_count += 1
        print(f"Game count : {game_count}\n {name} wins : {wins_count}\n Winning percentage {wins_count/game_count*100} %")
        play_game = input(f"{name}, if you want to play again, write yes\n")
        if play_game == "yes":
            play_game = True
        else:
            play_game = False
            print("The game is closed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number guesssing app")
    parser.add_argument("-n", "--name", required=True, help="Name of the person playing the game")
    args = parser.parse_args()
    guess_number(args.name)