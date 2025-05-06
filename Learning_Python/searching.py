#Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1

print("Linear Search on ([1,2,3,4,5,6,7,8,9], 5)")
print(f"Output: {linear_search([1,2,3,4,5,6,7,8,9], 5)}")


#Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return -1

print("Binary Search on (list(range(0, 10000000)), 9867)")
print(f"Output: {binary_search(list(range(0, 10000000)), 9867)}")