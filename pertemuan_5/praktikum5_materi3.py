"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""

# ==========================================
# Implementasi: Rekursif
# Case: Menghitung jumlah dalam list
# Recursive case => 1 + 2 + 3 + n
# Base case => sampai akhir list
# ==========================================


def jumlah_list(n, index=0):
    "Menghitung/tracing cara kerja rekursif"
    if index == len(n):  # Base case: Sampai akhir list
        return 0

    return n[index] + jumlah_list(n, index+1)  # Loop setiap elemen dalam list, lalu dijumlahkan


print(jumlah_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
