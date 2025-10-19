# Antonio Armwood
# 10/18/2025
# P3LAB CTI-110
# Branching (money float)


def calculate_change(amount_str):
# Remove dollar sign if present and convert to float
    amount = float(amount_str.replace("$", "").strip())
    
# Convert to cents
    cents = int(round(amount * 100))

    if cents == 0:
        print("No change needed.")
        return

# Define coin values
    coins = [("Dollar", 100), ("Quarter", 25), ("Dime", 10), ("Nickel", 5), ("Penny", 1)]

# Loop through coins
    for name, value in coins:
        count = cents // value
        cents %= value
        if count:
# Handle plural form
            if count == 1:
                coin_name = name
            else:
                coin_name = "Pennies" if name == "Penny" else name + "s"
            print(f"{count} {coin_name}")

# Example usage
user_input = input("Enter the amount of money as a float: ")
calculate_change(user_input)
