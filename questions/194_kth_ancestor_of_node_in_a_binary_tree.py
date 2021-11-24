"""
Question - Given a binary tree in which nodes are numbered from 1 to n.
            Given a node and a positive integer K. We have to print the Kth ancestor of the given node in the binary tree.
            If there does not exist any such ancestor then print -1.

link - https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1

example -
        n = 14 , k = 2
        tree -
                              8
                            /   \
                           3     10
                                /   \
                                9     14
                                    /
                                    10

        answer -  8
"""

# class to create node of the tree
class Node:
    # initialise class variales
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # insert new node to tree
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)

        else:
            self.data = data

    # create a string of data of all nodes to print the tree
    def _build_tree_string(self,root, curr_index ,include_index: bool = False,delimiter: str = "-",):
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if include_index:
            node_repr = "{}{}{}".format(curr_index, delimiter, root.data)
        else:
            node_repr = str(root.data)

        new_root_width = gap_size = len(node_repr)

        l_box, l_box_width, l_root_start, l_root_end = self._build_tree_string(
            root.left, 2 * curr_index + 1, include_index, delimiter
        )
        r_box, r_box_width, r_root_start, r_root_end = self._build_tree_string(
            root.right, 2 * curr_index + 2, include_index, delimiter
        )

        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(" " * (l_root + 1))
            line1.append("_" * (l_box_width - l_root))
            line2.append(" " * l_root + "/")
            line2.append(" " * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        line1.append(node_repr)
        line2.append(" " * new_root_width)

        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append("_" * r_root)
            line1.append(" " * (r_box_width - r_root + 1))
            line2.append(" " * r_root + "\\")
            line2.append(" " * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        gap = " " * gap_size
        new_box = ["".join(line1), "".join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else " " * l_box_width
            r_line = r_box[i] if i < len(r_box) else " " * r_box_width
            new_box.append(l_line + gap + r_line)

        return new_box, len(new_box[0]), new_root_start, new_root_end

    # print the string from _build_tree_string
    def __str__(self, index: bool = False, delimiter: str = "-") -> None:
        lines = self._build_tree_string(self, 0, index, delimiter)[0]
        return str("\n" + "\n".join((line.rstrip() for line in lines)))


class Solution:
    def findPath(self, root, key, path):
        if root is None:
            return False
        if root.data == key:
            path.append(root.data)
            return True

        out = self.findPath(root.left, key, path) or\
            self.findPath(root.right, key, path)

        if out:
            path.append(root.data)
        return out

    def kthancestor(self,root, value, k):
        path = []
        self.findPath(root,value,path)
        if k >= len(path):
            return -1
        else:
            return path[k]


if __name__ == "__main__":
    # create object of node class
    node = Node(8)
    node.insert(3)
    node.insert(10)
    node.insert(9)
    node.insert(14)
    node.insert(10)
    print(node)


    solution = Solution()
    print(solution.kthancestor(node, 14, 2))

