class Buku:
  def _init_(self, judul, pengarang, tahun_terbit):
    self.judul = judul
    self.pengarang = pengarang
    self.tahun_terbit = tahun_terbit

class Peminjam:
  def _init_(self, nama, alamat):
    self.nama = nama
    self.alamat = alamat

class Transaksi:
  def _init_(self, buku, peminjam, tanggal_pinjam, tanggal_kembali):
    self.buku = buku
    self.peminjam = peminjam
    self.tanggal_pinjam = tanggal_pinjam
    self.tanggal_kembali = tanggal_kembali

  def hitung_biaya_keterlambatan(self):
    denda = 0
    selisih_hari = (self.tanggal_kembali - self.tanggal_pinjam).days
    if selisih_hari > 7:
      denda = (selisih_hari - 7) * 5000
    return denda

# Contoh penggunaan
buku1 = Buku ("peminjam buku", ("Guido van Rossum", 2007))
peminjam1 = Peminjam ("Budi", "Malang")
transaksi1 = Transaksi (buku1, peminjam1,"datetime_date(2024, 5, 1), datetime_date (2024, 6, 4")

print("Judul Buku:", transaksi1.buku.judul)
print("Nama Peminjam:", transaksi1.peminjam.nama)
print("Tanggal Pinjam:", transaksi1.tanggal_pinjam)
print("Tanggal Kembali:", transaksi1.tanggal_kembali)
print("Biaya Keterlambatan:", transaksi1.hitung_biaya_keterlambatan)