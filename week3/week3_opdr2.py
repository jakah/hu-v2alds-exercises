class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.head
        if current != None:
            s = s + str(current)
            current = current.next
        while current != None:
            s = s + " -> " + str(current)
            current = current.next
        if not s:  # s == '':
            s = 'empty list'
        return s

    def addLast(self, e):
        if not self.head:  # self.head == None:
            self.head = ListNode(e, None)
            self.tail = self.head
        else:
            n = ListNode(e, None)
            self.tail.next = n
            self.tail = self.tail.next

    def delete(self, e):
        if self.head:  # self.head != None:
            if self.head.data == e:
                self.head = self.head.next
                if self.head == None:
                    self.tail = None
            else:
                current = self.head
                while current.next != None and current.next.data != e:
                    current = current.next
                if current.next != None:
                    current.next = current.next.next
                if current.next == None:
                    self.tail = current


class MyCircularLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        start = self.tail
        current = self.tail.next
        if current != start:
            s = s + str(current)
            current = current.next
        while current != start:
            print("while")
            print(start)
            s = s + " -> " + str(current)
            current = current.next
        if not s:  # s == '':
            s = 'empty list'
        return s

    def addLast(self, e):
        if self.tail == None:
            self.tail = ListNode(e, self)
            print(self.tail.data)
        else:
            self.tail = ListNode(e, self.tail.next)
            print(self.tail.data)

    def delete(self, e):
        if self.tail == None:
            return False
        elif self.tail.next == None:
            self.tail = None
# Original main
# if __name__ == '__main__':
#     mylist =  MyLinkedList()
#     print(mylist)
#     mylist.addLast(1)
#     mylist.addLast(2)
#     mylist.addLast(3)
#     print(mylist)
#     mylist.delete(2)
#     print(mylist)
#     mylist.delete(1)
#     print(mylist)
#     mylist.delete(3)
#     print(mylist)


if __name__ == '__main__':
    mylist = MyCircularLinkedList()
    # print(mylist)
    mylist.addLast(1)
    mylist.addLast(2)
    mylist.addLast(3)
    print("Start print")
    print(mylist)
    mylist.delete(2)
    print(mylist)
    mylist.delete(1)
    print(mylist)
    mylist.delete(3)
    print(mylist)
