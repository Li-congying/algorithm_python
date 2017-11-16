# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.cur_nodes = []
        if root:
            self.cur_nodes.append(root)
            node = root
            while node.left:
                self.cur_nodes.append(node.left)
                node = node.left


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur_nodes:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        node = self.cur_nodes.pop()

        cur_node = node.right
        while cur_node:
            self.cur_nodes.append(cur_node)
            cur_node = cur_node.left

        return node.val

        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())



list = [3,4,1,2,8,6,7,9]

r_n = TreeNode(5)
for val in list:
    root = r_n
    while True:
        if val > root.val:
            if root.right:
                root = root.right
            else:
                node = TreeNode(val)
                root.right = node
                break
        else:
            if root.left:
                root = root.left
            else:
                node = TreeNode(val)
                root.left = node
                break

bst_iter = BSTIterator(r_n)

while bst_iter.hasNext():
    val = bst_iter.next()
    print val


