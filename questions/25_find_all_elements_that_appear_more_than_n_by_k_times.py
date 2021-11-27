"""
Question - Given an array of size n, find all elements in array that appear more than n/k times.

link - https://www.geeksforgeeks.org/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/

example -
         {3, 1, 2, 2, 1, 2, 3, 3}, k= 4

        answer - [2, 3]
"""

from collections import Counter
class Solution:
    def findElements(self,arr, n, k):
        out = []
        counter = Counter(arr)
        for i,j in counter.items():
            if j > n//k:
                out.append(i)

        return out

if __name__ == "__main__":
    solution = Solution()
    arr = [3,1,2,2,1,2,3,3]
    k = 4
    print(solution.findElements(arr,len(arr),k))