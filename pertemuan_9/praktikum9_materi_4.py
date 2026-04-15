"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1

Latihan 4 : Membuat Traversal Inorder
"""


class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan nilai node
        self.right = None  # Child Kiri
        self.left = None  # Child Kanan


# Membuat Fungsi Inorder: left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# Membuat sebuah Node root
root = Node("A")

# Membuat Child Level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child Level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi node
print("Hasil Traversal Inorder:")
inorder(root)

# Penjelasan ...............
# Traversal adalah metode penyelusuruan sebuah struktur tree.
# Caranya adalah pemanggilan rekursif. Dengan rekursif, kita bisa menggali
# hingga node paling bawah dimulai dari tempat yang kita pilih.
# Contohnya dengan inorder, kita memulai dari kiri-bawah tree ke node atas.
# Output dengan kode di atas: D B E A C
# Disini, titik awalnya node paling kiri-bawah, lalu ke node parent, dan mengakhiri
# di node kanan-bawah sebelum melanjutkan ke parent.
# Subtree: Tree tertentu
