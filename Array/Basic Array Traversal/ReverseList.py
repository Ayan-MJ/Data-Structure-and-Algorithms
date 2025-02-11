def reverse_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = [8, 7, 40, 65, 3, 9]
reverse_in_place(arr)
print(arr)