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


# Latihan 1: Insert Data
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


# Testing
NODE_ROOT = None
data_list = [50, 30, 70, 20, 40, 60, 80]
for value in data_list:
    NODE_ROOT = insert(NODE_ROOT, value)

print(NODE_ROOT.data)


# Latihan 2 : Traversal Inorder
# ===============================
def inorder(root):
    """
    Traversal tree dengan teknik Inorder
    Menggunakan rekursif supaya sampai ke cabang paling kiri-bawah,\n
    lalu bergerak ke kanan dan ke root sebelum mulai lagi dari subtree selanjutnya.
    """
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


print("Hasil Traversal Inorder:")
inorder(NODE_ROOT)


# Latihan 3 : Search
# ===============================
def search(root, key):
    "Mencari data dalam Binary Tree"
    # Jika root kosong, hentikan function
    if not root:
        return False

    # Jika data node sama dengan key, return True
    if root.data == key:
        return True

    # Jika key lebih kecil dari root data, cari di branch kiri
    if key < root.data:
        return search(root.left, key)

    # Jika key lebih besar dari root data, cari di branch kanan
    return search(root.right, key)


TEST_KEY = 40
print(f"Data ditemukan: {TEST_KEY}" if search(
    NODE_ROOT, TEST_KEY) else "Data tidak ditemukan")
