"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""

# ==========================================
# Implementasi: Rekursif
# Case: Faktorial
# Recursive case => 5 * 4 * 3 * 2 * 1
# Base case => 0 berhenti
# ==========================================


def faktorial(n):
    "Faktorial function"
    if n == 0:  # Base case
        return 1
    return n * faktorial(n-1)  # Rekursif case


print(faktorial(5))
