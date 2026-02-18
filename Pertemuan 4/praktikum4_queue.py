"""
===========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
===========================================

# Queue
===========================================
"""

# Implementasi Dasar: Define Node
# ===========================================
class Node:
    "Node Class untuk LinkedList, Queue, Stack, dll."
    def __init__(self, data): # Constructor
        self.data = data # Menyimpan nilai
        self.next = None # Pointer ke node selanjutnya

# Queue denggan 2 pointer : front dan rear
class Queue:
    "Queue class."
    def __init__(self):
        self.front = None # Node paling depan
        self.rear = None # Node paling belakang

    def enqueue(self, data):
        "Menambah node di belakang/rear"
        node_baru = Node(data)

        # Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.rear is None:
            self.front = self.rear = node_baru
            return

        self.rear.next = node_baru
        self.rear = node_baru

    def dequeue(self):
        "Menghapus node di depan/front"

        # Jika queue kosong, jangan hapus
        if self.front is None:
            return

        # Ambil data terdepan
        _ = self.front.data
        # Geser front ke node berikutnya
        self.front = self.front.next
        # Check if rear == front
        if self.front is None:
            self.rear = None

    def tampilkan(self):
        "Menampilkan data dari front ke rear"
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")

queue = Queue()
queue.enqueue("Aku pake Arch btw")
queue.enqueue("Aku pake Bazzite btw")
queue.enqueue("Aku pake CachyOS btw")
queue.tampilkan()
queue.dequeue()
queue.tampilkan()
