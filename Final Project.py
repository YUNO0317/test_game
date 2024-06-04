
def display_instructions():

    print("Display How to play?")
    instruction = input("Please enter '1' to continue or '2' for skipping ")
    try:
        validate_input(int(instruction))
    except ValueError:
        print("not number")
        display_instructions()
    if int(instruction) ==1:
        try:
            with open("How to play the Pokémon.txt", "r") as file_How_to_play:
                content = file_How_to_play.readlines()
                for line in content:
                    print(line.strip())
        except FileNotFoundError:
            print("Sorry, we cannot find the instruction")
    # else:
    display_description()

def display_description():
    print("You can find a description of Pokémon below. Press 1 for description, press 2 for selection of Pokémon")
    description = input()
    try:
        validate_input(int(description))
    except ValueError:
        print("not number")
        display_description()
    if int(description) == 1:
        try:
            with open("description of Pokémon.txt", "r") as file_description:
                content = file_description.readlines()
                for line in content:
                    print(line.strip())
        except FileNotFoundError:
            print("Sorry, we cannot find the description")
    # else:
    select_Pokemon()

def validate_input(number: int):
    if number == 1 or number == 2:
        return True
    else:
        print("Invalid input. Please enter '1' or '2")

def select_Pokemon():
    print("For selection a Pokemon: ") 
    print("You pokemon is: ")

def opponent_Pokemon():
    print("You will fight with: ")

print("Welcome to Powers of Pokémon")
display_instructions()
opponent_Pokemon()