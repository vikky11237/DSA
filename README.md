# Data Structures and Algorithms Practice

This repository contains implementations of various data structures and algorithms in Python.

## Contents

1. Sorting Algorithms
   - Bubble Sort (`bubble_sort.py`): A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
   - Quick Sort (`quick_sort.py`): A divide-and-conquer algorithm that picks an element as pivot and partitions the array around the picked pivot.
   - Selection Sort (`selection_sort.py`): A simple sorting algorithm that repeatedly finds the minimum element from unsorted portion and puts it at the beginning.
   - Insertion Sort (`insertion_sort.py`): Builds final sorted array one item at a time by repeatedly inserting a selected element into its correct position.

## Time Complexities

| Algorithm       | Best Case | Average Case | Worst Case | Space Complexity |
|----------------|-----------|--------------|------------|------------------|
| Bubble Sort    | O(n)      | O(n²)        | O(n²)      | O(1)            |
| Quick Sort     | O(n log n)| O(n log n)   | O(n²)      | O(log n)        |
| Selection Sort | O(n²)     | O(n²)        | O(n²)      | O(1)            |
| Insertion Sort | O(n)      | O(n²)        | O(n²)      | O(1)            |

## How to Run

Each algorithm is contained in its own Python file. To run any algorithm, simply use Python:

```bash
python <filename>.py
