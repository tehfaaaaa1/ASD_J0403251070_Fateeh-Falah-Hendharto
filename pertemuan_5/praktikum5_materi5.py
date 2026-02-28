"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""


# =================================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# Menghentikan eksplorasi cabang yang pasti tidak memenuhi syarat
# 1. Input digit biner yang diinginkan (n)
# 2. Panggil function sendiri, mulai dari hasil = 0
# 3. Ulangi kode program dari line 25 dan print jika sampai base case. Cth: 00
# 4. Karena alur berhenti, balik ke atas. Jadi balik ke 0
# 5. Lanjut ke baris berikutnya, yaitu + 1. Output: 01.
# 6. Alur sudah selesai, baru keluar dari hasil awal 0 ke 1
# 7. Ulangi sampai semua kombinasi telah dicoba
# 8. Jika jumlah biner 1 melewati batas, maka tidak akan output
# =================================================================
def biner_atas(n, batas, hasil="", jumlah=0):
    "Pruning method untuk backtracking"
    # Pruning/pembatasan
    if jumlah > batas:
        return

    # Base case
    if len(hasil) == n:
        print(hasil)
        return

    # Pilih 0
    biner_atas(n, batas, hasil + "0", jumlah)

    # Pilih 1
    biner_atas(n, batas, hasil + "1", jumlah + 1)


biner_atas(4, 2)
