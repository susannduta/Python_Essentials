def calculate_discount(price: float, discount_percent: float) -> tuple:
    """
    Calculate the final price and discount amount based on the given discount percentage.

    Parameters:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage to apply.

    Returns:
        tuple: (final_price, discount_amount)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        discount_amount = 0.0
        final_price = price

    return final_price, discount_amount


def prompt_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")


def format_currency(amount: float) -> str:
    return f"${amount:,.2f}"


def run_discount_calculator():
    print("📦 Welcome Discount Calculator 📦")

    while True:

        price = prompt_positive_float("\nEnter the original price: $")
        discount = prompt_positive_float("Enter the discount percentage: ")

        final_price, discount_applied = calculate_discount(price, discount)

        # Output
        print("\n🧾 Calculation Summary")
        print("----------------------------")
        print(f"Original Price  : {format_currency(price)}")
        print(f"Discount Applied: {format_currency(discount_applied)}")

        if discount_applied > 0:
            print(f"✅ Final Price    : {format_currency(final_price)} (after {discount:.1f}% discount)")
        else:
            print("⚠️  No discount applied (less than 20%).")
            print(f"Final Price remains: {format_currency(final_price)}")

        choice = input("\nWould you like to calculate another item? (y/n): ").strip().lower()
        if choice != 'y':
            print("\n📌 Thank you for using the Discount Calculator. Have a great day!")
            break


if __name__ == "__main__":
    run_discount_calculator()