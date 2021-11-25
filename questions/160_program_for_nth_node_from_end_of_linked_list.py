"""
Question - Given a linked list consisting of L nodes and given a number N.
            The task is to find the Nth node from the end of the linked list.

link - https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1#

example -
        N = 2
       LinkedList: 1->2->3->4->5->6->7->8->9

       answer - 8
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def getNthFromLast(head,n):
    #code here
    head1 = head
    length = 0

    while(head1):
        length += 1
        head1 = head1.next

    if length < n:
        return -1
    for i in range(length - n):
        head = head.next
    return(head.data)

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

print(getNthFromLast(a,2))