class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution(object):

    def preOrder_recursive(self, root):
        if not root:
            return root

        self.list_pre = []

        def pre_order(root):
            if root:
                self.list_pre.append(root.val)
                pre_order(root.left)
                pre_order(root.right)
        pre_order(root)
        return self.list_pre

    def preOrder(self, root):
        if not root:
            return root
        result = []
        stack = [root]
        while len(stack):
            p = stack.pop()
            result.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)

        return result


    def innerOrder_recursive(self, root):
        if not root:
            return root
        self.list_inner = []
        def inner_order(root):
            if root:
                inner_order(root.left)
                self.list_inner.append(root.val)
                inner_order(root.right)

        inner_order(root)
        return self.list_inner

    def innerOrder(self, root):
        if not root:
            return root
        stack = []
        result = []
        p = root
        while p or len(stack):
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                result.append(p.val)
                p = p.right
            # for node in stack:
            #     print node.val,
            # print '---'
        return result


    def postOrder_recursive(self, root):
        if not root:
            return root
        self.list_post = []

        def post_order(root):
            if root:
                post_order(root.left)
                post_order(root.right)
                self.list_post.append(root.val)

        post_order(root)
        return self.list_post

    def postOrder(self, root):
        if not root:
            return root
        result = []
        stack_1 = []
        stack_2 = []
        p = root
        while len(stack_1) or p:
            if p:
                stack_1.append(p)
                if p.right:
                    stack_2.append(1)
                else:
                    stack_2.append(0)
                p = p.left
            else:
                p = stack_1.pop()
                status = stack_2.pop()
                if status == 0:
                    result.append(p.val)
                    p = None
                else:
                    stack_1.append(p)
                    stack_2.append(0)
                    p = p.right
        return result


    def layerOrder(self, root):
        if not root:
            return root

        queue = [root]
        result = []
        while len(queue):
            p = queue[0]
            del (queue[0])
            result.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)

        return result


    def pre_order_2(self, root):
        if not root:
            return root

        stack = [root]
        while stack:
            node = stack.pop()
            print node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def inner_order_2(self, root):
        if not root:
            return None
        stack = []
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                print node.val
                p = node.right

    def post_order_2(self, root):
        if not root:
            return root
        p = (root, 0)
        stack_node = []
        while p or stack_node:
            if p:
                stack_node.append(p)
                if p[0].left:
                    p = (p[0].left, 0)
                else:
                    p = None
            else:
                node = stack_node.pop()
                if node[1] == 1:
                    print node[0].val
                else:
                    stack_node.append((node[0], 1))
                    if node[0].right:
                        p = (node[0].right, 0)
                    else:
                        p = None






node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)

node_1.left = node_2
node_1.right = node_3
node_2.right = node_4
node_2.left = node_6
node_3.left = node_5


node_7 = None

s = Solution()
#s.pre_order_2(node_1)
s.post_order_2(node_1)