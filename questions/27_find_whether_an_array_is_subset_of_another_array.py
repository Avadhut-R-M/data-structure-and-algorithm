"""
Question - Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m.
            Task is to check whether a2[] is a subset of a1[] or not.
            Both the arrays can be sorted or unsorted.
            It may be assumed that elements in both array are distinct.



link - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1#

example -
        a1[] = {11, 1, 13, 21, 3, 7}
        a2[] = {11, 3, 7, 1}

        answer - Yes
"""

from collections import Counter

def isSubset( a1, a2, n, m):
    a1_counter = Counter(a1)
    a2_counter = Counter(a2)


    for i in a2:
        if i not in a1_counter or a1_counter[i] == 0:
            return 'No'
        a1_counter[i] -= 1

    return 'Yes'

if __name__ == "__main__":
    a1 = [11,1,13,21,3,7]
    a2 = [11, 3, 7, 1]

    print(isSubset(a1,a2,len(a1), len(a2)))