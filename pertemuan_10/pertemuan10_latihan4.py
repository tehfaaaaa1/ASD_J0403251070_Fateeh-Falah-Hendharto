"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1

Materi  : Binary Search Tree & AVL Tree
"""

from dataclasses import dataclass


@dataclass  # Wrapper function untuk Node, experimental
class Node:
    "Node Binary Tree"
    data: any  # Isi data node
    left: "Node" = None  # Branch kiri tree
    right: "Node" = None  # Branch kanan tree


# Traversal Preorder
# ===============================
def preorder(root):
    """
    Traversal tree dengan teknik Preorder
    Menggunakan rekursif supaya sampai di root,\n
    lalu bergerak ke cabang kiri dan ke cabang kanan sebelum mulai lagi dari subtree selanjutnya.
    """
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


# Tampilkan struktur tree
# ===============================
def tampil_struktur(root, level=0, posisi="Root"):
    "Tampilkan struktur tree"
    if root:
        print("\t" * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


def rotate_right(old_root):
    "Menukar secara clockwise / kiri-kanan"
    y = old_root.left  # y = cabang kanan root lama
    y_right = y.right     # y_right = cabang kiri dari y

    # Pokoknya diputarkan jadi root lama berada di
    # cabang kiri -> kanan. Lalu, cabang kiri root
    # ditukar dengan value cabang kiri -> kanan jika ada.
    # Return cabang kiri root.
    y.right = old_root
    old_root.left = y_right

    return y


# Program Utama
# ===============================

# Diawali dengan membuat tree tidak seimbang.
ROOT = Node(10)
ROOT.left = Node(20)
ROOT.left.left = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(ROOT)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(ROOT)

# Melakukan rotasi kanan pada root
ROOT = rotate_right(ROOT)

print("\nPreorder sesudah rotasi kiri")
preorder(ROOT)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(ROOT)
