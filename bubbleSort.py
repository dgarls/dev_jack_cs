"""
Bubble sort functions by repeating through a list and checking if the element in front is smaller
than the element behind it and swapping if true.
"""

def bubbleSort(n):
    for i in range(len(n)):
        swapped = False
        for j in range(len(n) - 1):
            if n[j + 1] < n[j]:
                n[j + 1], n[j] = n[j], n[j + 1]
                swapped = True
        if swapped == False:
            break
    
    return n


toSort = [5, 8, 4, 6, 9, 1, 3, 2, 7]

print(bubbleSort(toSort))