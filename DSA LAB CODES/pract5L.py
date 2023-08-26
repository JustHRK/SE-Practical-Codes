# Convert given binary tree into threaded binary tree. Analyze time and space complexity of the algorithm.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.thread = False


def create_threaded_binary_tree(root, prev):
    if root is None:
        return prev

    prev = create_threaded_binary_tree(root.left, prev)

    if prev is not None and prev.right is None:
        prev.right = root
        prev.thread = True

    prev = root

    prev = create_threaded_binary_tree(root.right, prev)

    return prev


def print_threaded_binary_tree(root):
    if root is None:
        return

    current = leftmost(root)

    while current:
        print(f"Node: {current.data}")
        print(f"Right Threaded: {current.right.data if current.right else None}")
        print(f"Is Threaded: {current.thread}")
        print()

        if current.thread:
            current = current.right
        else:
            current = leftmost(current.right)


def leftmost(node):
    if node is None:
        return None

    while node.left:
        node = node.left

    return node


# Constructing the binary tree
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

# Convert the binary tree into a threaded binary tree
create_threaded_binary_tree(root, None)

# Print the threaded binary tree
print("Threaded Binary Tree:")
print_threaded_binary_tree(root)
