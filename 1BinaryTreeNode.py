
class BinaryTreeNode:

    def __init__(self,data):
        self.data = data  #our node should have some data
        self.left = None
        self.right = None   #two address holders for left node and right node

rootNode = BinaryTreeNode(2)
node1 = BinaryTreeNode(4)
node2 = BinaryTreeNode(8)

#connected children to parent node
rootNode.left = node1
rootNode.right = node2

print(rootNode.data)
print(rootNode.left.data)
print(rootNode.right.data)