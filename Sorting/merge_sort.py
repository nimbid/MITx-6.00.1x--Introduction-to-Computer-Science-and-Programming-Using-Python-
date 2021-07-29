def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

testlist = [40, 39, 12, 35, 11, 48, 30, 25, 44, 22, 28, 1, 31, 41, 13, 21, 33,
29, 3, 49, 27, 23, 20, 7, 45, 32, 36, 42, 19, 10, 26, 17, 2, 46, 6, 43, 8, 16,
34, 4, 47, 37, 38, 9, 50, 24, 15, 5, 14, 182, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

print(merge_sort(testlist))
