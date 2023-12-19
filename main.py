import csv
from colored import fg, attr, bg
from functions import log_run, view_log, edit_log, remove_log

runs_file = "runs.csv"

# Check if runs file exist and if not create one
try:
    with open(runs_file, "r"):
        pass
except FileNotFoundError:
    with open(runs_file, "w") as rxn_file:
        rxn_file.write("TITLE,DATE,DISTANCE,TIME TAKEN,NOTES\n")

def main():
    """
    Main function to run the RXN application.
    """
    # ASCII art for app logo
    ascii_art = """
 _______     ____  ____  ____  _____  
|_   __ \   |_  _||_  _||_   \|_   _| 
  | |__) |    \ \  / /    |   \ | |   
  |  __ /      > `' <     | |\ \| |   
 _| |  \ \_  _/ /'`\ \_  _| |_\   |_  
|____| |___||____||____||_____|\____|
    """
    print(ascii_art)

    # Welcome message
    print("Welcome to RXN! Your personal running journal.")

    # Function - app instruction outputs
    def main_menu():
        """
        Display the main menu and get user input.
        """
        print(f"\n{fg('black')} {bg('white')}Please choose the following options:{attr('reset')}")
        print("1. Log run")
        print("2. View log")
        print("3. Edit log")
        print("4. Remove log")
        print("5. Exit\n")
        decision = input("Enter an option (1-5): ")
        return decision

    user_decision = ""

    # Main menue loop
    while user_decision != "5":
        user_decision = main_menu()
        if user_decision == "1":
            log_run(runs_file)
        elif user_decision == "2":
            view_log(runs_file)
        elif user_decision == "3":
            edit_log(runs_file)
        elif user_decision == "4":
            remove_log(runs_file)
        elif user_decision == "5":
            continue
        else:
            # Invalid input message
            print(f"{fg('black')} {bg('red')}Invalid input. Please try again.{attr('reset')}")

    # Exit app message
    print(ascii_art)
    print(f"{fg('black')} {bg('yellow')}Thank you for using RXN. See you next time!{attr('reset')}")

if __name__ == "__main__":
    main()