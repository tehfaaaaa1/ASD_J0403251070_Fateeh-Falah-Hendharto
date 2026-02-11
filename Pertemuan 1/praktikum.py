""" 
Praktikum 1: Konsep ADT dan File Handling
Latihan Dasar 1A: Membaca seluruh isi file
"""

# Membuka file dengan mode read ("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("=== Hasil Read ===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter:", len(isi_file))
print("Jumlah Baris:", isi_file.count("\n") + 1)

# Membuka file per baris
print("=== Membaca file per baris ===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        print("Baris ke-", jumlah_baris)
        print("Isi:", baris)

# Latihan Dasar 2: Parsing baris menjadi kolom data
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        print(f"NIM: {nim} | Nama: {nama} | Nilai: {nilai}")

# Latihan Dasar 3: Membaca file dan simpan ke list
data_list = []
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        data_list.append([nim,nama,int(nilai)])

print("=== Data mahasiswa dalam List ===")
print(data_list)
print("=== Jumlah data dalam List ===")
print(len(data_list))
print("=== Menampilkan data row dalam List ===")
print(data_list[0])

# Latihan Dasar 4: Membaca file dan simpan ke dict
data_dict = {}
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }
print("=== Data mahasiswa dalam Dict ===")
print(data_dict)
