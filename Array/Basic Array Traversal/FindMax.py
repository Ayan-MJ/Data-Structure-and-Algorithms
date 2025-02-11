# Find the maximum Element in an Array.

# Using simple loop

def find_max(arr):
    if not arr:
    # if the list is empty
        return None
    # Assuming the first element of the list is the largest element
    max_value = arr[0]

    for i in arr:
        if i > max_value:
            max_value = i
    return max_value

number = [2, 0, 7, 8, 7, 9]
maximum_value = find_max(number)
print(maximum_value)

# Using built in function

# maximum = max(number)
# print(max)

 