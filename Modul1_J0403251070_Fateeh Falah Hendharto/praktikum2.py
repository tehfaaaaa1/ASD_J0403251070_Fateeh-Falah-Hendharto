""" 
Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
"""

# Latihan 1: Membuat fungsi load data
NAMA_FILE = "data_mahasiswa.txt"
def read_data(filename):
    "Fungsi untuk membaca  data. filename = file data mahasiswa. Return data sebagai dictionary."
    data_dict = {}
    with open(filename, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(', ')
            data_dict[nim] = {
                "nama": nama,
                "nilai": int(nilai)
            }
    return data_dict

# data_mhs = read_data(NAMA_FILE)
# print("=== Data mahasiswa ===")
# print(f"Mendapatkan {len(data_mhs)} baris")

# Latihan 2: Membuat fungsi load data
def show_data(data):
    "Membuat fungsi load data. Param data = dictionary "
    if len(data) == 0:
        print("Data kosong")
        return
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM': <10} | {'Nama': <12} | {'Nilai': >5}")
    # <10 = 10 char terawal
    # >5 = 5 char terakhir
    print("-" * 33)

    for nim in sorted(data.keys()):
        nama = data[nim]['nama']
        nilai = data[nim]['nilai']
        print(f"{nim: <10} | {nama: <12} | {nilai: >5}")

# show_data(data_mhs)

# Latihan 3: Mencari data
def search_data(data):
    "Fungsi mencari data. data = data yang telah di-fetch."
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data:
        nama = data[nim_cari]['nama']
        nilai = data[nim_cari]['nilai']

        print("\n=== Mahasiswa Ditemukan ===")
        print(f"NIM\t: {nim_cari}")
        print(f"Nama\t: {nama}")
        print(f"Nilai\t: {nilai}")
    else:
        print("Mahasiswa tidak ditemukan")

# search_data(data_mhs)

# Latihan 4: Update data
def update_data(data):
    "Update data. data = data yang telah di-fetch."
    nim = input("Masukkan NIM mahasiswa yang nilainya akan diubah: ").strip()

    if nim not in data:
        print("Mahasiswa tidak ditemukan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru: "))
    except ValueError:
        print("Masukkan nilai dengan bilangan!")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus di antara 0 - 100 !!")
    else:
        print(f"Nilai {data[nim]['nilai']} --> {nilai_baru}")
        data[nim]['nilai'] = nilai_baru
        print("Data berhasil diubah!")

# update_data(data_mhs)

# Latihan 5: Simpan perubahan data ke file
def save_data(filename, data):
    """
    Simpan perubahan data ke file.\n
    filename = nama file yang akan digunakan untuk save\n
    data = data yang telah di-fetch.
    """
    with open(filename, "w", encoding="utf-8") as file:
        for nim in sorted(data.keys()):
            nama = data[nim]["nama"]
            nilai = data[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai}\n")
        print("Data berhasil disimpan!")

# save_data(NAMA_FILE, data_mhs)
# print("Data berhasil disimpan!")

def main():
    "Menu program dashboard program mahasiswa."
    # Fungsi load data
    open_data = read_data(NAMA_FILE)

    while True:
        print("\n=== Mahasiswa Program ===")
        print("1. Show data")
        print("2. Search mahasiswa")
        print("3. Update data")
        print("4. Save perubahan")
        print("0. Keluar")

        match int(input("Pilih menu: ")):
            case 1:
                show_data(open_data)
            case 2:
                search_data(open_data)
            case 3:
                update_data(open_data)
            case 4:
                save_data(NAMA_FILE, open_data)
            case 0:
                print("Exit dari program!")
                return
            case _:
                print("Pilih menu yang valid!")

main()
