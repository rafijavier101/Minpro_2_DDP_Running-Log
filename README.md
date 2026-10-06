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

<img width="1280" height="800" alt="Code_IqOitd5pNJ" src="https://github.com/user-attachments/assets/59d97b69-595e-4d9e-aedd-c3d0381e565a" />
<img width="1280" height="800" alt="Code_I0KrcIvgtl" src="https://github.com/user-attachments/assets/70a8068d-eb7f-4fd3-a624-99c1d83caa95" />

1. kode dibawa adalah data awal, username dan pw yang benar, serta library.
<img width="232" height="50" alt="data" src="https://github.com/user-attachments/assets/69e3c669-4d70-40a1-9e6d-877ec18f0073" />

2. kode dibawah merupakan function yang dapat ditanggil lagi oleh barisan kode dibawahnya, berfungsi untuk menambahkan data baru.
<img width="369" height="178" alt="tambahcode" src="https://github.com/user-attachments/assets/d2c8856c-b7e8-4419-ba17-dc9d41e0821b" />

Tambahan: 

while True:

        try:
            jarak = float(input("Berapa kilometer kamu berlari? : "))
            if jarak < 0:
                print("JARAK LARI TIDAK VALID")
                continue
            break
        except ValueError:
            print("JARAK LARI HARUS BERUPA ANGKA")

   berfungsi agar sistem tidak crash dengan cara: jika user input value selain angka pada input jarak, maka sistem akan kembali ke input jarak sampai user menginput jarak dengan format yang benar.

Output:

<img width="252" height="140" alt="TerTambah" src="https://github.com/user-attachments/assets/d9d5093c-86cb-40c2-b01a-43d9040304a6" />

3. kode dibawah merupakan function yang dapat dipanggil lagi oleh barisan kode dibawahnya, berfungsi untuk mengubah data yang sudah ada.
<img width="388" height="371" alt="ubahcode" src="https://github.com/user-attachments/assets/cbda1024-0fe0-4e78-ab5f-50b66ddf5d18" />

Tambahan:

while True:

            try:
                pili = int(input("pilih data yang mau di ubah : ")) - 1
                if 0 <= pili < len(rlog):
                    hari = input("Masukkan hari baru :")
                    lokasi = input("Masukkan lokasi baru :")
                    while True:
                        try:
                            jarak = float(input("Masukkan jarak baru :"))
                            if jarak < 0:
                                print("JARAK TIDAK VALID")
                                continue
                            break
                        except ValueError:
                            print("MASUKKAN ANGKA YANG BENAR")
                    rlog[pili] = (hari, lokasi, jarak)
                    print(" DATA BERHASIL DI UPDATE")
                    break
                else:
                    print("TIDAK ADA DATA")
            except ValueError:
                print("TIDAK ADA DATA")

 berfungsi agar sistem tidak crash dengan cara: jika user menginput value idx 4 misalnya, namun running log hanya memiliki 3 data, maka user akan kembali ke input value idx dari data. jika user input value selain angka pada input jarak, maka sistem akan kembali ke input jarak sampai user menginput jarak dengan format yang benar.
 
Output:

<img width="248" height="190" alt="TerUbah" src="https://github.com/user-attachments/assets/42f07bbe-3e2c-435a-b991-91d235f8e9bf" />

4. kode dibawah merupakan function yang dapat dipanggil lagi oleh barisan kode dibawahnya, berfungsi untuk menghapus data yang sudah ada.
<img width="369" height="204" alt="hapuscode" src="https://github.com/user-attachments/assets/4b23a0c5-cad8-4bed-b0a3-b42b67a54c85" />

Tambahan:

try:

            hapus = int(input("pilih data yang mau dihapus : ")) - 1
            if 0 <= hapus < len(rlog):
                rlog.pop(hapus)
            else:
                print("DATA TIDAK ADA")
        except ValueError:
            print("MASUKKAN ANGKA YANG BENAR")
 berfungsi agar sistem tidak crash dengan cara: jika user menginput value idx 2 misalnya, namun running log hanya memiliki 1 data, atau user menginput variabel misalnya a, maka user akan kembali ke menu utama.

 Output:

 <img width="190" height="360" alt="TerHapus" src="https://github.com/user-attachments/assets/73633be7-38cf-4ec5-a0ab-084944bc37f0" />

 5. kode dibawah merupakan function yang dapat dipanggil lagi oleh barisan kode dibawahnya, berfungsi untuk melihat data yang sudah ada.
<img width="349" height="109" alt="lihatcode" src="https://github.com/user-attachments/assets/4f956540-871c-4ab2-8845-69bdd426f167" />


  




  




