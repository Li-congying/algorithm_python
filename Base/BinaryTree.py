class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree(object):

    def __init__(self, list):

        self.list_ = list
        self.root = self.build_tree(self.list_)
        self.cur_list = []

    def build_tree(self, list = []):
        if len(list) == 0:
            return None
        mid = len(list)/2
        root = TreeNode(list[mid])
        root.left = self.build_tree(list[0:mid])
        if root.left:
            root.left.parent = root
        root.right = self.build_tree(list[mid+1:])
        if root.right:
            root.right.parent = root
        return root

    def go_along_tree(self, root):
        if not root:
            return self.cur_list
        self.cur_list.append(root.val)
        self.go_along_tree(root.left)
        self.go_along_tree(root.right)
        return self.cur_list



    def insertInto(self, x):
        node = TreeNode(x)
        if not self.root:
            self.root = node
            return
        p = self.root
        while p:
            if x > p.val:
                if p.right:
                    p = p.right
                else:
                    p.right = node
                    break
            else:
                if p.left:
                    p = p.left
                else:
                    p.left = node
                    break

    #def get_processor(self, p):


    def pre_order(self, root):

        print root.val,
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)


    def pre_order_stack(self, root):
        node_stack = [root]
        while node_stack:
            node = node_stack.pop()
            if node:
                print node.val,
            if node.right:
                node_stack.append(node.right)
            if node.left:
                node_stack.append(node.left)


    def inner_order(self, root):

        if root.left:
            self.inner_order(root.left)
        if root:
            print root.val,
        if root.right:
            self.inner_order(root.right)

    def inner_order_stack(self, root):

        node_stack = []
        node = root
        while node or node_stack:
            if node:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop()
                print node.val,
                node = node.right

    def post_order(self, root):
        if root.left:
            self.post_order(root.left)
        if root.right:
            self.post_order(root.right)
        if root:
            print root.val,

    def post_order_stack(self, root):
        node_stack = []
        status_stack = []
        node = root
        while node or node_stack:
            if node:
                node_stack.append(node)
                status_stack.append(0)
                node = node.left
            else:
                node = node_stack.pop()
                status = status_stack.pop()
                if status:
                    print node.val,
                    node = None
                else:
                    node_stack.append(node)
                    status_stack.append(1)
                    node = node.right







bt = BinaryTree([1,2,3,4])


bt.insertInto(5)
bt.insertInto(3.5)
#bt.pre_order(bt.root)
bt.post_order(bt.root)
bt.post_order_stack(bt.root)