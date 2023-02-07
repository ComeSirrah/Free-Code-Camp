class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @staticmethod
    def depth_first(root):
        if not root:
            return []
        tree_values = []
        stack = [root]
        while stack:
            current = stack.pop()
            tree_values.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return tree_values


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(Node.depth_first(a))
