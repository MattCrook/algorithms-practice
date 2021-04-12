class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def atEnd(self, newData):
        NewNode = Node(newData)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode

    def printList(self):
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next


list = LinkedList()
list.head = Node('Monday')
e2 = Node('Tuesday')
e3 = Node('Wednesday')
e4 = Node('Thursday')
e5 = Node('Friday')
e6 = Node('Saturday')

list.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
list.atEnd('Sunday')

list.printList()
