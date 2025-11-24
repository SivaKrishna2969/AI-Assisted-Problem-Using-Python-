def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    Repeatedly compares adjacent values and swaps them if they are in the wrong order.
    Returns the sorted list.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
    return arr


# ------------ User Inputs ------------
user_input = input("Enter list elements separated by space: ")
arr = list(map(int, user_input.split()))

# ------------ Call Bubble Sort Function ------------
sorted_arr = bubble_sort(arr)

# ------------ Output ------------
print("Sorted list is:", sorted_arr)
