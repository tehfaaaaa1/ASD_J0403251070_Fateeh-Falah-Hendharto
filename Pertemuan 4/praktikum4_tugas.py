"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : TPL B1
==========================================
"""

# ===================================================
# Tugas Hands-on: Sistem Antrian Bengkel Motor
# ===================================================


# TUGAS SISTEM ANTRIAN BENGKEL
class Node:
    "Node class untuk LinkedList"

    def __init__(self, number: int, nama, servis):
        self.number = number
        self.nama = nama
        self.servis = servis
        self.next = None


class QueueBengkel:
    "Queue class untuk mengelola LinkedList secara FIFO"

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, nama, servis):
        "Menambah item di paling belakang."
        # Auto-indexing and increment index based on rear number
        # If list is empty, first to enter becomes 1
        # Else, increment based on last person's number
        num = self.rear
        if num is None:
            num = 1
        else:
            num = num.number + 1

        new_node = Node(num, nama, servis)

        # If list is empty, create new node
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        # If lists is not empty, create node after last
        else:
            self.rear.next = new_node
            self.rear = new_node

        print("Pelanggan berhasil ditambah!")  # Success message

    def dequeue(self):
        "Menghapus item paling depan."

        # If list is empty
        if self.front is None:
            print("List masih kosong. Tidak ada yang diservis.")
            return None

        # Select temporary node in the front
        # Then, move front of list to next node
        # This will replace the front of the list to the next
        temp_node = self.front
        self.front = self.front.next

        # If list is empty after deletion
        if self.front is None:
            self.rear = None

        print("Pelanggan berhasil dilayani!")  # Success Message

        return temp_node  # Return the temporary node if needed

    def show(self):
        "Tampilkan isi LinkedList."
        current_node = self.front  # Holds current position during looping
        print("== Antrian == ")
        if current_node is None:
            print("Tidak ada data!")
        while current_node:  # Loop through the list until rear
            print(f"{current_node.number}. {current_node.nama} - {current_node.servis}")
            current_node = current_node.next


def main():
    "Main"
    query = QueueBengkel()

    while True:
        print("\n=== Servis Bengkel Motor ===")
        print("Tefa Motor Comp 2026\n")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("0. Keluar")

        choice = input("Pilih Menu : ")
        match (choice):
            case "1":  # Enqueue pelanggan
                nama = input("Masukkan nama pelanggan\t\t: ")
                servis = input("Masukkan servis yang diperlukan\t: ")
                query.enqueue(nama, servis)
            case "2":  # Dequeue pelanggan
                query.dequeue()
            case "3":  # Show list pelanggan
                query.show()
            case "0":
                return
            case _:  # Base case AKA if choice is not valid
                print("Masukkan pilihan menu yang benar!")


if __name__ == "__main__":
    main()
