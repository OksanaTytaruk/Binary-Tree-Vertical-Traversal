from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(root):
    columns = defaultdict(list)

    def dfs(node, row, column):
        if node is None:
            return

        columns[column].append((row, node.val))

        dfs(node.left, row + 1, column - 1)
        dfs(node.right, row + 1, column + 1)

    dfs(root, 0, 0)

    result = []

    for column in sorted(columns):
        values = columns[column]

        # Спочатку сортуємо за рядком,
        # потім за значенням вузла
        values.sort(key=lambda x: (x[0], x[1]))

        result.append([value for row, value in values])

    return result


# Приклад 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print("Приклад 1:", verticalTraversal(root1))


# Приклад 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)

print("Приклад 2:", verticalTraversal(root2))


# Приклад 3
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(6)
root3.right.left = TreeNode(5)
root3.right.right = TreeNode(7)

print("Приклад 3:", verticalTraversal(root3))