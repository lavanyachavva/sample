import math

def is_strong_number(num):
    """Checks if a number is a strong number."""
    if num < 0:
        return False
    
    original_num = num
    sum_of_factorials = 0
    
    # Handle the case of 0 separately as factorial of 0 is 1.
    if num == 0:
        return False # 0 is not considered a strong number in this context
        
    while num > 0:
        digit = num % 10
        sum_of_factorials += math.factorial(digit)
        num //= 10
        
    return sum_of_factorials == original_num

def print_strong_numbers_in_range(start, end):
    """Prints all strong numbers within a given range."""
    print(f"Strong numbers between {start} and {end}:")
    for i in range(start, end + 1):
        if is_strong_number(i):
            print(i)

# Call the function to print strong numbers from 1 to 5000
print_strong_numbers_in_range(1, 5000)