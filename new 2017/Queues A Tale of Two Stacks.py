class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class MyQueue(object):

    def __init__(self):
        self.head = None
        self.tail = None


    def peek(self):
        return  self.head.data

    def pop(self):
        if self.head == None: return None
        self.head = self.head.next


    def put(self, value):
        newq = Node(value)
        if  self.head == None:
            self.head = newq
            self.tail = newq
        else:
            self.tail.next = newq
            self.tail = newq




queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
