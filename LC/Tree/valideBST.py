class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):

    def buildTree(self, list, i):
        if not list or i >= len(list):
            return None
        root = TreeNode(list[i])
        root.left = self.buildTree(list, 2*i + 1)
        root.right = self.buildTree(list, 2*i + 2)
        return root

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.orders = []
        def innerOrder(root):
            if root.left:
                innerOrder(root.left)
            self.orders.append(root.val)
            if root.right:
                innerOrder(root.right)

        innerOrder(root)
        for i in range(1, len(self.orders)):
            if self.orders[i] <= self.orders[i-1]:
                return False
        else:
            return True


node_1 = TreeNode(5)
node_2 = TreeNode(10)
node_3 = TreeNode(3)
node_1.right = node_2
node_2.left = node_3
s = Solution()

root = s.buildTree([3,4,5], 0)
print s.isValidBST(root)
# print root.val

a = '1'
print a.isdigit()
