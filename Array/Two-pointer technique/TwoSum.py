def sum_of_two(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]    
    
        if current_sum == target:
            return (left, right) # or return (arr[left], arr[right]) if you only want the values
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

arr = [2, 7, 11, 15]
target = 9
result = sum_of_two(arr, target)
print(result)