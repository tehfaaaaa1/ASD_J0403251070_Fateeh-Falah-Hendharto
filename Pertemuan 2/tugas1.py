"""
=============================================================
TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)

# Nama : Fateeh Falah Hendharto
# NIM :J0403251070
# Kelas : B1
=============================================================
"""

# -------------------------------
# Konstanta nama file
# -------------------------------
FILENAME = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def fetch(filename):
    "Fetch data dari file. filename = nama file termasuk ekstensi."
    # Buka file
    with open(filename, 'r', encoding='utf-8') as file:
        data_dict = {}
        # Loop setiap baris di file
        for row in file:
            row = row.strip()
            id_barang, nama_barang, stok_barang = row.split(',')
            # Save ke dictionary
            data_dict[id_barang] = {
                "nama_barang": nama_barang,
                "stok_barang": stok_barang
            }
    return data_dict

# Menu functions
# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def show(data):
    "Tunjukkan list semua data. data = variabel dictionary data yang sudah di-fetch."
    # Check if empty
    if len(data) == 0:
        print("Data kosong.")

    print("=== List Data ===")
    thead = f"{'ID': <6} | {'Barang': <25} | {'Stok': <3}"
    print(thead)
    print('-' * len(thead))
    for row in data.keys():
        print(f"{row: <6} | {data[row]['nama_barang']: <25} | {data[row]['stok_barang']: <3}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def search(data):
    "Cari data yang diinginkan. data = variabel dictionary data yang sudah di-fetch."
    result = input("Ketik kode barang: ").strip().upper()
    # If not found
    if result not in data:
        print("Barang tidak ditemukan!")

    print("Info Barang:")
    print(f"ID\t: {result}")
    print(f"Produk\t: {data[result]['nama_barang']}")
    print(f"Stok\t: {data[result]['stok_barang']}")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def create(data):
    """
    Membuat barang baru ke database.\n
    filename = nama file yang berisi data.\n
    data = variabel dictionary data yang sudah di-fetch.
    """
    # Input
    new_product = input("Masukkan nama produk: ").strip()
    # last_id = ambil angka ID terakhir
    # Untuk membuat ID baru berdasarkan ID terakhir. Auto-increment.
    if len(data) == 0:
        last_id = "BRG1"
    else:
        *_, last_id = data.keys()
        last_id = "BRG" + str((int(last_id.lstrip('BRG')) + 1))
    # Check ValueError
    try:
        new_stock = int(input("Masukkan stok barang: "))
    except ValueError:
        print("Masukkan angka saja!")

    # Save and print output
    data[last_id] = {"nama_barang": new_product, "stok_barang": new_stock}
    print("Produk berhasil ditambah!")

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update(data):
    "Update data dalam file. data = variabel dictionary data yang sudah di-fetch."
    id_input = input("Masukkan kode barang: ").strip().upper()
    # If not found
    if id_input not in data:
        print("Produk tidak ditemukan!")

    print("Produk ditemukan:")
    print(f"ID\t: {id_input}")
    print(f"Produk\t: {data[id_input]['nama_barang']}")
    print(f"Stok\t: {data[id_input]['stok_barang']}")
    update_barang = input("Masukkan produk baru\t\t: ").strip()
    # Check ValueError
    try:
        update_stock = input("Masukkan stok produk baru\t: ").strip()
    except ValueError:
        print("Masukkan angka saja!")

    print(f"Barang\t: {data[id_input]['nama_barang']} -> {update_barang}")
    print(f"Stok\t: {data[id_input]['stok_barang']} -> {update_stock}")
    data[id_input] = {
        "nama_barang": update_barang,
        "stok_barang": update_stock
    }
    print("Data berhasil diubah!")

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def save(filename, data):
    """
    Menyimpan data ke database.\n
    filename = nama file termasuk ekstensi.\n
    data = variabel dictionary data yang sudah di-fetch.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        # "Write" setiap baris data satu persatu
        for row in sorted(data.keys()):
            file.write(f"{row},{data[row]['nama_barang']},{data[row]['stok_barang']}\n")
    print("Data berhasil disimpan!")

# -------------------------------
# Program Utama
# -------------------------------
def main():
    "Main program."
    data = fetch(FILENAME)

    while True:
        print("\nTARGET WAREHOUSE")
        print("==================")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar dari program")

        # Memilih menu dan menjalankan functions
        match int(input("Pilih menu di atas: ")):
            case 1:
                show(data)
            case 2:
                search(data)
            case 3:
                create(data)
            case 4:
                update(data)
            case 5:
                save(FILENAME, data)
            case 0:
                print("Exit dari program...")
                return
            case _: # Default
                print("Masukkan angka saja!")

# Menjalankan program utama
if __name__ == "__main__":
    main()
