class Node:

    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    
    def insert(self, node):
        if self.data > node.data:
        #If node is smaller than current root node go the left subtree
            if not self.left:
                #if no further left subtree exists append the current node as left child
                self.left = node
            else:
                #else keep recursively traversing to left subtree
                self.left.insert(node)

        #If node is greater than current root node go the right subtree
        if self.data < node.data:
            if not self.right:
                #if no further left righttree exists append the current node as right child
                self.right = node
            else:
                #else keep recursively traversing to right subtree
                self.right.insert(node)
    
    def print_inorder(self):
        if self.data:
            if self.left: self.left.print_inorder()
            print(self.data, end= ' ')
            if self.right: self.right.print_inorder()

    def print_preorder(self):
        if self.data:
            print(self.data, end=' ')
            if self.left: self.left.print_inorder()
            if self.right: self.right.print_inorder()

    def print_postorder(self):
        if self.data:
            if self.left: self.left.print_inorder()
            if self.right: self.right.print_inorder()
            print(self.data, end=' ')
    
    def isBST(self, left=None, right=None):
        left_result = True
        right_result = True

        if self == None: return True

        if (left and self.data <= left.data): return False
        if (right and self.data >= right.data): return False

        if self.left:
            left_result = self.left.isBST(left, self)
        if self.right:
            right_result = self.right.isBST(self, right) 


        return left_result and right_result

    
class BST:

    def __init__(self, root):
        self.root = Node(root)

    def add(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:
            self.root.insert(new_node)

    def inorder(self):
        if self.root:
            self.root.print_inorder()

    def preorder(self):
        if self.root:
            self.root.print_preorder()
    def postorder(self):
        if self.root:
            self.root.print_postorder()
    def isBST(self):
        if self.root:
            return self.root.isBST()


if __name__ == "__main__":

    #example of BST
    bst = BST(50)
    bst.add(30)
    bst.add(20)
    bst.add(40)
    bst.add(25)
    bst.add(70)
    bst.add(50)
    bst.add(20) #this is validation of duplicate entry, this will be ignored by BST.

    print('======= Binary Search Tree in Inorder(Left Root Right) =======')
    bst.inorder()
    print('\n======= Binary Search Tree in Preorder(Root Left Right) =======')
    bst.preorder()
    print('\n======= Binary Search Tree in Postorder(Left Right Root) =======')
    bst.postorder()
    print('\n======= Is Tree a Binary Search Tree? =======>', end=' ')
    print(bst.isBST())

    #example of non BST
    tree = Node(3)
    tree.left = Node(2)
    tree.left.left = Node(1)
    tree.left.right = Node(4)
    tree.right = Node(5)

    
    print('======= Non Binary Search Tree in Inorder(Left Root Right) =======')
    tree.print_inorder()
    print('\n======= Is Tree a Binary Search Tree? =======>', end=' ')
    print(tree.isBST())

