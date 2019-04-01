__author__ = 'Senyutina'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head is None:
            head = Node(data)
        else:
            head.next = self.insert(head.next, data)
        return head



        '''
        node = Node(data)
        if head  ==  None:
            node.next = None
            head = node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = node
        return head
         '''



mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);