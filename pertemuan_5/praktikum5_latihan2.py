"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""

# =========================================================
# Latihan 2: Tracing Rekursi
# =========================================================


def countdown(n):
    "Tracing dari n sampai 0, lalu kembali ke n"
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)


countdown(3)
# Mengapa output 'Keluar' muncul terbalik?
# Karena setelah baris 20 (countdown call) selesai, akhirnya dia pindah ke panggilan
# baris selanjutnya, yaitu print 'Keluar'.
# Misal berhenti di 0, lalu dia keluar dari function-nya dan panggil:
# Keluar: 1. Setelah selesai running, balik ke struktur atasnya dan ulangi output.
