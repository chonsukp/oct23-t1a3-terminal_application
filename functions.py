import csv

# Feature 1 - Log a run
def log_run(runs_file):
    with open(runs_file, "a", newline="") as f:
        writer = csv.writer(f,)

        # Input - title of the run
        title = input("Enter a title of the run: ")

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
                    print("Invalid time value. Please enter a valid time")
                    continue

            except ValueError:
                print("Invalid input. Please enter a valid time.")
                continue
            
            else:
                break

        writer.writerow([title, date, time])

       