def calculate_average(numbers):

    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(calculate_average([5, 10, 15, 20]))  
print(calculate_average([]))              