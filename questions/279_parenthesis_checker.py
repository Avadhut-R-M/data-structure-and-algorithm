"""
Question - Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
        For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.



link - https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1#

example -
        {([])}

        answer - True

"""


class Solution:
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        start = ('(', '[', '{')
        end = (')', ']', '}')
        complete = ('()', '[]', '{}')
        stack = []
        for i in x:
            if i in start:
                stack.append(i)
            if i in end:
                if len(stack):
                    start_element = stack.pop()
                    if start_element+i not in complete:
                        return False
                else:
                    return False
        if len(stack):
            return False
        return True

if __name__ == "__main__":

    expression = '((()))'
    solution = Solution()
    print(solution.ispar(expression))
