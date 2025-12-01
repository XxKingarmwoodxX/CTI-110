## Antonio Armwood
# 11/27/25
# P5LAB
# disperse change

import random

def coin_output(count, singular, plural=None):
    """Return properly formatted coin string with singular/plural, handling irregular plurals."""
    if count == 0:
        return None
    # If no explicit plural provided, default to singular + 's'
    word = singular if count == 1 else (plural or singular + "s")
    return f"{count} {word}"

def disperse_change(change):
    """Takes a float value (change owed) and prints the breakdown into coins."""
    cents = round(change * 100)  # convert to cents to avoid floating-point issues

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print("\n")

    for count, singular, plural in [
        (dollars, "Dollar", "Dollars"),
        (quarters, "Quarter", "Quarters"),
        (dimes, "Dime", "Dimes"),
        (nickels, "Nickel", "Nickels"),
        (pennies, "Penny", "Pennies"),  # irregular plural handled here
    ]:
        result = coin_output(count, singular, plural)
        if result:
            print(result)

def main():
    # Generate a random float between 1 and 100 for the total owed
    amount_owed = round(random.uniform(1, 100), 2)
    print(f"You owed: ${amount_owed}")

    # Prompt user for payment
    amount_paid = float(input("How much cash will you put into the self-checkout: $"))

    # Calculate change
    if amount_paid < amount_owed:
        print("Insufficient payment. Transaction canceled.")
    else:
        change = amount_paid - amount_owed
        print(f"Change is: ${change:.2f}")
        # Call disperse_change with the change owed
        disperse_change(change)

# Run the program
main()
