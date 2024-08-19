class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Graph:
    def max_magical_grove(self, root, is_left):
        if root is None:
            return 0

        max_value = root.val
        if is_left:
            max_value = max(max_value, self.max_magical_grove(root.right, False))
        else:
            max_value = max(max_value, self.max_magical_grove(root.left, True))

        return max_value

    def max_total_value(self, root):
        if root is None:
            return 0

        left_max = self.max_magical_grove(root.left, True)
        right_max = self.max_magical_grove(root.right, False)
        
        total_value = left_max + right_max + root.val
        return total_value

    def max_magic_groves(self, root):
        if root is None:
            return 0

        max_total_value = self.max_total_value(root)
        left_max = self.max_magic_groves(root.left)
        right_max = self.max_magic_groves(root.right)

        return max(max_total_value, left_max, right_max)

if __name__ == "__main__":
    graph = Graph()

    # Constructing the binary tree
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(5)

    max_total_value = graph.max_magic_groves(root)
    print("The maximum total value is:", max_total_value)
