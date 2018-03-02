'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # self.min_abs = float('inf')
        list = []
        stack = []
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                list.append(node.val)
                p = node.right

        min_abs = float('inf')
        for i in range(1, len(list)):
            min_abs = min(abs(list[i]-list[i-1]), min_abs)

        return min_abs

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.right.left = TreeNode(2)
obj = Solution()
print obj.getMinimumDifference(root)
