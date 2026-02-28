"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""


# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
    "Kombinasi Huruf"
    if len(hasil) == n:
        print(hasil)
        return
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")


kombinasi(2)

# 1. Input digit kombinasi yang diinginkan (n)
# 2. Panggil function sendiri, mulai dari hasil = A
# 3. Ulangi kode program dari line 24 dan print jika sampai base case. Cth: AA
# 4. Karena alur berhenti, balik ke struktur atas. Jadi balik ke A
# 5. Lanjut ke baris berikutnya (19), yaitu + B. Output: AB.
# 6. Alur sudah selesai, baru keluar dari hasil awal A (line 18) ke B (line 19)
# 7. Ulangi sampai semua kombinasi telah dicoba

# Flow:
# A  -- Line 18
# AA -- Line 18. Base case, yaitu panjang hasil sama dengan n.
# AB -- Line 19
# B  -- Line 19
# BA -- Line 18
# BB -- Line 19
