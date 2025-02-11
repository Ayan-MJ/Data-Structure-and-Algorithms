def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

numbers = [9, 8, 52, 25, 1]
total = sum_of_array(numbers)
print(total)

# Time Complexity: You cannot do better than O(n) in the worst case because you must examine every element at least once to include it in the sum.
# Space Complexity: The iterative approach only requires one additional integer variable (total), which is constant extra space, O(1).