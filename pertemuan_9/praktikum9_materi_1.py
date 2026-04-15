"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1

Latihan 1 : Membuat Node Tree
"""


class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan nilai node
        self.right = None  # Child Kiri
        self.left = None  # Child Kanan


root = Node("A")
root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

print("Data pada root:", root.data)
print("Child kiri root:", root.left.data)
print("Child kanan root:", root.right.data)

# Penjelasan ...............
# Dengan data LinkedList, kita bisa memperluas data kita menjadi hierarki.
# Hierarki ini disebut dengan "Tree". Pada Tree ini terdapat node2 yang saling berhubungan,
# di antaranya adalah Parent (atasan) dan Child (bawahan).
# Root sendiri adalah node paling atas alias Adam dalam data tree.
# Jadi, strukturnya seperti berikut:
# Root (Parent)
# |- Child
# |-- Grandchild
# |- Child
# Pemakaiannya menggunakan variable left dan right seperti
# next dan previous dalam Double Linked List.
