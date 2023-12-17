import csv

# Feature 1 - Log a run
def log_run(runs_file):
    with open(runs_file, "a", newline="") as f:
        writer = csv.writer(f,)

        title = input("Enter a title of the run: ")

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
            
        writer.writerow([title, date,])

       