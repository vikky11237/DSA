def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right =[x for x in arr[1:] if x >=pivot]
    return quick_sort(left)+[pivot] +quick_sort(right)

# Test cases
if __name__ == "__main__":
    # Basic test case
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    print("Sorted array:", quick_sort(test_array.copy()))

    # Additional test cases
    test_cases = [
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [1],              # Single element
        [],               # Empty array
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],  # Random array with duplicates
        [10, 10, 10, 10], # All elements same
        [-5, 0, -3, 2, -1, 10, -8]  # Array with negative numbers
    ]
    
    print("\nAdditional test cases:")
    for test in test_cases:
        print(f"Original: {test}")
        print(f"Sorted: {quick_sort(test.copy())}\n")