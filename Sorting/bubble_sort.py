def bubble_sort(L):
    swap = False
    # Outer loop to check if sorted.
    while not swap:
        swap = True
        # Inner loop for comparisons
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

testlist = [40, 39, 12, 35, 11, 48, 30, 25, 44, 22, 28, 1, 31, 41, 13, 21, 33,
29, 3, 49, 27, 23, 20, 7, 45, 32, 36, 42, 19, 10, 26, 17, 2, 46, 6, 43, 8, 16,
34, 4, 47, 37, 38, 9, 50, 24, 15, 5, 14, 182, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

print(bubble_sort(testlist))
