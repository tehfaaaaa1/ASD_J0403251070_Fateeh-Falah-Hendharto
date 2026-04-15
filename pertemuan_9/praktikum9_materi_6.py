"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1

Latihan 6 : Struktur Organisasi Perusahaan
"""


class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan nilai node
        self.right = None  # Child Kiri
        self.left = None  # Child Kanan


# Membuat Fungsi Preorder: root -> left -> right
def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


# Membuat sebuah Node root
root = Node("Direktur")

# Membuat Child Level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Membuat Child Level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.right = Node("Staff 3")

# Traversal
print("Struktur Organsisasi A:")
preorder(root)

# Penjelasan ...............
# Pada suatu hari, ada seseorang bernama Direktur yang memiliki
# 2 anak, yaitu Manajer A dan Manajer B. Mereka berdua juga memiliki
# anak sendiri. Anaknya Manajer A ada Staff 1 dan Staff 2, sedangkan
# Anaknya Manajer B ada Staff 3. Keluarga ini hidup tentram dalam satu perumahan.
