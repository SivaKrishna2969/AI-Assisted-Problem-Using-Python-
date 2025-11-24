def fibonacci(n):
    """Return Fibonacci series up to n terms and the nth Fibonacci number."""
    series = []
    a, b = 0, 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series, series[-1]   # full series + nth number


# ---- User input section ----
try:
    n = int(input("Enter a non-negative integer (number of Fibonacci terms): "))

    if n < 0:
        print("Please enter a non-negative number!")
    elif n == 0:
        print("No terms to display.")
    else:
        series, nth_num = fibonacci(n)
        print(f"\nFibonacci series ({n} terms): {series}")
        print(f"The {n}th Fibonacci number is: {nth_num}")

except ValueError:
    print("Invalid input! Please enter an integer.")
