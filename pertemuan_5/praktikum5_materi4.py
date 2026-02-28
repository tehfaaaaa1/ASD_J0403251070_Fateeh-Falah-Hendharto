"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""


# ===========================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# 1. Input digit biner yang diinginkan (n)
# 2. Panggil function sendiri, mulai dari hasil = 0
# 3. Ulangi kode program dari line 24 dan print jika sampai base case. Cth: 00
# 4. Karena alur berhenti, balik ke atas. Jadi balik ke 0
# 5. Lanjut ke baris berikutnya (30), yaitu + 1. Output: 01.
# 6. Alur sudah selesai, baru keluar dari hasil awal 0 (line 28) ke 1 (line 30)
# 7. Ulangi sampai semua kombinasi telah dicoba
# ===========================================
def biner(n, hasil=""):
    "n: jumlah digit biner. hasil: output biner."
    # Base case: Jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")
    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")


biner(3)
