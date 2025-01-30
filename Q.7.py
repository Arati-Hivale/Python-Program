import random

# Generate a list of numbers from 0 to 100 with a step of 2
num_list = list(range(0, 101, 2))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        print(f"Checking middle value: {mid_value}")  # Debugging statement

        if mid_value == target:
            return mid  # Found the target
        elif mid_value < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found

# Ask user for a number between 0 and 100
try:
    user_num = int(input("Enter a number between 0 and 100: "))

    if user_num % 2 != 0 or user_num < 0 or user_num > 100:
        print("Invalid input! Please enter an even number between 0 and 100.")
    else:
        result = binary_search(num_list, user_num)

        if result != -1:
            print(f"Number {user_num} found at index {result}.")
        else:
            print(f"Number {user_num} is not in the list.")

except ValueError:
    print("Please enter a valid number.")
