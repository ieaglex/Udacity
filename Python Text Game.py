import chance
import time
import random


def print_slow(my_string):
    print(my_string)
    time.sleep(2)


def intro():
    print_slow("You wake up disoriented and look around.")
    print_slow("You're in a small room that you don't recognize.")
    print_slow("You see a metal door, a wooden nightstand, a panel "
               "on the wall, and a small bed.")


def choice1(health, items, randomlock):
    if "Large_key" not in items and "Small_key" not in items:
        print_slow("The door is locked")
        main_game(health, items, randomlock)
    elif "Small_key" in items and "Large_key" not in items:
        print_slow("The small key doesn't fit the door.")
        main_game(health, items, randomlock)
    elif "Large_key" in items:
        print_slow("The key fits!")
        print_slow("You open the door.")
        print_slow("You run outside and escape!")
        print_slow("Victory!")
        play_again(health, items, randomlock)


def choice2(health, items, randomlock):
    if "Code" not in items:
        print_slow("The nightstand has a lock on it that needs three numbers "
                   "that you don't know.")
        main_game(health, items, randomlock)
    elif "Code" in items and "Small_key" not in items:
        print_slow("You are pretty sure that the numbers from the bed are "
                   "related to this code.")
        print_slow("You know the first two numbers are 3 and 7.")
        print_slow("You will have to guess at what the last one is.")
        while True:
            lockchoice = input("What is your guess?\n")
            if lockchoice == str(randomlock):
                print_slow("You got it right! The nightstand is open.")
                print_slow("There is a small key inside that you take.")
                items.append("Small_key")
                main_game(health, items, randomlock)
            else:
                print_slow("That didn't work. Let's try another one.")
    else:
        print_slow("The nightstand is now empty")
        main_game(health, items, randomlock)


def choice3(health, items, randomlock):
    if "Small_key" not in items:
        print_slow("The panel doesn't budge.")
        main_game(health, items, randomlock)
    elif "Small_key" in items and "Large_key" not in items:
        print_slow("The panel swings open, revealing a much larger key inside "
                   "of a glass case")
        glassanswer = input("Would you like to break the glass to get the "
                            "key? It will likely hurt.\n(Yes or No)\n").lower()
        if "yes" in glassanswer:
            print_slow("You break the glass and grab the key, taking some "
                       "damage in the process")
            items.append("Large_key")
            health -= 1
            if health == -1:
                print_slow("You lost too much health and can't continue.")
                print_slow("Game over")
                play_again(health, items, randomlock)
            else:
                main_game(health, items, randomlock)
        else:
            main_game(health, items, randomlock)
    else:
        print_slow("The panel is empty")
        main_game(health, items, randomlock)


def choice4(health, items, randomlock):
    if "Code" not in items:
        print_slow("On the bed there are the numbers \"3, 7, _\".")
        print_slow("Unfortunately you aren't able to read the third number.")
        items.append("Code")
        main_game(health, items, randomlock)
    else:
        print_slow("You take a quick nap and regain a little health. ")
        health = 3
        print_slow("You have " + str(health) + " health now!")
        main_game(health, items, randomlock)


def choice5(health, items, randomlock):
    if health == 3:
        print_slow("You hit the door several times and hurt your hand.")
        print_slow("Nobody is responding to your calls.")
        print_slow("This was probably a bad choice.")
        health -= 1
        main_game(health, items, randomlock)
    elif health == 2:
        print_slow("There is no response.")
        print_slow("Your hands are in a lot of pain")
        health -= 1
        main_game(health, items, randomlock)
    elif health == 1:
        print_slow("Still no response and your hands aren't looking so good.")
        print_slow("Hitting the door again would be a bad idea")
        health -= 1
        main_game(health, items, randomlock)
    else:
        print_slow("You hit the door a final time. The pain causes your eyes "
                   "to blur and then shut.")
        print_slow("Game Over")
        play_again(health, items, randomlock)


def main_game(health, items, randomlock):
    print_slow("Enter the number of what you would like to do")
    choice = input("1. Open the door\n2. Check the nightstand\n3. Open "
                   "the panel\n4. Check the bed\n5. Punch the door "
                   "while yelling for help\n")
    if choice == "1":
        choice1(health, items, randomlock)
    elif choice == "2":
        choice2(health, items, randomlock)
    elif choice == "3":
        choice3(health, items, randomlock)
    elif choice == "4":
        choice4(health, items, randomlock)
    elif choice == "5":
        choice5(health, items, randomlock)
    else:
        main_game(health, items, randomlock)


def play_again(health, items, randomlock):
    playagain = input("Would you like to play again?\n(Yes or No)\n").lower()
    if "yes" in playagain:
        new_game()
    elif "no" in playagain:
        print_slow("Thanks for playing!")
        exit()
    else:
        play_again(health, items, randomlock)


def new_game():
    items = []
    health = 3
    randomlock = random.randint(0, 9)
    intro()
    main_game(health, items, randomlock)


new_game()
