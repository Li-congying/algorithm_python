'''
Given a binary search tree and the lowest and highest boundaries as L and R, 
trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree,
so the result should return the new root of the trimmed binary search tree.
Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        node = root
        while node.left and node.left.val >= L:
            node = node.left
        node.left = None
        node = root
        while node.right and node.right <= R:
            node = node.right
        node.right = None

        while root and root.val < L:
            if root.right:
                root = root.right

        while root and root.val > R:
            if root.left:
                root = root.left

        return root


obj = Solution()

root = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.right = TreeNode(4)

root = obj.trimBST(root, 3, 4)
print root , root.val, root.left


