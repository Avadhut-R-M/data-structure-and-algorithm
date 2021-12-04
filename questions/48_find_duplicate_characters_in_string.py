"""
Question - Write an efficient program to print all the duplicates and their counts in the input string

link - https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

example -
        geeksforgeeks

        answer - [g,e,k,s]
"""

def duplicates(string):
    visited = {}
    out = []
    for i in string:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1
    for i in visited:
        if visited[i] > 1:
            out.append(i)
    return out

if __name__ == "__main__":
    string = 'skeeGrofskeeG'
    print(duplicates(string))