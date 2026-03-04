"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""


# ========================================
# Merge Sort Tracing
# ========================================
def merge_sort(data, depth=0):
    "Merge Sort Algorithm"

    indent = " " * depth
    print(f"{indent}merge_sort({data})")

    # Base call / Error handling
    if len(data) <= 1:
        return data

    # Divide: Membagi data menjadi 2 bagian
    mid = len(data)//2
    left = data[:mid]  # Slicing bagian kiri
    right = data[mid:]  # Slicing bagian kanan

    print(f"{indent}divide -> left = {left} | right = {right}")

    # Recursive Call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge -> {left_sorted} + {right_sorted} = {merged}")

    return merged


def merge(left, right):
    "Merge Sort Merger"
    result = []
    i = j = 0

    # Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])
    return result


angka = [13, 8, 28, 5, 19, 36, 4]
print("Hasil Sorting: ", merge_sort(angka))
