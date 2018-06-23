class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Avl:
    def __init__(self):
        self.root = Node(5)

    def insert(self, val):
        prev = None
        current = self.root
        while current:
            prev = current
            if val > current.val:
                current = current.right
                if not current:
                    prev.right = Node(val)
            elif val <= current.val:
                current = current.left
                if not current:
                    prev.left = Node(val)

    def check(self):
        self.height(self.root)

    def height(self, node):
        "check if node is balanced"
        left_height, right_height = 0, 0

        if node.left:
            left_height = self.height(node.left)
        if node.right:
            right_height = self.height(node.right)
        diff = left_height - right_height
        if abs(diff) > 1:
            print("unbalanced")
        return 1 + max(left_height, right_height)


tree = Avl()
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.check()
