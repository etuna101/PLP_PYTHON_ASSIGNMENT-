def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Main program
def main():
    try:
        # Prompt user for input
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate final price
        final_price = calculate_discount(price, discount_percent)

        # Display results
        if discount_percent >= 20:
            print(f"Discount applied! Final price: ksh{final_price:.2f}")
        else:
            print(f"No discount applied. Price remains: Ksh{final_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount.")


# Run the program
if __name__ == "__main__":
    main()
