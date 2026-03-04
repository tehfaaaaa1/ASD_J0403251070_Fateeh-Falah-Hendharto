"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
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


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # Soal No. 1
        # if __________________________:
        # ===============================
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Soal:
# 1. Lengkapi kondisi agar menjadi ascending.
# 2. Jelaskan fungsi result.extend().
# ==========================================
# 1. if left[i] < right[j]:
# 2. Menggabungkan dua list. Bedanya dengan append
# adalah extend merupakan penggabungan antara 2 list (termasuk list kosong),
# sedangkan append adalah penggabungan sebuah data ke dalam list.
