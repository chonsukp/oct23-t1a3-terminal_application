import csv
import os

# import tabulate

# Feature 1 - Log a run
def log_run(runs_file):
    print("Log a run")

    with open(runs_file, "a", newline="") as f:
        writer = csv.writer(f)

        # Input - title of the run
        title = input("Enter a title for the run: ")

        # Input - date of the run
        while True:
            try:
                date = input("Enter the date of the run (DD/MM/YYYY): ")

                date_parts = date.split("/")
                if len(date_parts) != 3:
                    print("Invalid date format. Please enter date in DD/MM/YYYY format.")
                    continue
        
                days, months, years = map(int, date_parts)
                if days <= 0 or days > 31 or months <= 0 or months > 12 or years <= 0:
                    print("Invalid date value. Please enter a valid date.")
                    continue

            except ValueError:
                print("Invalid input. Please enter a valid date.")
                continue

            else:
                break
        
        # Input - time of the run 
        while True:
            try:
                time = input("Enter the time of the run in 24-Hour format (HH:MM): ")
                
                time_parts = time.split(":")
                if len(time_parts) != 2:
                    print("Invalid time format. Please enter date in HH:MM format.")
                    continue

                hours, minutes = map(int, time_parts)
                if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
                    print("Invalid time value. Please enter a valid time.")
                    continue

            except ValueError:
                print("Invalid input. Please enter a valid time.")
                continue
            
            else:
                break
        
        # Input - distance of the run
        while True:
            try:
                distance = float(input("Enter the distance of the run in kilometers: "))
                if distance < 0:
                    print("Invalid distance value. Please enter a whole number only.")
                    continue

            except ValueError:
                print("Invalid input. Please enter a valid distance in number only.")
                continue
            
            else:
                break

        # Input - time taken for the run
        while True:
            try:
                time_taken = input("Enter the time taken for the run (HH:MM:SS): ")

                time_taken_parts = time_taken.split(":")
                if len(time_taken_parts) != 3:
                    print("Invalid time format. Please enter time taken in HH:MM:SS format.")
                    continue

                hours, minutes, seconds = map(int, time_taken_parts)
                if hours < 0 or minutes < 0 or seconds < 0:
                    print("Invalid time input. Please enter a whole number only.")
                    continue

            except ValueError:
                print("Invalid input. Please enter a valid time in number only.")
                continue

            else:
                break
        
        # Input - notes for the run
            
        notes = input("Enter notes for the run: ")

        writer.writerow([title, date, time, distance, time_taken, notes])

# Feature 2
# def view_log():
        # print("View runs")