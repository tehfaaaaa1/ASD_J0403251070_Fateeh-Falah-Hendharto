"""Useful snippets. Experimental."""

def create(filename, data):
    """
    Membuat barang baru ke database.\n
    filename = nama file yang berisi data.\n
    data = variabel dictionary data yang sudah di-fetch
    """
    new_product = input("Masukkan nama produk: ").strip()
    *_, last_id = data.keys()
    try:
        new_stock = int(input("Masukkan stok barang: "))
    except ValueError:
        print("Input harus bilangan!")
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(
            f"\nBRG{int(last_id.lstrip('BRG'))+1},{new_product},{new_stock}"
            )
    print("Produk berhasil ditambah!")