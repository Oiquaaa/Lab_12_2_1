class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #ця ф-ція вставляє new node в кінець списку.Створює цю new node з заданою датою,а якщо лист пустий - задає head node до new node 
    
    #or створює новий вузол з заданим data та вставляє його в кінець списку. Якщо список пустий, то head встановлюється на новий вузол.
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    #ця ф-ція вставляє новий вузол зі значенням value2 перед вузлом зі значенням value1. Якщо список пустий, то метод просто повертається. Якщо вузол зі значенням value1 знаходиться на початку списку, то новий вузол стає новим головним елементом списку. В іншому випадку, метод перебирає вузли у списку, поки не знайде вузол зі значенням value1 і вставляє новий вузол перед ним.
    def insert_before_value(self, value1, value2):
        if not self.head:
            return

        if self.head.data == value1:
            new_node = Node(value2)
            new_node.next = self.head
            self.head = new_node
            return
        else:
            prev = None
            current = self.head

        while current:
            if current.data == value1:
                new_node = Node(value2)
                new_node.next = current
                prev.next = new_node
                return
            else:
                prev = current
                current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.insert_at_end(4)
llist.insert_at_end(5)
llist.insert_at_end(6)

llist.print_list()

llist.insert_before_value(1, 8) 
llist.insert_before_value(3, 6) 
llist.insert_before_value(5, 9) 

llist.print_list()
