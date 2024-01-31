
class BinaryTreeNode:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
def printTree(root):
    
    #base case if root is None return nothing
    
    if root is None:
        return
    
    print(root.data, end=":")
    
    if root.left is not None:
        print("L => ", root.left.data, end=',')
    
    if root.right is not None:
        print("R => ", root.right.data, end= ",")
    print()
    
    printTree(root.left) #to access our left Subtree
    printTree(root.right) #to access our right subtree
    

def inputTree():
    root = int(input())
    
    if root == -1:
        return None
    
    rootNode = BinaryTreeNode(root)
    leftTree = inputTree()
    rightTree = inputTree()
    
    #here we are building bottom to top
    #all subtrees in the bottom will get connect to main trees going up
    rootNode.left = leftTree
    rootNode.right = rightTree
    
    return rootNode

root = inputTree()
printTree(root)
