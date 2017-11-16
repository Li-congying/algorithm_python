#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """








node_1 = TreeNode(1)
node_2 = TreeNode(-1)
node_3 = TreeNode(2)
node_4 = TreeNode(-2)

node_1.left = node_2
node_2.left = node_4
node_1.right = node_3

codec = Codec()
str =  codec.serialize(node_1)
#print str
#str = '(2,(3,()))'
node =  codec.deserialize(str)
print node.val, node.left.val, node.right.val,
