class DoubleLinkedList:

    class _Node:

        def __init__(self, element, prev, next_element):
            self._element =element
            self._prev = prev
            self._next = next_element

    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def insert(self, element):
        pointer = self._head._next
        new_node = self._Node(element, None, None)
        while pointer is not self._tail:
            pointer = pointer._next
        new_node._prev = pointer._prev
        new_node._next = pointer
        pointer._prev._next = new_node
        pointer._prev = new_node
        self._size += 1

    def delete(self, element):
        pointer = self._head._next
        if self._size != 0:
            while pointer is not self._tail:
                if pointer._element == element:
                    pointer._prev._next = pointer._next
                    pointer._next._prev = pointer._prev
                    pointer._prev = pointer._next = pointer._element = None
                    self._size -= 1
                    break
                else:
                    pointer = pointer._next


    def printList(self):
        pointer = self._head._next
        result ="[ "
        if self._size != 0:
            while pointer is not self._tail:
                result += pointer._element + " "
                pointer = pointer._next
        result += "]"
        print(result)

    def swap(self, element1, element2):
        pointer1 = self._head._next
        while pointer1._next._element != element1:
            pointer1 = pointer1._next

        pointer2 = pointer1._next
        while pointer2._next._element != element2:
            pointer2 = pointer2._next


        element1 = pointer1._next
        element2 = pointer2._next
        pointer1._next = element2
        element2._prev = pointer1
        pointer2._next = element1
        element1._prev = pointer2
        element1._next._prev = element2
        if(element2._next != None):
            element2._next._prev = element1
        temp_node = element2._next
        element2._next = element1._next
        element1._next = temp_node

    def middleElement(self):
        pointer1 = self._head
        pointer2 = self._tail
        flag = True
        while flag :
            if pointer1 == pointer2:
                print(pointer1._element)
                flag = False
                
            elif pointer1._next == pointer2:
                print(pointer1._element)
                flag = False

            else:
                pointer1 = pointer1._next
                pointer2 = pointer2._prev

    def appendList(self, anotherList):
        pointer = self._tail._prev
        pointer._next = anotherList._head._next
        anotherList._head._next._prev = pointer
        self._tail = anotherList._tail


L = DoubleLinkedList()
L.insert("A")
L.insert("S")
L.insert("D")
L.insert("F")
L.insert("G")
L.printList()
L.swap("S","G")
L.printList()
L.middleElement()
M = DoubleLinkedList()
M.insert("1")
M.insert("2")
M.insert("3")
M.insert("4")
M.insert("5")
L.appendList(M)
L.printList()
