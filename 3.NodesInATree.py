def countNodeInTree(root):
    
    if root is None:
        return 0
    
    leftcount = countNodeInTree(root.left)
    rightcount = countNodeInTree(root.right)
    #1 cause counting our root node
    return 1 + leftcount + rightcount

class BinaryTreeNode:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    
    
def printTree(root):
    
    #the base that what if the tree is empty
    if root is None:
        return 
    
    print(root.data, end=":")
    #what if either of the subtree node on left or right is empty
    
    if root.left is not None:
        print(root.left.data, end=",")
    if root.left is not None:
        print(root.right.data, end=',')
    print()
    
    printTree(root.left)
    printTree(root.right)
    
def inputTree():
    
    n = int(input("Please enter the node data: "))
    
    #what if our tree is an empty tree and -1 means Node is empty
    if n == -1:
        return None
    
    rootNode = BinaryTreeNode(n)
    
    leftTree = inputTree()
    rightTree = inputTree()
    
    rootNode.left = leftTree
    rootNode.right = rightTree
    
    return rootNode
    
root = inputTree()
printTree(root)
count = countNodeInTree(root)
print("Nodes in Tree = ", count)
