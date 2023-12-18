import csv
import datetime
from colored import fg, attr, bg
import tabulate

# Feature 1 - Log a run
def log_run(runs_file):
    # Display feature header
    print(f"\n{fg('black')}{bg('white')}Log runs:{attr('reset')}\n")

    # Input - title of the run
    title = input("Enter a title for the run: ")

    # Input - date of the run
    while True:
        try:
            date_str = input("Enter the date of the run (DD/MM/YYYY): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date format. Please enter date in DD/MM/YYYY format.")
            continue
        else:
            break
    
    # Input - distance of the run
    while True:
        try:
            distance = float(input("Enter the distance of the run in kilometers: "))
            if distance < 0:
                print("Invalid distance value. Please enter a whole number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid distance in number only.")
            continue
        else:
            break

    # Input - time taken for the run
    while True:
        try:
            time_taken_str = input("Enter the time taken for the run (HH:MM:SS): ")
            time_taken = datetime.datetime.strptime(time_taken_str, "%H:%M:%S").time()
        except ValueError:
            print("Invalid input. Please enter a valid time in HH:MM:SS format.")
            continue
        else:
            break

    # Input - notes for the run
    notes = input("Enter notes for the run: ")

    # Append run inputs to CSV file
    with open(runs_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([title, date, distance, time_taken, notes])

# Function to convert time to seconds
def convert_time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(":"))
    return hours * 3600 + minutes * 60 + seconds

# Feature 2 - View Logs
def view_log(runs_file):
    # Display feature header
    print(f"\n{fg('black')}{bg('white')}View runs:{attr('reset')}\n")

    # Read data from CSV file
    with open(runs_file, "r") as f:
        csv_reader = csv.reader(f)
        headers = next(csv_reader)
        data = list(csv_reader)

    # Convert data to a list of lists
    data_as_lists = [list(map(str, row)) for row in data]

    # Calculate total runs, total distance, total time taken and average pace
    total_runs = len(data_as_lists)
    total_distance = sum(float(row[2]) for row in data_as_lists)

    total_time_taken_seconds = sum(convert_time_to_seconds(row[3]) for row in data_as_lists)

    total_time_hours = total_time_taken_seconds // 3600
    total_time_minutes = (total_time_taken_seconds % 3600) // 60
    total_time_seconds = total_time_taken_seconds % 60

    average_pace_seconds_per_km = total_time_taken_seconds / total_distance
    average_pace_minutes_per_km = average_pace_seconds_per_km / 60

    # Create a table using tabulate module 
    table = tabulate.tabulate(data_as_lists, headers, tablefmt='pretty')

    # Display the table and run stats
    print(table)
    print(f"\nTotal runs: {total_runs}.")
    print(f"Total distance: {total_distance} kilometers.")
    print(f"Total time: {total_time_hours} hours, {total_time_minutes} minutes, {total_time_seconds} seconds.")
    print(f"Average pace: {average_pace_minutes_per_km:.2f} minutes/kilometers.")

# Feature 3 - Edit log
def edit_log(runs_file):
    print(f"\n{fg('black')}{bg('white')}Edit runs:{attr('reset')}\n")

    # Load existing data from CSV file
    with open(runs_file, "r") as f:
        csv_reader = csv.reader(f)
        headers = next(csv_reader)
        data = list(csv_reader)

    # Convert data to a list of list
    data_as_lists = [list(map(str, row)) for row in data]

    # Display the existing logs
    table = tabulate.tabulate(data_as_lists, headers, tablefmt='pretty')
    print(table)

    # Input - ask user which log to edit
    while True:
        try:
            row_to_edit = int(input("\nEnter the row number to edit: "))
            if 0 <= row_to_edit < len(data_as_lists):
                break
            else:
                print("Invalid row number. Please enter a valid row number.")
        except ValueError:
            print("Invalid input. Please enter a valid row number.")

    # Input - ask user for new log inputs
    title = input("Enter a new title for the run: ")

    while True:
        try:
            date_str = input("Enter the new date of the run (DD/MM/YYYY): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date format. Please enter date in DD/MM/YYYY format.")
            continue
        else:
            break

    while True:
            try:
                distance = float(input("Enter the new distance of the run in kilometers: "))
                if distance < 0:
                    print("Invalid distance value. Please enter a whole number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid distance in number only.")
                continue
            else:
                break

    while True:
            try:
                time_taken_str = input("Enter the new time taken for the run (HH:MM:SS): ")
                time_taken = datetime.datetime.strptime(time_taken_str, "%H:%M:%S").time()
            except ValueError:
                print("Invalid input. Please enter a valid time in HH:MM:SS format.")
                continue
            else:
                break

    notes = input("Enter new notes for the run: ")

    # Update the selected row
    data_as_lists[row_to_edit] = [title, date, distance, time_taken, notes]

    # Save the updated data
    with open(runs_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data_as_lists)
