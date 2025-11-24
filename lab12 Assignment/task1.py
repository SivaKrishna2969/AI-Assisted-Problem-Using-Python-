def linear_search(data_list, target):
    """
    Performs linear search to find the index of the target value.
    Returns the index if found, otherwise returns -1.
    """
    for index in range(len(data_list)):
        if data_list[index] == target:
            return index
    return -1


# ------ User Inputs --------
# Taking list elements from user
user_input = input("Enter list elements separated by space: ")
data_list = list(map(int, user_input.split()))

# Value to search
target = int(input("Enter value to search: "))

# ------ Call Function -------
result = linear_search(data_list, target)

# ------ Output -------
if result != -1:
    print(f"Value {target} found at index {result}.")
else:
    print(f"Value {target} not found in the list.")
