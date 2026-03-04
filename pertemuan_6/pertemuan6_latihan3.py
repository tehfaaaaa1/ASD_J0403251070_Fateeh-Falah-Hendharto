"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""

# Buat program dengan menggunakan algoritma insertion sort
# Tracing dengan data = [5, 2, 4, 6, 1, 3]

angka = [5, 2, 4, 6, 1, 3]


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j+1] = key

        # 1.
        if i == 1:
            print("Iterasi i = 1: ", data)
        # 2.
        if i == 3:
            print("Iterasi i = 3: ", data)
    return data


print("Data Awal: ", angka)
print("Data Akhir: ", insertion_sort(angka))

# Soal:
# 1. Tuliskan isi list setelah iterasi i = 1.
# 2. Tuliskan isi list setelah iterasi i = 3.
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4?
# =======================================================
# 1. [2, 5, 4, 6, 1, 3]
# 2. [2, 4, 5, 6, 1, 3]
# 3. 4 kali. Bergeser ke paling kiri: 4 Langkah
