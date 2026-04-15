"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1

Latihan 3 : Membuat Traversal Preorder
"""


class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan nilai node
        self.right = None  # Child Kiri
        self.left = None  # Child Kanan


# Membuat Fungsi Preorder: root -> left -> right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Membuat sebuah Node root
root = Node("A")

# Membuat Child Level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child Level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi node
print("Hasil Traversal Preorder:")
preorder(root)

# Penjelasan ...............
# Traversal adalah metode penyelusuruan sebuah struktur tree.
# Caranya adalah pemanggilan rekursif. Dengan rekursif, kita bisa menggali
# hingga node paling bawah dimulai dari tempat yang kita pilih.
# Contohnya dengan preorder, kita memulai dari root tree ke node bawah.
# Output dengan kode di atas: A B D E C
# Disini, alurnya dari root, lalu ke node paling kiri-bawah, dan mengakhiri
# di node kanan-bawah sebelum melanjutkan ke sebelah kanan parent / sibling.
# Subtree: Tree tertentu
# Sibling: Node se-level & se-parent
