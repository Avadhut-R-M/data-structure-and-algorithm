"""
Question - Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1

link - https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/

example -
         s1 = ABCD and s2 = CDAB

        answer - True
"""

def isSame(string1, string2):
    if len(string2) != len(string1):
        return False
    string1 = string1 + string1
    return True if (string1.count(string2)) else False

if __name__ == "__main__":
    string1 = 'abcd'
    string2 = 'cdba'
    print(isSame(string1, string2))