class BinaryTreeNode:
    
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None
        
        
#Making A basic Tree HArdcoded

n1 = BinaryTreeNode(10)
n2 = BinaryTreeNode(5)
n3 = BinaryTreeNode(20)
n4 = BinaryTreeNode(3)
n5 = BinaryTreeNode(75)

n1.left = n2
n1.right = n3

n2.left = n4
n3.right = n5

def printInOrder(root): #Left Root Right
    
    if root is None:
        return
    
    
    printInOrder(root.left)
    print(root.data)
    printInOrder(root.right)
    


printInOrder(n1)
