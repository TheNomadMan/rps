import random
valid_choices = ['rock', 'paper', 'scissors']
play_again_options = ['yes', 'no']
while True:

    while True:
        user_choice = str(input("'Rock', 'Paper', or 'Scissors'?\n")).lower()
        if user_choice in valid_choices:
            print()
            print("You picked:", user_choice.capitalize())
            break
        else:
            print("That's not a valid choice, try again")

    computer_pick = random.choice(valid_choices)
    print("The computer chose:", computer_pick.capitalize())
    print()
    if computer_pick == user_choice:
        print("Its a tie!")
    elif computer_pick == "rock" and user_choice == "scissors":
        print("Rock beats Scissors: you lost.")
    elif computer_pick == "scissors" and user_choice == "paper":
        print("Scissors beats Paper: you lost.")
    elif computer_pick == "paper" and user_choice == "rock":
        print("Paper beats Rock: you lost.")
    elif user_choice == "rock" and computer_pick == "scissors":
        print("Rock beats Scissors: YOU WON!")
    elif user_choice == "scissors" and computer_pick == "paper":
        print("Scissors beats Paper: YOU WON!")
    elif user_choice == "paper" and computer_pick == "rock":
        print("Paper beats Rock: YOU WON!")
    else:
        print("Something went wrong")
    print()
    while True:
        print("Would you like to play again?")
        play_again = str(input("'Yes' or 'No'\n")).lower()
        if play_again in play_again_options:
            if play_again == "no":
                print("Goodbye!")
                break
            elif play_again == "yes":
                print()
                print("Yay!\n")
                break
        else:
            print()
            print("Huh?\n")
    if play_again == "no":
        break