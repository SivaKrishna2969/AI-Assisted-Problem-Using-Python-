def area_rectangle(x, y):
    return x * y

def area_square(x):
    return x * x

def area_circle(x):
    return 3.14 * x * x


# Dispatch dictionary
area_dispatch = {
    "rectangle": lambda x, y=0: area_rectangle(x, y),
    "square": lambda x, y=0: area_square(x),
    "circle": lambda x, y=0: area_circle(x),
}


def calculate_area(shape, x, y=0):
    shape = shape.lower()
    if shape not in area_dispatch:
        raise ValueError("Invalid shape type selected.")
    return area_dispatch[shape](x, y)


# ---------------- USER INPUT SECTION ----------------
print("Choose a shape: rectangle / square / circle")
shape = input("Enter shape: ")

x = float(input("Enter value x (length / side / radius): "))

y = 0
if shape.lower() == "rectangle":
    y = float(input("Enter value y (width): "))

# ---------------- CALL FUNCTION ----------------
try:
    result = calculate_area(shape, x, y)
    print(f"\nArea of the {shape} = {result}")
except ValueError as e:
    print("\nError:", e)
