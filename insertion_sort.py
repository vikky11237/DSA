import array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Test cases
if __name__ == "__main__":
    # Test case to demonstrate why j -= 1 is necessary
    print("Demonstrating why j -= 1 is necessary:")
    special_case = [5, 2, 9, 1, 7]
    print("Original array:", special_case)
    print("Step by step insertion sort:")
    
    # Manual step-by-step execution
    arr = special_case.copy()
    print("\nStarting array:", arr)
    
    # First pass (i=1): inserting 2
    print("\nPass 1 - inserting 2:")
    print("Before:", arr)
    i = 1
    key = arr[i]  # key = 2
    j = i-1       # j = 0
    print(f"key = {key}, comparing with arr[{j}] = {arr[j]}")
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1  # Corrected to j -= 1
        print(f"After shift: {arr}, j is now {j}")
    arr[j+1] = key
    print("Final array after pass 1:", arr)
    
    # Regular test cases
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("\nRegular test cases:")
    print("Original array:", test_array)
    print("Sorted array:", insertion_sort(test_array.copy()))

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
        [999, 1000, 998, 997, 996, 995],  # Large numbers
        [0.1, 0.2, 0.01, 0.001, 0.0001]  # Small decimal numbers
    ]
    
    print("\nAdditional test cases:")
    for test in test_cases:
        print(f"Original: {test}")
        print(f"Sorted: {insertion_sort(test.copy())}\n")