# Write a program that converts a given number of days into years and weeks

def convert_days_to_years_weeks_days(days):
    years = days // 365
    weeks = (days % 365) // 7
    remaining_days = (days % 365) % 7
    return years, weeks, remaining_days

# Example usage
days = 1000  # Replace with the number of days you want to convert

years, weeks, remaining_days = convert_days_to_years_weeks_days(days)

print(f"{days} days is approximately {years} years, {weeks} weeks, and {remaining_days} days.")
