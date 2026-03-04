"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""


# def insertion_sort(data):
#     for i in range(1, len(data)):
#         key = data[i]
#         j = i - 1
#         while j >= 0 and ______________________:
#         data[j + 1] = data[j]
#         j -= 1
#         ______________________
#     return data

# 1. Lengkapi kondisi agar menjadi sorting ascending.
# 2. Ubah agar menjadi descending.
# ====================================================
# 1.
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j+1] = key
    return data


# 2.
def insertion_sort_descend(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1
        data[j+1] = key
    return data


angka = [5, 6, 1, 2, 10, 7]
print("Insertion Sort Ascending  : ", insertion_sort(angka))
print("Insertion Sort Descending : ", insertion_sort_descend(angka))
