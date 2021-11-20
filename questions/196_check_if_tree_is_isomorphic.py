"""
Question - Given two Binary Trees. Check whether they are Isomorphic or not.
link - https://practice.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1
example -
        tree -              T1    1     T2:    1
                                /  \         /   \
                              2    3        3     2
                             /                     \
                            4                       4

        answer -  True
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
    def isIsomorphic(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.data != root2.data:
            return False

        return(
            (self.isIsomorphic(root1.left, root2.left) and
            self.isIsomorphic(root1.right, root2.right)) or
            (self.isIsomorphic(root1.left, root2.right) and
            self.isIsomorphic(root1.right, root2.left))
        )


if __name__ == "__main__":
    # create object of node class
    node1 = Node(8)
    node1.insert(3)
    node1.insert(10)
    node1.insert(9)
    node1.insert(14)

    node2 = Node(8)
    node2.insert(3)
    node2.insert(10)
    node2.insert(9)
    node2.insert(14)

    print(node1)
    print(node2)

    solution = Solution()
    print(solution.isIsomorphic(node1, node2))

