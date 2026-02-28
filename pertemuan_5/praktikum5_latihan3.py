"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""
# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================


def cari_maks(data, index=0):
    "Fungsi untuk mencari bilangan tertinggi dalam list"
    # Base case: Berhenti jika sampai index terakhir. Return elemen terakhir dalam list
    if index == len(data) - 1:
        return data[index]
    # Recursive case: Loop ke semua elemen
    maks_sisa = cari_maks(data, index + 1)
    if data[index] > maks_sisa:
        return data[index]

    return maks_sisa


angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))
# 3
# 7
# 2
# 9
# 5
# Ke atas lagi
# maks_sisa = 5
# 9 > 5 -> True
# 2 > 9 -> False
# 7 > 9 -> False
# 3 > 9 -> False
# return 9
