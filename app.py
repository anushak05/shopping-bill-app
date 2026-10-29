def calculate_total(price, quantity, discount_pct=0):
    subtotal = price * quantity
    discount_amount = subtotal * (discount_pct / 100)
    return subtotal - discount_amount

def main():
    print("=== Shopping Bill Calculator (Push 2 - With Discount) ===")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
        discount = float(input("Enter discount percentage (0 if none): "))
        total = calculate_total(price, quantity, discount)
        print(f"Final Bill after discount: ${total:.2f}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()