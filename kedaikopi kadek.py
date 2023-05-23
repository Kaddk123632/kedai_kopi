class AnandaCoffee:
    def __init__(self):
        self.__menu = {
            "a": {"nama": "ES Kopi Susu", "harga": 11000},
            "b": {"nama": "ES Kopi Coklat", "harga": 12000},
            "c": {"nama": "ES Kopi Hitam", "harga": 11000},
            "d": {"nama": "Ice Americano", "harga": 14000}
        }

    def hitung_total_harga(self, pesanan, jumlah):
        if pesanan in self.__menu:
            harga = self.__menu[pesanan]["harga"]
            total_harga = harga * jumlah
            return total_harga
        else:
            return None

    def cetak_pesanan(self, pesanan, jumlah, total_harga):
        if pesanan in self.__menu:
            nama = self.__menu[pesanan]["nama"]
            print("Ananda Coffee")
            print("--------------")
            print("Pesanan: ", nama)
            print("Jumlah: ", jumlah)
            print("Total Harga: ", total_harga)
            print("--------------")


pilihan = "y"
ananda_coffee = AnandaCoffee()

while pilihan == "y":
    print("""
    ==============================
    
    Ananda Coffee
    List Menu Minuman Kopi
 
    ==============================
    A. ES Kopi Susu : Rp 11.000
    B. ES Kopi Coklat : Rp 12.000
    C. ES Kopi Hitam : Rp 11.000
    D. Ice Americano : Rp 14.000
    ==============================
    """)
    pesan = input("Masukkan kode menu kopi yang dipilih = ")
    jumlah_pesan = int(input("Masukkan jumlah pesanan = "))

    total_harga = ananda_coffee.hitung_total_harga(pesan, jumlah_pesan)

    if total_harga is not None:
        ananda_coffee.cetak_pesanan(pesan, jumlah_pesan, total_harga)
    else:
        print("Menu tidak tersedia.")

    pilihan = input("Apakah Anda ingin memesan kembali? (y/n) ")

print("Terima kasih telah menggunakan layanan Ananda Coffee.")