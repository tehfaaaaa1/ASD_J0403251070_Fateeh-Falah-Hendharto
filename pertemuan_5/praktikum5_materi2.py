"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""

# ==========================================
# Implementasi: Rekursif
# Case: Call Stack (Tracing bilangan masuk/keluar)
# Recursive case => 3-2-1 | 1-2-3
# Base case => 0 berhenti
# ==========================================


def hitung(n):
    "Tracing bilangan dari awal eksekusi sampai akhir"
    if n == 0:  # Base case
        print("Selesai menghitung.")
        return

    # Recursive Case
    print("Masuk: ", n)
    hitung(n-1)
    print("Keluar: ", n)


print(hitung(5))
