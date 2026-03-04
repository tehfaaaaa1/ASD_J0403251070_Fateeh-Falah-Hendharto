"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

# 1. Mengapa perulangan dimulai dari indeks 1?
# 2. Apa fungsi variabel key?
# 3. Mengapa digunakan while, bukan for?
# 4. Operasi apa yang terjadi di dalam while?
# =============================================
# 1. Karena index 0 akan digunakan sebagai perbandingan
# serta mempercepat algoritma dengan menghapus satu langkah
# 2. Sebagai elemen yang ingin disisipkan
# 3. Karena ketidakpastian dalam jumlah data
# 4. Menggeserkan elemen sebelum key ke index selanjutnya.
# Lalu, turun index j ke bawah sekali.
