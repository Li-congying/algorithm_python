# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder, index = 0):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        left_in_order  = []
        left_pre_order = []
        while inorder and inorder[0] != root_val:
            left_in_order.append(inorder.pop(0))
        while preorder and preorder[0] in left_in_order:
            left_pre_order.append(preorder.pop(0))

        inorder.pop(0)
        root.left = self.buildTree(left_pre_order, left_in_order, index+1)
        root.right = self.buildTree(preorder, inorder, index+1)
        return root


obj = Solution()
root = obj.buildTree([1,2,3], [2,3,1])

print root.left.right.val