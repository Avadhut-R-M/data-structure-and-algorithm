"""
Question - You are given a string S, the task is to reverse the string using stack.

link - https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1

example -
        "GeeksforGeeks"

        answer - skeeGrofskeeG

"""

def reverse(S):
    stack = []
    for i in S:
        stack.insert(0,i)
    return ''.join(stack)

if __name__ == "__main__":
    string = 'skeeGrofskeeG'
    print(reverse(string))