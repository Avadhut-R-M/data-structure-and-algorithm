"""
Question - Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet.
        Each packet can have a variable number of chocolates. There are M students,
        the task is to distribute chocolate packets among M students such that :
        1. Each student gets exactly one packet.
        2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.





link - https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1#

example -
        N = 8, M = 5
        A = {3, 4, 1, 9, 56, 7, 9, 12}

        answer - 6
"""

from collections import Counter

def findMinDiff(A,N,M):
        A.sort()
        mindiff = A[-1]
        i,j = 0,M-1
        while(j<N):
            if (A[j] - A[i]) < mindiff:
                mindiff = A[j] - A[i]
            i += 1
            j += 1
        return mindiff

if __name__ == "__main__":
    a1 = [11,1,13,21,3,7]

    print(findMinDiff(a1,len(a1),3))