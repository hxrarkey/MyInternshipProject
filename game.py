import time

# Define the game storyline and initial situation
def intro():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("You have two paths ahead of you. Which one do you choose?")
    time.sleep(1)
    print("1. Go left")
    print("2. Go right")

# Define a function to handle the user's choices
def make_choice():
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        path_left()
    elif choice == "2":
        path_right()
    else:
        print("Invalid input. Please enter 1 or 2.")
        make_choice()

# Define the outcomes for the left path
def path_left():
    print("You chose to go left.")
    time.sleep(1)
    print("You encounter a friendly group of elves who offer to guide you.")
    time.sleep(1)
    print("Do you accept their offer?")
    time.sleep(1)
    print("1. Accept the offer")
    print("2. Decline the offer")
    choice = input("Enter your choice (1/2):")
    if choice == "1":
        print("The elves guide you safely out of the forest. You win!")
    elif choice == "2":
        print("You continue on your own and get lost. Game over.")
    else:
        print("Invalid input. Please enter 1 or 2.")
        path_left()

# Define the outcomes for the right path
def path_right():
    print("You chose to go right.")
    time.sleep(1)
    print("You stumble upon a hidden treasure chest.")
    time.sleep(1)
    print("Do you open it?")
    time.sleep(1)
    print("1. Open the chest")
    print("2. Leave it and keep going")
    choice = input("Enter your choice (1/2):")
    if choice == "1":
        print("The chest contains valuable treasures. You win!")
    elif choice == "2":
        print("You decide to leave the chest and continue your journey. The forest gets darker, and you're never seen again. Game over.")
    else:
        print("Invalid input. Please enter 1 or 2.")
        path_right()

# Main game loop
def play_game():
    intro()
    make_choice()

# Start the game
play_game()
