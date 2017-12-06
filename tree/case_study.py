from binary_search_tree import BinarySearchTree
from tree_node import TreeNode

# Search tree's node
tree = BinarySearchTree()
tree.insert(4)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)  

for i in range(1, 10):
    found = tree.search(i)
    print("{}: {}".format(i, found))

print(tree.bfs_traversal())