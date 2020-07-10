class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        curr = root
        self.heights = list()
        self.traverse(root, -1)
        return max(self.heights)

    def traverse(self, node, height):
        if node==None:
            self.heights.append(height)
            return
        else:
            self.traverse(node.left, height + 1)
            self.traverse(node.right, height + 1)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       