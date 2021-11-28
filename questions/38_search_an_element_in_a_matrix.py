"""
Question - Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.

link - https://leetcode.com/problems/search-a-2d-matrix/

example -
         matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

        answer - True
"""

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        for i in matrix:
            if i[0] <= target <= i[-1]:
                low = 0
                high = len(i) - 1
                mid = 0
                while low <= high:
                    mid = (high+low) // 2
                    if i[mid] == target:
                        return True
                    if i[mid] > target:
                        high = mid-1
                    if i[mid] < target:
                        low = mid +1
        return False

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(solution.searchMatrix(matrix, target))