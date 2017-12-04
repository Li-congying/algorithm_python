# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder ):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return None
        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        index = 0
        while index < len(inorder):
            if inorder[index] == root_val:
                break
            index += 1

        root.left = self.buildTree(preorder[:index], inorder[:index] )
        root.right = self.buildTree(preorder[index:], inorder[index+1:])
        return root

class Solution2(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        mi_idx = {n: i for i, n in enumerate(inorder)}
        return self.buildTreeWithDict(preorder, inorder, 0, len(preorder), 0, len(inorder), mi_idx)

    def buildTreeWithDict(self, preorder, inorder, p_start, p_end, i_start, i_end, mi_idx):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # print(p_start, p_end, i_start, i_end)
        if p_start >= len(preorder) or p_start == p_end:
            return None
        root = TreeNode(preorder[p_start])
        len_left = mi_idx[preorder[p_start]] - i_start
        root.left = self.buildTreeWithDict(preorder, inorder, p_start + 1, p_start + 1 + len_left, i_start,
                                           i_start + len_left, mi_idx)
        root.right = self.buildTreeWithDict(preorder, inorder, p_start + 1 + len_left, p_end,
                                            i_start + len_left + 1, i_end, mi_idx)
        # print(root.val, root.left, root.right)
        return root


obj = Solution()
root = obj.buildTree([1,2,4,3,5,6], [2,4,1,5,3,6])

print root.left.right.val