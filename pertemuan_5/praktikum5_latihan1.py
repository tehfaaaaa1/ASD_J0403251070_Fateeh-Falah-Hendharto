"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================


def pangkat(a, n):
    "Function Pangkat"
    # Base case: Berhenti jika sampai eksponen 0
    if n == 0:
        return 1
    # Recursive case: Rekursi a * (a * eksponen (n))
    return a * pangkat(a, n - 1)


print(pangkat(2, 4))  # Output: 16
# 2 * (2 * (2 * (2 * 1)))
# 2 * (2 * (2 * 2))
# 2 * (2 * 4)
# 2 * 8
# 16
