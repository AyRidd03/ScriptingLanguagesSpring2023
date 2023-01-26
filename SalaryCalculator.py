# Salary Calculator by Ayden Riddle

# Variables

DASH_LENGTH = 40  # To be used for repeating Dashes in code
COLUMN_LENGTH = 25  # To be used when setting a standard column length
WEEKS_PER_YEAR = 52

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

unadjusted_salary = salary_per_hour * hours_per_week * days_per_week * WEEKS_PER_YEAR  # Calculates unadjusted Salary

adjusted_days_per_year = days_per_week * WEEKS_PER_YEAR - holidays_per_year - vacations_per_year  # Calculates Days
adjusted_salary = salary_per_hour * hours_per_week * adjusted_days_per_year  # Calculates adjusted Salary

# End Display

print('=' * DASH_LENGTH)
print(f"{'Unadjusted Salary':.<{COLUMN_LENGTH}}: ${unadjusted_salary:6,.2f}")
print(f"{'Adjusted Salary':.<{COLUMN_LENGTH}}: ${adjusted_salary:6,.2f}")
print('=' * DASH_LENGTH)
print("Thank You For Using Annual Salary Calculations,")
print("Have a Nice Day!")
