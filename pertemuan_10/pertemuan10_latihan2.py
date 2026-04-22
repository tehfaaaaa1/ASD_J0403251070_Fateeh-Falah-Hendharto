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


# Insert Data untuk BST
# ===============================
def insert(root, data):
    "Insert Node baru dalam suatu tree"
    # Jika rootnya kosong, insert node baru
    if not root:
        return Node(data)

    # Jika data baru lebih kecil dari data root, masukkan ke branch kiri
    if data < root.data:
        root.left = insert(root.left, data)

    # Jika data baru lebih kecil dari data root, masukkan ke branch kanan
    elif data > root.data:
        root.right = insert(root.right, data)

    # Jika data sama persis, jangan insert
    return root


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


# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    "Menampilkan struktur tree"
    if root:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


# Program Utama
# Ini menunjukkan kenapa pure BST bisa tidak efisien,
# Karena BST mulai condong ke kanan atas banyaknya data
# Yang lebih besar dari rootnya. Jadi, semakin panjang tree ini,
# pencarian bisa semakin lambat.
ROOT = None
data_list = [10, 20, 30]
for value in data_list:
    ROOT = insert(ROOT, value)

print("Preorder BST:")
preorder(ROOT)

print("\n\nStruktur BST:")
tampil_struktur(ROOT)
