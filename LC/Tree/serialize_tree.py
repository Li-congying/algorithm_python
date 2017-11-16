'''
Serialization is the process of converting a data structure or object into a sequence of 
bits so that it can be stored in a file or memory buffer, or transmitted across a network 
connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no 
restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this 
string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a 
binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''


# Definition for a binary tree node.
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

        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if not node:
                result.append('#')
            else:
                result .append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        while result and result[-1] == '#':
            result.pop()

        return ','.join(result) if result else ''


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data:
            list = data.split(',')
            root = TreeNode(int(list.pop(0)))
            queue = [root]
            while queue:
                node = queue.pop(0)
                if list:
                    left = list.pop(0)
                    if left != '#':
                        node_left = TreeNode(int(left))
                        node.left = node_left
                        queue.append(node_left)
                if list:
                    right = list.pop(0)
                    if right != '#':
                        node_right = TreeNode(int(right))
                        node.right = node_right
                        queue.append(node_right)
            return root
        else:
            return None


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))


from collections import deque


class Codec2:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []

        ret = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                ret.append(node)

        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        queue = deque(data)
        root = TreeNode(queue.popleft())
        prevLevel = [root]

        while len(prevLevel) > 0:
            newLevel = []

            for node in prevLevel:
                if not node:
                    continue

                left = queue.popleft()
                right = queue.popleft()

                if left != None:
                    node.left = TreeNode(left)
                    newLevel.append(node.left)

                if right != None:
                    node.right = TreeNode(right)
                    newLevel.append(node.right)

            prevLevel = newLevel

        return root

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)

node_1.left = node_2
# node_1.right = node_3
# node_2.right = node_4

obj = Codec2()
ser = obj.serialize(node_1)
print ser

root = obj.deserialize(ser)



def getTreeVal(root):
    if root:
        print root.val
        getTreeVal(root.left)
        getTreeVal(root.right)

getTreeVal(root)