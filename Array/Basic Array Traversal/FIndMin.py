def find_min(arr):
    if not arr:
        return None
    
    min_value = arr[0]

    for i in arr:
        if i < min_value:
            min_value = i

    return min_value

number = [99, 68, 56, 877, 24, 3]
minimum_value = find_min(number)
print(minimum_value)


# Using built in function

minimum = min(number)
print(minimum)