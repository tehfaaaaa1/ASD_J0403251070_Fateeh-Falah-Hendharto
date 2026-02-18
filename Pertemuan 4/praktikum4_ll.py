"""
===========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
===========================================

# LinkedList, Stack
===========================================
"""

# Implementasi Dasar: Node pada Linked List
# =========================================
class Node:
    "Node Class untuk LinkedList, Queue, Stack, dll."
    def __init__(self, data): # Constructor
        self.data = data # Menyimpan nilai
        self.next = None # Pointer ke node selanjutnya

# 1) Membuat Node satu-persatu
node_a = Node("A")
node_b = Node("B")
node_js = Node("JS")

# 2) Menghubungkan Node (A -> B -> C -> None)
node_a.next = node_b
node_b.next = node_js

# 3) Menentukan node pertama (head)
head = node_a

# 4) Traversal : Menelusuri dari head sampai None
current = head
while current:
    print(current.data)
    current = current.next

# ===============================================
# Implementasi Dasar: Linked List + Insert Awal
# ===============================================

class LinkedList: # Stack
    "Class LinkedList berisi function mengenai LinkedList"
    def __init__(self):
        self.head = None

    def insert_awal(self, data):
        "Insert node baru di awal. Push dalam Stack karena data terakhir adalah head."
        # Buat node baru
        new_node = Node(data) # Panggil class Node

        # Node baru menunjuk ke head class
        new_node.next = self.head

        # Head pindah ke node Baru
        self.head = new_node

    def hapus_awal(self):
        "Hapus node yang di awal. Pop dalam Stack."
        _data_terhapus = self.head.data # Rekam data yang ingin dihapus. Var bersifat opsional
        self.head = self.head.next # Pindah head ke sebelahnya

    def traversal(self):
        "Telusuri seluruh isi LinkedList"
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

LL = LinkedList()
LL.insert_awal("x")
LL.insert_awal("y")
LL.insert_awal("z")
LL.traversal()
LL.hapus_awal()
LL.traversal()
