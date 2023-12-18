from functions import log_run, view_log, edit_log, remove_log
import csv
from colored import fg, attr, bg

runs_file = "runs.csv"

try:
    rxn_file = open(runs_file, "r")
    rxn_file.close()
except FileNotFoundError:
    rxn_file = open(runs_file, "w")
    rxn_file.write("TITLE,DATE,DISTANCE,TIME TAKEN,NOTES\n")
    rxn_file.close()

def main():

    ascii_art = """
 _______     ____  ____  ____  _____  
|_   __ \   |_  _||_  _||_   \|_   _| 
  | |__) |    \ \  / /    |   \ | |   
  |  __ /      > `' <     | |\ \| |   
 _| |  \ \_  _/ /'`\ \_  _| |_\   |_  
|____| |___||____||____||_____|\____| 
    """
    print(ascii_art)
    print(f"{fg('black')}{bg('white')}Welcome to RXN! Your personal running journal.{attr('reset')}")

    # Function - output options - instructions
    def main_menu():
        print("\nPlease choose the following options:")
        print("1. Log run")
        print("2. View log")
        print("3. Edit log")
        print("4. Remove log")
        print("5. Exit\n")
        decision = input("Enter an option (1-5): ")
        return decision

    user_decision = ""

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
            print(f"{fg('black')}{bg('red')}Invalid input. Please try again.{attr('reset')}")

    print("Thank you for using RXN!")

main()
