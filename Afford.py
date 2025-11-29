# How much car can I afford?
# Korben Bujnicki
# 2025-11-17

def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest.
    Formula: SI = (P * R * T) / 100
    """
    return (principal * rate * time) / 100

def calculate_sales_tax(vehicle_value, tax_rate):
    return vehicle_value * tax_rate
while input != 0:
    print("Welcome to How Much Car Can You Afford")
    income = int(input("Enter pre tax income: "))

    car_value = income * 0.35
    print(f"With {income:,} you can buy a ${car_value:,.0f} car!")

    down_payment = car_value * 0.20
    print(f"Your down payment should be ${down_payment:,.0f}")

    principal = car_value - down_payment
    monthly_payments = principal / 48
    print(f"Your monthly payments for a 48 month (4 year) loan will be ${monthly_payments:,.2f} ")
