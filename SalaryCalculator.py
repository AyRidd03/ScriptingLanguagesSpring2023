# Salary Calculator by Ayden Riddle

# Variables

DASH_LENGTH = 40  # To be used for repeating Dashes in code
COLUMN_LENGTH = 25  # To be used when setting a standard column length

# Intro Display

print('=' * DASH_LENGTH)
print("The Annual Salary Calculator")
print('=' * DASH_LENGTH)

# Inputs

salary_per_hour = float(input(f"{'Salary per Hour':.<{COLUMN_LENGTH}}"))  # Takes input from user of Salary per Hour
hours_per_week = float(input(f"{'Hours per Week':.<{COLUMN_LENGTH}}"))  # Takes input for Hours per Week
days_per_week = float(input(f"{'Days per Week':.<{COLUMN_LENGTH}}"))  # Takes input Days per Week
holidays_per_year = float(input(f"{'Holidays per Year':.<{COLUMN_LENGTH}}"))  # Takes Holidays per Year
vacations_per_year = float(input(f"{'Vacation Days per Year':.<{COLUMN_LENGTH}}"))  # Takes Vacation Days Per Year

# Calculations
