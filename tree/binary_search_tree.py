from tree_node import TreeNode
from collections import deque

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    
    def min_node(self):
        current = self.root

        while current.left_child:
            current = current.left_child

        return current

    def max_node(self):
        current = self.root

        while current.right_child:
            current = current.right_child

        return current
    
    def search(self, data):
        current = self.root

        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    def insert(self, data):
        node = TreeNode(data)

        if self.root is None:
            self.root = node
        else:
            current = self.root
            parent = None

            while True:
                parent = current
                
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def delete(self, data):
        parent, node = self.get_node_parent(data)

        if parent is None and node is None:
            return False

        #Get children count
        children_count = 0

        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1
        
        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root = None        
        elif children_count == 1:
            next_node = None

            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root = next_node
        else:
            # searching for inorder successor
            parent_of_leftmost_node = node
            leftmost_node = node.right_child

            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            
            node.data = leftmost_node.data

            # attaching new child node  
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child
    
    def get_node_parent(self, data):
        parent = None
        current = self.root

        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child 
        
        return (parent, current)
    
    # DFS traversal
    def inorder(self, root):
        # left subtree, node, right subtree
        current = root
        if current is None:
            return

        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)
    
    def preorder(self, root):
        # node, left subtree, right subtree
        current = root
        if current is None:
            return

        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)
    
    def postorder(self, root):
        # left subtree, right subtree, node
        current = root
        if current is None:
            return

        self.postorder(current.left_child)
        self.postorder(current.right_child)
        print(current.data)

    # BFS traversal
    def bfs_traversal(self):
        nodes_list = []
        traversal_queue = deque([self.root])

        while(len(traversal_queue) > 0):
            node = traversal_queue.popleft()
            nodes_list.append(node.data)

            if node.left_child:
                traversal_queue.append(node.left_child)
            
            if node.right_child:
                traversal_queue.append(node.right_child)
        
        return nodes_list