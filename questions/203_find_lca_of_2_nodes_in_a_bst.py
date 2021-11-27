"""
Question - Given a Binary Search Tree (with all values unique) and two node values.
            Find the Lowest Common Ancestors of the two nodes in the BST.

link - https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1

example -
            n1 = 4, n2 = 2

                             5
                            /
                          3
                        /  \
                       2    4

        answer -  3
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


def findPath(root,k,path):
    if root is None:
        return False
    if root.data == k:
        path.append(root)
        return True
    if root.data < k:
        out = findPath(root.right,k,path)
    else:
        out = findPath(root.left,k,path)

    if out:
        path.append(root)
    return out

def LCA(root, n1, n2):
    path1, path2 = [],[]
    if findPath(root,n1,path1) and findPath(root,n2,path2):
        len1 = len(path1)
        len2 = len(path2)
        if len1 >= len2:
            for i in range(len2):
                if path2[i] in path1:
                    return path2[i]

        elif len2 > len1:
            for i in range(len1):
                if path1[i] in path2:
                    return path1[i]
    return root




if __name__ == "__main__":
    # create object of node class
    node = Node(8)
    node.insert(3)
    node.insert(10)
    node.insert(9)
    node.insert(14)
    node.insert(10)
    print(node)


    print(LCA(node,10,14).data)

