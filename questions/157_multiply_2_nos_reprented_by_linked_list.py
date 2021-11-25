"""
Question - Given elements as nodes of the two linked lists.
The task is to multiply these two linked lists, say L1 and L2.

link - https://practice.geeksforgeeks.org/problems/multiply-two-linked-lists/1#

example -

       LinkedList1: 3 -> 2
       LinkedList2: 2

       answer - 64
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def multiplyTwoList(head1, head2):
    # Code here
    num1,num2 = [],[]
    while head1:
        num1.append(str(head1.data))
        head1 = head1.next

    while head2:
        num2.append(str(head2.data))
        head2 = head2.next

    num1 = int(''.join(num1))
    num2 = int(''.join(num2))

    return (num1*num2)%(10**9 + 7)

if __name__ == "__main__":
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(2)

    print(multiplyTwoList(a,b))