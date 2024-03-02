#Given a list of integers, find the sum of all positive numbers

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

sum_of_positive = 0

for num in numbers:
    if num > 0:
        sum_of_positive += num

print("Sum of the positive number:" , sum_of_positive)
