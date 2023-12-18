from colored import fg, attr, bg
from tabulate import tabulate
from functions import log_run, view_log

runs_file = "runs.csv"

try:
    rxn_file = open(runs_file, "r")
    rxn_file.close()

except FileNotFoundError:
    rxn_file = open(runs_file, "w")
    rxn_file.write("TITLE,DATE,TIME,DISTANCE,TIME TAKEN,NOTES\n")
    rxn_file.close()

def main():

    ascii_art = """
    _____  __  _ 
    |__/ \/ |\ | 
    |  \_/\_| \|

    """
    print(ascii_art)

    # Function - Welcome Menu - Prompting user to login or register.
    def welcome_menu():
        print(f"{fg('black')}{bg('white')}Welcome to RXN! Your personal running journal.{attr('reset')}\n")
        print("Please choose the following options:")
        print("1. Log a run")
        print("2. View all runs")
        print("3. Edit a run")
        print("4. Remove a run")
        print("5. Exit\n")
        decision = input("Enter an option (1-5): ")
        return decision

    user_decision = ""

    while user_decision != "5":
        user_decision = welcome_menu()
        if (user_decision == "1"):
            log_run(runs_file)
        elif (user_decision == "2"):
            view_log(runs_file)
        elif (user_decision == "3"):
            # Edit_run(runs_file)
            print("Three")
        elif (user_decision == "4"):
            # remove_run(runs_file)
            print("Four")
        elif (user_decision == "5"):
            continue
        else:
            print("Invalid Input. Please Try Again")

    print("Thank you for using RXN!")

main()

