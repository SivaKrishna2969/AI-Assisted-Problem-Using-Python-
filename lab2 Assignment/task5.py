def sum_even_and_odd(numbers):
    """
    Returns a tuple (even_sum, odd_sum) for the given iterable of integers.
    """
    even_sum = sum(x for x in numbers if x % 2 == 0)
    odd_sum = sum(x for x in numbers if x % 2 != 0)
    return even_sum, odd_sum

if _name_ == "_main_":
    nums = [1, 2, 3, 4, 5, 6]
    even, odd = sum_even_and_odd(nums)
    print("Numbers:", nums)
    print("Sum of even numbers:", even)
    print("Sum of odd numbers:", odd)
