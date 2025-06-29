class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def construct_tree(bin_string):
    if not bin_string:
        return None

    root_node = TreeNode(bin_string[0])
    queue = [root_node]

    for digit in bin_string[1:]:
        new_node = TreeNode(digit)
        current = queue[-1]
        if digit == "0":
            current.left_child = new_node
        else:
            current.right_child = new_node
        queue.append(new_node)

    return root_node


def traverse_inorder(node, output):
    if node is None:
        return
    traverse_inorder(node.left_child, output)
    output.append(node.value)
    traverse_inorder(node.right_child, output)


def process_number(num):
    binary = format(num, "b")

    tree_root = construct_tree(binary)

    traversal_result = []
    traverse_inorder(tree_root, traversal_result)

    binary_result = "".join(traversal_result)
    return int(binary_result, 2)


number = int(input())
print(process_number(number))
