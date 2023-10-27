# Generate a random dataset of 30 numbers (you can replace this with your own dataset)
import random

dataset = [random.randint(1, 100) for _ in range(30)]

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in this pass, the array is already sorted
        if not swapped:
            break

# Sort the dataset using Bubble Sort
bubble_sort(dataset)

# Display the original and sorted datasets
print("Original Dataset:", dataset)