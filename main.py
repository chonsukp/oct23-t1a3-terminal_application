from functions import user_authenticate, user_register, user_login

ascii_art = """
_____  __  _ 
|__/ \/ |\ | 
|  \_/\_| \|

"""
print(ascii_art)

# Function - Welcome Menu - Prompting user to login or register.
def welcome_menu():
    print("Welcome to RXN! Your personal running journal.\n")
    print("Please choose the following options:")
    print("1. Login")
    print("2. Register")
    print("3. Exit\n")
    decision = input("Enter an option (1/2/3): ")
    return decision

user_decision = ""

while user_decision != "3":
    user_decision = welcome_menu()
    if (user_decision == "1"):
        user_login()
    elif (user_decision == "2"):
        user_register()
    elif (user_decision == "3"):
        continue
    else:
        print("Invalid Input. Please Try Again")

print("Thank you for using RXN!")




# def main_menu():
#     print("What would you like to do:")
#     print("1. Log a run")
#     print("2. Display logged runs")
#     print("3. Edit run")
#     print("4. Delete run")
#     print("5. Exit")