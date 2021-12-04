"""
Question - Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is
            followed by negative and vice-versa maintaining the order of appearance.

link - https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/

example -
        {1, 2, 3, -4, -1, 4}

        answer - {-4, 1, -1, 2, 3, 4}
"""

def rearrangeArray(arr):
    arr.sort()
    pos, neg = 0,0
    while(arr[pos]<0):
        pos += 1
    while(pos < len(arr) and arr[neg] < 0):
        arr[pos], arr[neg] = arr[neg], arr[pos]
        pos += 1
        neg += 2
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, -4, -1, 4]
    print(rearrangeArray(arr))