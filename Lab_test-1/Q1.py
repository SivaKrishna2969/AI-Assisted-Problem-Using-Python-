def fibonacci(n):
    """
    Returns the n-th Fibonacci number and prints the full Fibonacci series up to n.
    Only accepts non-negative integers.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Generating the Fibonacci series
    series = []
    a, b = 0, 1
    for i in range(n + 1):
        series.append(a)
        a, b = b, a + b

    return series[-1], series  # (nth number, full series)


# ---------- User Input Section ----------
try:
    user_input = int(input("Enter a non-negative integer (n): "))
    nth_number, fib_series = fibonacci(user_input)

    print(f"\nThe Fibonacci series up to n = {user_input}:")
    print(fib_series)

    print(f"\nThe {user_input}th Fibonacci number is: {nth_number}")

except ValueError:
    print("Error: Please enter a valid non-negative integer.")
except TypeError:
    print("Error: Input must be an integer.")
