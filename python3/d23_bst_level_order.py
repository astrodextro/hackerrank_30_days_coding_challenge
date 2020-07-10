import sys

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

    def levelOrder(self,root):
        #Write your code here
        self.levels = {}
        self.traverse(root, 0)
        all = []
        for value in self.levels.values():
            all += value
        print(*all)

    def traverse(self, node, height):
        if node==None:
            return
        else:
            if not height in self.levels.keys():
                self.levels[height] = []
            self.levels[height] += [node.data]
            self.traverse(node.left, height + 1)
            self.traverse(node.right, height + 1)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
