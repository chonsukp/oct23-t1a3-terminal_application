import csv
import datetime

from colored import fg, attr, bg
import tabulate

# Feature 1 - Log a run
def log_run(runs_file):
    print(f"\n{fg('black')}{bg('white')}Log runs:{attr('reset')}\n")

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

# Function to convert...
def convert_time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(":"))
    return hours * 3600 + minutes * 60 + seconds

# Feature 2 - View Logs
def view_log(runs_file):
        print(f"\n{fg('black')}{bg('white')}View runs:{attr('reset')}\n")

        with open(runs_file, "r") as f:
            csv_reader = csv.reader(f)
            headers = next(csv_reader)
            data = list(csv_reader)
        
        data_as_lists = [list(map(str, row)) for row in data]

        total_runs = len(data_as_lists)
        total_distance = sum(float(row[3]) for row in data_as_lists)
   
        total_time_taken_seconds = sum(convert_time_to_seconds(row[4]) for row in data_as_lists)

        total_time_hours = total_time_taken_seconds // 3600
        total_time_minutes = (total_time_taken_seconds % 3600) // 60
        total_time_seconds = total_time_taken_seconds % 60

        average_pace_seconds_per_km = total_time_taken_seconds / total_distance
        average_pace_minutes_per_km = average_pace_seconds_per_km / 60

        table = tabulate.tabulate(data_as_lists, headers, tablefmt='pretty')

        print(table)
        print(f"\nTotal runs: {total_runs}.")
        print(f"Total distance: {total_distance} kilometers.")
        print(f"Total time: {total_time_hours} hours, {total_time_minutes} minutes, {total_time_seconds} seconds.")
        print(f"Average pace: {average_pace_minutes_per_km:.2f} minutes/kilometers.\n")



       



