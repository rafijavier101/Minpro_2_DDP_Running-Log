# Minpro_2_DDP_Running-Log

Nama : Rafi Javier Maulana

NIM  : 2609116050

kode progran yang saya buat berfungsi untuk menambahkan, mengubah, menghapus, membaca sekumpulan data dengan tema Running log atau riwayat lari. Dalam kode tersebut user akan dibagi ke dalam dua role yaitu user dan viewer. pada role user, kita dapt melakukan CRUD, sedangkan di role viewer hanya bisa membaca/lihat data yang sudah ada.

<img width="1280" height="800" alt="pafa9vmett" src="https://github.com/user-attachments/assets/7163c4e9-9a4e-4e0b-b19e-c5a4f158a223" />

Penjelasan alur flowchart

user akan menginput username dan pw jika username dan pw benar maka akan masuk ke role user jika salah akan masuk ke role viewer

jika masuk role VIEWER:

akan ada menu pilihan dan bisa melilih antara 1-3
   jika pilihan = 1 maka user akan mendapat tampilan data running log yang sudah ada. Jika running log kosong maka akan kembali ke menu.

   jika pilihan = 2 maka user akan log out dan kembali ke tampilan input username dan pw

   jika pilihan = 3 maka user akan menghentikan program

jika masuk role USER:

akan ada menu pilihan dan bisa memilih antara 1-6
  jika pilihan = 1 maka user akan menginput data dari running loh (Hari,Lokasi,Jarak)
  jika pilihan = 2 maka user akan bisa mengubah data running log yang sudah ada. Pertama user akan ditampilkan seluruh running log yang ada, lalu user dapat memilih running log mana yang mau di ubah, setelah memilih user akan menginput data baru. jika data kosong maka akan kembali ke menu awal.
  jika pilihan = 3 maka user akan bisa menghapus data running log yang ada. Pertama user akan ditampilkan seluruh running log yang ada, lalu user dapat memilih running log mana yang mau di hapus, setelah memilih data yang dipilih akan terhapus. Jika data kosong maka akan kembali ke menu awal.
  jika pilihan = 4 maka user akan mendapat tampilan data running log yang sudah ada. Jika running log kosong maka akan kembali ke menu.
  jika pilihan = 5 maka user akan log out dan kembali ke tampilan input username dan pw
  jika pilihan = 6  maka user akan menghentikan program

