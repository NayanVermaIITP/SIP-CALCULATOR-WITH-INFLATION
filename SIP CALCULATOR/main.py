# SIP Calculator


def get_number(question, default=None):
    while True:
        answer = input(question).strip().replace(",", "")

        if answer == "" and default is not None:
            return default

        
        number = float(answer)
       

        if number < 0:
            print("Please enter zero or a positive number.")
        else:
            return number


def main():
    print("SIP Calculator")
    print("Press Enter to use the default return and inflation rates.\n")

    monthly_amount = get_number("Monthly SIP amount (₹): ")
    years = get_number("Investment period in years: ")
    return_rate = get_number("Expected yearly return % [12]: ", 12)
    inflation_rate = get_number("Expected yearly inflation % [7]: ", 7)

    months = int(years * 12)
    monthly_return = return_rate / 100 / 12
    monthly_inflation = inflation_rate / 100 / 12
    invested = monthly_amount * months

    if monthly_return == 0:
        future_value = invested
    else:
        future_value = monthly_amount * (
            ((1 + monthly_return) ** months - 1) / monthly_return
        ) * (1 + monthly_return)

    # Convert the future amount to its estimated value in today's money.
    today_value = future_value / ((1 + monthly_inflation) ** months)
    profit = future_value - invested

    print("\nSIP Estimate")
    print(f"Total invested:                     ₹{invested:,.2f}")
    print(f"Estimated value after {years:g} years:   ₹{future_value:,.2f}")
    print(f"Estimated returns:                  ₹{profit:,.2f}")
    print(f"Estimated value in today's money:   ₹{today_value:,.2f}")
    print(f"Return used: {return_rate:g}% per year | Inflation used: {inflation_rate:g}% per year")
    print("These are estimates; actual returns and inflation can vary.")


if __name__ == "__main__":
    main()
