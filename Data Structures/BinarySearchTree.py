class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data, node):
        if data < node.data:
            if node.left is not None:
                self.insert(data, node.left)
            else:
                node.left = Node(data)
                node.left.parent = node

        if data > node.data:
            if node.right is not None:
                self.insert(data, node.right)
            else:
                node.right = Node(data)
                node.right.parent = node

    def delete(self, data):
        del_node = self.find(data, self.root)

        if del_node is None:
            raise RuntimeError('Does not exist')
            return

        # Two children
        if del_node.left and del_node.right:
            least_node_bst = self.returnLeastNodeBST(del_node.right)
            del_node.data = least_node_bst.data
            least_node_bst.parent.left = None

        # One Child
        elif del_node.left:
            del_node.parent.left = del_node.left

        elif del_node.right:
            del_node.parent.right = del_node.right

        # No child
        else:
            if del_node.parent.right is del_node:
                del_node.parent.right = None
            else:
                del_node.parent.left = None

    def returnLeastNodeBST(self, node):
        if node.left is not None:
            return self.returnLeastNodeBST(node.left)

        return node

    def find(self, data, node):
        if node.data is data:
            return node

        if node.left is not None:
            return self.find(data, node.left)
        if node.right is not None:
            return self.find(data, node.right)

        return None

    def printTree(self, node):
        print node.data
        if node.left is not None:
            self.printTree(node.left)
        if node.right is not None:
            self.printTree(node.right)

    def isBinarySearchTree(self, node, minKey, maxKey):
        if node is None:
            return True
        if node.data < minKey or node.data > maxKey:
            return False

        return self.isBinarySearchTree(node.left, minKey, node.data) and self.isBinarySearchTree(node.right, node.data, maxKey)

binarySearchTree = BinarySearchTree(1)

binarySearchTree.insert(2, binarySearchTree.root)
binarySearchTree.insert(3, binarySearchTree.root)
binarySearchTree.insert(4, binarySearchTree.root)
binarySearchTree.insert(5, binarySearchTree.root)
binarySearchTree.insert(6, binarySearchTree.root)

binarySearchTree.delete(2)

binarySearchTree.printTree(binarySearchTree.root)

print binarySearchTree.isBinarySearchTree(binarySearchTree.root, 0, 10)

