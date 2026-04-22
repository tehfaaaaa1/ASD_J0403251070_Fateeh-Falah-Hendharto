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


def rotate_left(old_root):
    "Menukar secara counter-clockwise / kanan-kiri"
    y = old_root.right  # y = cabang kanan root lama
    y_left = y.left     # y_left = cabang kiri dari y

    # Pokoknya diputarkan jadi root lama berada di
    # cabang kanan -> kiri. Lalu, cabang kanan root
    # ditukar dengan value cabang kanan -> kiri jika ada.
    # Return cabang kanan root.
    y.left = old_root
    old_root.right = y_left

    return y


# Program Utama
# ===============================

# Diawali dengan membuat tree tidak seimbang.
ROOT = Node(10)
ROOT.right = Node(20)
ROOT.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(ROOT)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(ROOT)

# Melakukan rotasi kiri pada root
ROOT = rotate_left(ROOT)

print("\nPreorder sesudah rotasi kiri")
preorder(ROOT)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(ROOT)
