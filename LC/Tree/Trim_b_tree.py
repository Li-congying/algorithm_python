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
        if not root:
            return None

        while root and root.val < L:
            root = root.right
        while root and root.val > R:
            root = root.left

        if root:
            node = root
            while node.left:
                if node.left.val < L:
                    node.left = node.left.right
                node = node.left
            node = root
            while node.right:
                if node.right.val > R:
                    node.right = node.right.left
                node = node.right
        return root

        '''
        if not root: return None
        if root.val<L:
            return self.trimBST(root.right, L, R)
        if root.val>R:
            return self.trimBST(root.left, L, R)
        root.left=self.trimBST(root.left, L, R)
        root.right=self.trimBST(root.right, L, R)
        return root
        '''


'''
[18,0,40,null,2,22,49,1,17,21,32,45,null,null,null,9,null,19,null,29,37,44,47,8,13,null,20,26,30,33,39,42,null,46,48,3,null,10,16,null,null,24,27,null,31,null,35,38,null,41,43,null,null,null,null,null,4,null,12,14,null,23,25,null,28,null,null,34,36,null,null,null,null,null,null,null,7,11,null,null,15,null,null,null,null,null,null,null,null,null,null,5,null,null,null,null,null,null,6]
35
35
'''

root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)

obj = Solution()
new_root = obj.trimBST(root, 4, 4)
print new_root.val