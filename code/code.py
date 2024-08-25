import random

def average(arr):

    # Sort the list in ascending order
    sorted_numbers = sorted(arr)

    print("Sorted list:", sorted_numbers)

    # Calculate the sum of the numbers in the list
    total_sum = sum(sorted_numbers)

    print("Sum of numbers:", total_sum)

    # Find the average of the numbers
    average = total_sum / len(sorted_numbers)
    return(average)