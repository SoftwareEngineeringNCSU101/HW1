import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Original list:" random_numbers)

# Sort the list in ascending order
sorted_numbers = sorted(random_numbers)

print("Sorted list:", sorted_numbers)

# Calculate the sum of the numbers in the list
total_sum = sum(sorted_numbers)

print("Sum of numbers:", total_sum)

# Find the average of the numbers
average = total_sum / len(sorted_numbers)
print("Average:", average)