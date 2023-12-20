import csv

from colored import fg, attr, bg

from functions import edit_log, log_run, remove_log, view_log

runs_file = "runs.csv"

# Check if CSV file exist and if not create one
try:
    with open(runs_file, "r"):
        pass
except FileNotFoundError:
    with open(runs_file, "w") as rxn_file:
        rxn_file.write("TITLE,DATE,DISTANCE,TIME TAKEN,NOTES\n")

def main():
    """Main function to run the RXN application"""
    ascii_art = """
 _______     ____  ____  ____  _____  
|_   __ \   |_  _||_  _||_   \|_   _| 
  | |__) |    \ \  / /    |   \ | |   
  |  __ /      > `' <     | |\ \| |   
 _| |  \ \_  _/ /'`\ \_  _| |_\   |_  
|____| |___||____||____||_____|\____|
    """
    
    # Welcome message and app logo
    print(ascii_art)
    print(f"\n{fg('black')}{bg('yellow')}Welcome to RXN! Your personal running journal.{attr('reset')}")

    def main_menu():
        """Display the main menu instructions to get user input"""
        print(f"\n{fg('black')} {bg('white')}Please choose the following options:{attr('reset')}")
        print("1. Log run")
        print("2. View log")
        print("3. Edit log")
        print("4. Remove log")
        print("5. Exit\n")
        decision = input("Enter an option (1-5): ")
        return decision

    user_decision = ""

    # Main menu loop
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
            print(f"{fg('black')} {bg('red')}Invalid input. Please try again.{attr('reset')}")

    # Exit app message
    print(ascii_art)
    print(f"{fg('black')} {bg('yellow')}Thank you for using RXN. See you next time!{attr('reset')}")

if __name__ == "__main__":
    main()