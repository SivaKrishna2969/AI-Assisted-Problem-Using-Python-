def student_discount(price):
    return price * (0.90 if price > 1000 else 0.95)

def regular_discount(price):
    return price * (0.85 if price > 2000 else 1.00)

def discount(price, category):
    if category == "student":
        return student_discount(price)
    return regular_discount(price)


# ---- INPUT FUNCTIONS ----

def main():
    try:
        price = float(input("Enter the price: "))
    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    category = input("Enter category (student / regular): ").strip().lower()

    final_price = discount(price, category)
    print(f"Discounted price: {final_price}")

# Run the program
main()
