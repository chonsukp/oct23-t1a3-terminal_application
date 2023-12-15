import csv
import os
import getpass

ascii_art = """
            _____  __  _ 
            |__/ \/ |\ | TM
            |  \_/\_| \|

"""
def welcome():
    print(ascii_art)

# Function - Main Menu
def main_menu():
    print("Welcome to RXN! Your personal running journal.\n")
    print(ascii_art)
    print("Please choose the following options:\n")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

