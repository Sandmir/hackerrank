__author__ = 'marina_senyutina'
"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as
"""
class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

   def Insert(self, data):
       newNode = Node(data)
       actualNode = self

       while actualNode.next is not None:
          actualNode = actualNode.next

       actualNode.next = newNode

       return self


   def InsertNth(self, data, position):
     if position == 0:
        newNode = Node(data)
        actualNode = self

        newNode.next = actualNode

        return self

     else:
          newnode = Node(data)
          actualNode = self
          n = 0
          while n != position:
              n += 1
              actualNode = actualNode.next
          nextNode =  actualNode.next.next
          actualNode.next = newnode
          newnode.next = nextNode

          return self

   def print_list(self):
       print(self.data)
       if self.next == None:
           print("Null")

       else:
           self.next.print_list()




l = Node()
l.Insert(1)
l.Insert(5)
l.print_list()
l.InsertNth(99,0)
print('------')
l.print_list()