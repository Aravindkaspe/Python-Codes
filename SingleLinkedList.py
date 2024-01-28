class SingleLinkedList:

    class _Node:

        def __init__(self,element,next_element):
            self.element = element
            self.next = next_element

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def append(self, element):
        new_node = self._Node(element, None)
        if self._size == 0:
            self._head = new_node
            self._size = 1
        else:
            pointer = self._head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = new_node
            self._size += 1

    def secondLast(self):
        if self._size >= 2:
            pointer = self._head
            while pointer.next.next != None:
                pointer = pointer.next
            print(pointer.element)

    def appendList(self,another_list):
        pointer = self._head
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = another_list._head

    def printList(self):
        pointer = self._head
        while pointer.next != None:
            print(pointer.element)
            pointer = pointer.next
        print(pointer.element)

    def countNumber(self):
        pointer = self._head
        self.count = 0
        def counter(pointer):
            if pointer.next == None:
                return 1
            else:
                return 1+counter(pointer.next)
        print("Total elements in the list are : ",counter(pointer))

    def swap(self, element1, element2):
        pointer1 = self._head
        while pointer1.next.element != element1:
            pointer1 = pointer1.next
        
        pointer2 = pointer1.next
        while pointer2.next.element != element2 :
            pointer2 = pointer2.next

        element1 = pointer1.next
        element2 = pointer2.next
        pointer1.next = element2
        pointer2.next = element1
        temp = element2.next
        element2.next = element1.next
        element1.next = temp
        
        

L = SingleLinkedList()
L.append("R")
L.append("S")
L.append("A")
L.append("D")
L.secondLast()
M = SingleLinkedList()
M.append("1")
M.append("2")
M.append("3")
M.append("4")
L.appendList(M)
L.printList()
L.countNumber()
L.swap("S","3")
L.printList()

                
