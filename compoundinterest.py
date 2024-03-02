#Calculate the compound interest for a given principal amount, interest rate, and time period
#c = p(1 + r/n)^t

def calculate_compound_interest(principal, rate, time, comp_per_year):
    # Convert the annual interest rate to decimal form
    rate = rate / 100.0

    # Calculate the compound interest
    amount = principal * (1 + rate / comp_per_year) ** (comp_per_year * time)

    # Calculate the interest earned
    interest = amount - principal

    return amount, interest

# Example usage
principal_amount = 1000  # Initial principal amount
annual_interest_rate = 5.0  # 5% annual interest rate
compounding_frequency = 4  # Quarterly compounding
investment_period = 3  # 3 years

result, earned_interest = calculate_compound_interest(principal_amount, annual_interest_rate, investment_period, compounding_frequency)

print(f"Total amount after {investment_period} years: ${result:.2f}")
print(f"Interest earned: ${earned_interest:.2f}")

