import pwinput
from prettytable import PrettyTable
rlog = []
akun = {"username": "Rafi", "password": "123"}
def tambah_log():
    hari = input("Berlari di hari apa? : ")
    lokasi = input("Berlari dimana? : ")
    while True:
        try:
            jarak = float(input("Berapa kilometer kamu berlari? : "))
            if jarak < 0:
                print("JARAK LARI TIDAK VALID")
                continue
            break
        except ValueError:
            print("JARAK LARI HARUS BERUPA ANGKA")
    print("RUNNING LOG + 1")
    rdata = (hari, lokasi, jarak)
    rlog.append(rdata)
def ubah_log():
    if not rlog:
        print("TIDAK ADA DATA YANG BISA DI UBAH")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Hari", "Lokasi", "Jarak(km)"]
        for idx, data in enumerate(rlog, 1):
            table.add_row([idx, data[0], data[1], data[2]])
        print(table)
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
def hapus_log():
    if not rlog:
        print("TIDAK ADA DATA YANG BISA DIHAPUS")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Hari", "Lokasi", "Jarak(km)"]
        for idx, data in enumerate(rlog, 1):
            table.add_row([idx, data[0], data[1], data[2]])
        print(table)
        try:
            hapus = int(input("pilih data yang mau dihapus : ")) - 1
            if 0 <= hapus < len(rlog):
                rlog.pop(hapus)
            else:
                print("DATA TIDAK ADA")
        except ValueError:
            print("MASUKKAN ANGKA YANG BENAR")
def lihat_log():
    if not rlog:
        print("TIDAK ADA DATA")
    else: 
        table = PrettyTable()
        table.field_names = ["No", "Hari", "Lokasi", "Jarak(km)"]
        for idx, data in enumerate(rlog, 1):
            table.add_row([idx, data[0], data[1], data[2]])
        print(table)
while True:
    print("LOGIN RUNNING LOG APP")
    user = input("Username : ")
    pw = pwinput.pwinput("Password : ")
    role = "User" if (user == akun["username"] and pw == akun["password"]) else "viewer"
    print(f"Selamat datang, {user} Role Anda: {role.upper()}")
    while True:    
        print(f"MENU RUNNING LOG [{role.upper()}]")
        if role == "User":
            print("1. Tambah Running Log")
            print("2. Ubah Running Log")
            print("3. Hapus Running Log")
            print("4. Lihat Running Log")
            print("5. Log Out")
            print("6. Keluar")
        else:
            print("1. Lihat Log")
            print("2. Log Out") 
            print("3. Keluar") 
        pilih = input("Pilih menu : ")
        if role == "User":
            if pilih == "1":
                tambah_log()
            elif pilih == "2": 
                ubah_log()
            elif pilih == "3": 
                hapus_log()
            elif pilih == "4": 
                lihat_log()
            elif pilih == "5":
                print("ANDA TELAH LOG OUT")
                break
            elif pilih == "6":
                print("ANDA TELAH KELUAR")
                exit()      
            else: 
                print("PILIHAN TIDAK VALIS.")
        else:
            if pilih == "1": 
                lihat_log()
            elif pilih == "2":
                print("ANDA TELAH LOG OUT")
                break
            elif pilih == "3":
                print("ANDA TELAH KELUAR")
                exit()
            else: 
                print("PILIHAN TIDAK VALID.")