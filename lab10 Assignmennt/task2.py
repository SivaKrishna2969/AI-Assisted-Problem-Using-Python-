def find_common():
    a_input = input("Enter numbers for list A (comma-separated): ")
    b_input = input("Enter numbers for list B (comma-separated): ")

    # Convert to integer lists
    try:
        a = [int(x) for x in a_input.split(",")]
        b = [int(x) for x in b_input.split(",")]
    except ValueError:
        print("Error: Please enter only numbers separated by commas.")
        return []

    # Find common values
    common = [num for num in a if num in b]

    return common


result = find_common()
print("Common elements:", result)
