__author__ = 'Senyutina'
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
        if root == None:
            return -1
        else:
            return 1 + max(self.getHeight(root.right),self.getHeight(root.left))

    def levelOrder(self,root):
         if root == None:
            return -1
         else:
            print(root.data)
            self.levelOrder(root.left)
            self.levelOrder(root.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
#height=myTree.getHeight(root)
#print(height)
myTree.levelOrder(root)
