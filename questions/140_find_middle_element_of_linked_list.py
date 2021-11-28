"""
Question - Given the head of a singly linked list, return the middle node of the linked list.
        If there are two middle nodes, return the second middle node.

link - https://leetcode.com/problems/middle-of-the-linked-list/

example -

       [1,2,3,4,5]

       answer - node(3)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def middleNode(self, head):
        length = 0
        temp = head
        while(temp):
            length += 1
            temp = temp.next
            n = length//2

        while(n):
            head = head.next
            n -= 1
        return head

if __name__ == "__main__":
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)


    solution = Solution()
    print(solution.middleNode(a).data)