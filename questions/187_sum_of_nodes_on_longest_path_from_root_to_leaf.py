"""
Question - Given a binary tree of size N. Your task is to complete the function sumOfLongRootToLeafPath(),
            that find the sum of all nodes on the longest path from root to leaf node.
            If two or more paths compete for the longest path, then the path having maximum sum of nodes is being considered.

link - https://practice.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1#

example -
        tree -              4
                           / \
                          2   5
                         / \ / \
                        7  1 2  3
                       /
                      6

        answer -  13
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
    def sumOfLongRootToLeafPathUtil(self, root, length, total_sum,max_length, max_sum):
        if root is None:
            if length > max_length[0]:
                max_length[0] = length
                max_sum[0] = total_sum
            elif length == max_length[0] and total_sum > max_sum[0]:
                max_sum[0] = total_sum
            return
        print(root.data,length, total_sum,max_length, max_sum)
        self.sumOfLongRootToLeafPathUtil(root.left,length+1, total_sum+root.data, max_length, max_sum)
        self.sumOfLongRootToLeafPathUtil(root.right,length+1, total_sum+root.data, max_length, max_sum)

    def sumOfLongRootToLeafPath(self,root):
        max_sum, max_length = [], []
        max_sum.append(-9999999)
        max_length.append(0)
        self.sumOfLongRootToLeafPathUtil(root,0,0,max_length,max_sum)
        return max_sum[0]


if __name__ == "__main__":
    # create object of node class
    node = Node(8)
    node.insert(3)
    node.insert(10)
    node.insert(9)
    node.insert(14)
    print(node)


    solution = Solution()
    print(solution.sumOfLongRootToLeafPath(node))

