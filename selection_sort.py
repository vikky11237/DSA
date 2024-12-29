def selection_sort(arr):
    temp = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr      

# Test cases
if __name__ == "__main__":
    # Basic test case
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    print("Sorted array:", selection_sort(test_array.copy()))

    # Additional test cases
    test_cases = [
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [1],              # Single element
        [],               # Empty array
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],  # Random array with duplicates
        [10, 10, 10, 10], # All elements same
        [-5, 0, -3, 2, -1, 10, -8],  # Array with negative numbers
        [100, 0, 0.5, -100, 50, -50],  # Array with mixed positive/negative and decimal
        [999, 1000, 998, 997, 996, 995]  # Large numbers
    ]
    
    print("\nAdditional test cases:")
    for test in test_cases:
        print(f"Original: {test}")
        print(f"Sorted: {selection_sort(test.copy())}\n")
