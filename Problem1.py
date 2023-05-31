class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
 
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # добавление нового элемента в конец списка
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node

    # метод разворота двусвязного списка
    def reverse(self):
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head, self.tail = self.tail, self.head

    # отображение элементов списка      
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
          
# создание списка          
lst = DoublyLinkedList() 
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)

# отображение исходного списка
print("Исходный список:")
lst.display() # 1 2 3 4

# разворот списка и отображение его элементов
lst.reverse() 
print("\nСписок после разворота:")
lst.display() # 4 3 2 1