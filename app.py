def calculate_total(price, quantity):
    return price * quantity

def main():
    print("=== Shopping Bill Calculator (Push 1) ===")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
        total = calculate_total(price, quantity)
        print(f"Total Bill: ${total:.2f}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
