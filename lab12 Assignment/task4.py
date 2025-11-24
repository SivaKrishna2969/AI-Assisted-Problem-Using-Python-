def f(x):
    return 2 * (x ** 3) + 4 * x + 5

# ----- User inputs -----
start = float(input("Enter start of interval: "))
end = float(input("Enter end of interval: "))
step = float(input("Enter step size (e.g., 0.01): "))

# ----- Search for minimum value -----
x = start
min_x = x
min_val = f(x)

while x <= end:
    fx = f(x)
    if fx < min_val:
        min_val = fx
        min_x = x
    x += step

print("\nWithin the given interval:")
print(f"Minimum f(x) = {min_val} occurs at x = {min_x}")
