"""
==========================================
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
==========================================
"""


# ========================================
# Insertion Sort (Tracing Output)
# ========================================
def insertion_sort(data):
    "Insertion Sort Simulation"

    # Melihat data awal
    print("Data Awal: ", data)
    print("=" * 20)

    # Loop
    for i in range(1, len(data)):
        key = data[i]  # Simpan nilai yang disisipkan
        j = i - 1  # Index elemen terakhir di bagian kiri

        print("Iterasi ke-", i)
        print("Nilai key: ", key)
        print("Bagian kiri (sorted): ", data[:i])
        print("Bagian kanan (unsorted): ", data[i:])

        # Geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1

        # Sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan: ", data)
        print("=" * 20)
    return data


angka = [7, 8, 5, 2, 4, 6]
print("Hasil Insertion Sort: ", insertion_sort(angka))
