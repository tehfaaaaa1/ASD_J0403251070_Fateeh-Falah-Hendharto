"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1

Latihan 2 : Membuat Binary Search Tree Sederhana
"""


class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan nilai node
        self.right = None  # Child Kiri
        self.left = None  # Child Kanan


# Membuat sebuah Node root
root = Node("A")

# Membuat Child Level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child Level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi node
print("Data pada root:", root.data)
print("Child kiri root:", root.left.data)
print("Child kanan root:", root.right.data)
print("Child kiri dari B:", root.left.left.data)
print("Child kanan dari B:", root.left.right.data)

# Lanjutkan kode programnya untuk keseluruhan tree
# Tambahkan child di sisi kanan (C) dengan node F dan G
root.right.left = Node("F")
root.right.right = Node("G")
print("Child kiri dari C:", root.right.left.data)
print("Child kanan dari C:", root.right.right.data)

# Penjelasan ...............
# Hierarki ini bisa diperdalam. Contohnya, disini sudah sampai level 2,
# yang berarti node paling bawahnya adalah sekitar 2 kali penurunan dari root.
# Jadi, kita bisa turun secukupnya selama ada parent yang sesuai.
