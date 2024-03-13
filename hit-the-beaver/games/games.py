import main
import random

def start():
    while True:
        pit_shape = "|_|"
        empty_pit = [pit_shape] * 4

        beaver_position = random.randint(1,4)

        pit = empty_pit.copy()
        pit[beaver_position - 1] = "|0_0|"

        empty_pit = " ".join(empty_pit)
        pit = " ".join(pit)

        print(f"Take a look at the pit below\n\n{empty_pit}\n")

        user_choice = int(input("What the pit number do you think beaver is in? [ 1 / 2 / 3 / 4 ] "))

        if user_choice == beaver_position:
            print(f"\n{pit}\n\nCongratulations, You Win 🏆\n")
        else:
            print(f"\n{pit}\n\nYou Lose 🙊\n")

        play_again = input("Do you want continue the game? [y/n] ")
        if play_again == "n":
            main.menu()

if __name__ == '__main__':
    start()
