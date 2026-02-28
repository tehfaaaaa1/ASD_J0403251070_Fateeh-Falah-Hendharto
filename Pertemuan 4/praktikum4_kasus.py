"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""

# ==========================================
# Studi Kasus: Sistem Antrian Layanan Akademik
# Implementasi Queue ->
# Stack ==> Front -> C -> B -> A -> Rear
# Queue ==> Front -> A -> B -> C -> Rear
# Enqueue: Memindahkan pointer rear
# Dequeue: Memindahkan pointer front
# ==========================================


# 1) Mendefinisikan Node (LinkedList)
class Node:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.next = None


# 2) Mendefinisikan Queue yang terdiri dari Front dan Rear
class queueAkademik:
    "Queue Logic"

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        "Check if empty"
        return self.front is None

    def enqueue(self, nama, nim):
        "Menambah item di paling belakang"
        new_node = Node(nama, nim)

        # Jika data kosong, tambahkan new node
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        # Selain itu, tambahkan node ke rear
        else:
            self.rear.next = new_node
            self.front = new_node

    def dequeue(self):
        "Menghapus node di paling depan. Return node yang dihapus."
        # Check if empty
        if self.is_empty():
            print("Antrian kosong. Tidak ada yang dilayani.")
            return None

        # Lihat data di front, lalu simpan di variabel sementara
        selected_node = self.front

        # Geser pointer ke sebelah
        self.front = self.front.next

        # Handling if only 1 node
        if self.front is None:
            self.rear = None

        return selected_node

    def show(self):
        "Show Queue data"
        print("Daftar antrian mahasiswa :")
        current = self.front
        index = 1
        while current:
            print(f"{index}. {current.nim} - {current.nama}")
            current = current.next
            index += 1


# Main Program
def main():
    queue = queueAkademik() # Instantiate queue
    while True:
        print("\n===== CUSTOMER SERVICE MAHASISWA =====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()
        match (pilihan):
            case '1':
                nim = input("Masukkan NIM\t: ").strip()
                nama = input("Masukkan Nama\t: ").strip()
                queue.enqueue(nama, nim)
                print("Mahasiswa berhasil ditambahkan!")
            case '2':
                mahasiswa = queue.dequeue()
                if mahasiswa is None:
                    continue
                print(
                    f"Mahasiswa yang dilayani: {mahasiswa.nim} - {mahasiswa.nama}")
            case '3':
                queue.show()
            case '0':
                print("Terima kasih telah menggunakan pelayanan kami!")
                return


main()
