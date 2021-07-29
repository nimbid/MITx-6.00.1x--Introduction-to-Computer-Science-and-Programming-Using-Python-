def selection_sort(L):
  suffixSt = 0 # Suffix store. Marks end of sorted part.
  while suffixSt != len(L): # Run loop until sorted part length equals original length.
      for i in range(suffixSt, len(L)):
          if L[i] < L[suffixSt]:
              L[suffixSt], L[i] = L[i], L[suffixSt]
      suffixSt += 1
  return L

testlist = [40, 39, 12, 35, 11, 48, 30, 25, 44, 22, 28, 1, 31, 41, 13, 21, 33,
29, 3, 49, 27, 23, 20, 7, 45, 32, 36, 42, 19, 10, 26, 17, 2, 46, 6, 43, 8, 16,
34, 4, 47, 37, 38, 9, 50, 24, 15, 5, 14, 182, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

print(selection_sort(testlist))
