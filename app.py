# app.py
# Study Time Tracker Program
# This program asks the user for daily study hours, handles incorrect input,
# calculates weekly estimated study time, and prints the results clearly.

print("Welcome to the Study Time Tracker!")  # Task 1: Welcome message

# Task 2: Ask the user for input
daily_hours = input("How many hours did you study today? ")

# Task 5: Error handling for non-numeric input
try:
    daily_hours = float(daily_hours)  # Task 3: Convert to number
except ValueError:
    print("Error: Please enter a valid number (example: 2.5)")
    exit()

# Extra safety: prevent negative inputs
if daily_hours < 0:
    print("Error: Hours cannot be negative.")
    exit()

# Task 3: Perform a calculation
weekly_hours = daily_hours * 7

# Task 4: Display the results clearly
print(f"\nYou studied {daily_hours} hours today.")
print(f"At this pace, you will study about {weekly_hours} hours this week!")

# End of program
