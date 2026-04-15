"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1

Latihan 5 : Membuat Traversal Postorder
"""


class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan nilai node
        self.right = None  # Child Kiri
        self.left = None  # Child Kanan


# Membuat Fungsi Postorder: right -> left -> root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# Membuat sebuah Node root
root = Node("A")

# Membuat Child Level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child Level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi node
print("Hasil Traversal Postorder:")
postorder(root)

# Penjelasan ...............
# Traversal adalah metode penyelusuruan sebuah struktur tree.
# Caranya adalah pemanggilan rekursif. Dengan rekursif, kita bisa menggali
# hingga node paling bawah dimulai dari tempat yang kita pilih.
# Contohnya dengan postorder, kita memulai dari kanan-bawah tree ke node sebelah.
# Output dengan kode di atas: D E B C A
# Disini, titik awalnya node kanan di tree paling kiri-bawah, lalu ke node sibling, dan
# mengakhiri di node parent sebelum melanjutkan ke sebelah kanan parent / node sibling.
# Subtree: Tree tertentu
# Sibling: Node se-level & se-parent
