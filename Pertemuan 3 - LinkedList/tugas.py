"""
Docstring for Pertemuan 3 - LinkedList.tugas
"""
class Node:
    "Node"
    def __init__(self,data=0):
        self.data = data
        self.next = None

class LinkedList:
    "LinkedList"
    def __init__(self):
        self.head = None
        self.tail = None # Pointer tail

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node # Jika List kosong
            self.tail = new_node # Tail menunjuk ke Node pertama
        else:
            self.tail.next = new_node # Sambung tail ke node baru
            self.tail = new_node # Update tail ke node baru
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

    # Latihan 1
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    # Latihan 4
    def merge(self, list1: Node, list2: Node):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.data < list2.data:
            list1.next = self.merge(list1.next, list2)
            return list1

        list2.next = self.merge(list1, list2.next)
        return list2

class CircularSingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head # Circular link
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def display(self):
        if not self.head:
            print("List is empty.")
            return

        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("... (Back to head)")

    def search(self, key):
        if not self.head:
            print("LinkedList kosong.")
            return
        temp = self.head
        count = 1
        while temp and count <= 3:
            if temp.data == key:
                return True
            temp = temp.next
            count += 1
        return False

LL = LinkedList()
LL.insert_at_end(3)
LL.insert_at_end(5)
LL.insert_at_end(15)
LL.insert_at_end(2)
print("Linked List Sample:")
LL.display()

# Latihan 1
print("Delete 15:")
LL.delete_node(15)
LL.display()

# Latihan 2
CSLL_lat_2_1 = CircularSingleLinkedList()
CSLL_lat_2_1.insert_at_end(3)
CSLL_lat_2_1.insert_at_end(7)
CSLL_lat_2_1.insert_at_end(12)
CSLL_lat_2_1.insert_at_end(19)
CSLL_lat_2_1.insert_at_end(25)
print("Circular Single Linked List Sample:")
CSLL_lat_2_1.display()

x = int(input("Ketik angka yang dicari: "))

match (CSLL_lat_2_1.search(x)):
    case True:
        print("Angka ditemukan!")
    case False:
        print("Angka tidak ditemukan!")

# Latihan 4
LL_lat_4_x = LinkedList()
LL_lat_4_y = LinkedList()

LL_lat_4_x.insert_at_end(1)
LL_lat_4_x.insert_at_end(3)
LL_lat_4_x.insert_at_end(5)
LL_lat_4_x.insert_at_end(7)

LL_lat_4_y.insert_at_end(2)
LL_lat_4_y.insert_at_end(4)
LL_lat_4_y.insert_at_end(6)
LL_lat_4_y.insert_at_end(8)

print("Linked List X:")
LL_lat_4_x.display()
print("Linked List Y:")
LL_lat_4_y.display()
LL_lat_4_x.merge(LL_lat_4_x.head, LL_lat_4_y.head)
print("Linked List setelah digabung:")
LL_lat_4_x.display()
