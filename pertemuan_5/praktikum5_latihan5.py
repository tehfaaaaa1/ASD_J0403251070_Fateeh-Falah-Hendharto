"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""


# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    "Membuat PIN"
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


def modified_buat_pin(panjang, hasil=""):
    "Membuat PIN dengan set supaya tidak mengulang karakter yang sama."
    if len(hasil) == panjang:
        print("PIN:", "".join(map(str, set(hasil))))
        return
    for angka in ["0", "1", "2"]:
        modified_buat_pin(panjang, hasil + angka)


modified_buat_pin(3)

# 1. Input digit kombinasi yang diinginkan (n)
# 2.
