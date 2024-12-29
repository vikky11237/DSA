def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    Time Complexity: O(n^2) in worst and average cases
    Space Complexity: O(1)
    
    Parameters:
    arr (list): List of comparable elements to be sorted
    
    Returns:
    list: Sorted list in ascending order
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize the algorithm - if no swaps occur, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        # If no swapping occurred in this pass, array is already sorted
        if not swapped:
            break
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test cases
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    
    sorted_array = bubble_sort(test_array.copy())
    print("Sorted array:", sorted_array)
    
    # Additional test cases
    test_cases = [
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [1],              # Single element
        [],               # Empty array
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]  # Random array
    ]
    
    print("\nAdditional test cases:")
    for test in test_cases:
        print(f"Original: {test}")
        print(f"Sorted: {bubble_sort(test.copy())}\n")