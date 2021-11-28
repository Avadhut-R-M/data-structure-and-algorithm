"""
Question - Given head, the head of a singly linked list, find if the linked list is circular or not.
        A linked list is called circular if it not NULL terminated and all nodes are connected in the form of a cycle.
        An empty linked list is considered as circular.

link - https://practice.geeksforgeeks.org/problems/circular-linked-list/1#

example -

       [1,2,3,4,5] (5 is connected to 1)

       answer - 1
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isCircular(head):
    # Code here
    temp = head
    while(temp):
        temp = temp.next
        if temp == head:
            return 1
    return 0

if __name__ == "__main__":
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = a


    print(isCircular(a))