"""
Question - Given an integer N, find its factorial.
        Return as list of integers of numbers of factorial



link - https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1#

example -
        5

        answer - [1,2,0]
"""

class Solution:
    def factorialUtil(self, N):
        if N in [0,1]:
            return 1
        #code here
        return N * self.factorialUtil(N-1)

    def factorial(self, N):
        fact = self.factorialUtil(N)
        return [int(i) for i in str(fact)]

if __name__ == "__main__":
    solution = Solution()
    print(solution.factorial(5))