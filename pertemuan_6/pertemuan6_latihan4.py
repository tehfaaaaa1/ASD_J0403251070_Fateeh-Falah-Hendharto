"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
Note to self: Don't run program. For study purposes. Will result in error
"""


def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

# Soal:
# 1. Apa yang dimaksud dengan base case?
# 2. Mengapa fungsi memanggil dirinya sendiri?
# 3. Apa tujuan fungsi merge()?
# ===============================================
# 1. Kondisi berakhirnya recursive
# 2. Untuk melakukan recursive call
# 3. Menggabungkan dua data yang terpisah
