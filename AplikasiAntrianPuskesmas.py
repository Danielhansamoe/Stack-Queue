# Nama Aplikasi "Aplikasi Antrian Puskesmas"
# Nama Kelompok :
# 1. Amirullah
# 2. Karolina
# 3. Zahra
# 4. Ripal


# AWAL
def menu():
    print(" =================================== ")
    print("     SELAMAT DATANG DI PUSKESMAS     ")
    print("              SEJAHTERA              ")
    print(" =================================== ")
    print("1. Lihat Antrian")
    print("2. Tambah Antrian")
    print("3. Status Antrian Terbaru")
    print("4. Hapus Antrian")
    print("5. Tambah Kapasitas Antrian")
    print("6. Keluar")
    print("")
    go = input("Pilihan Menu : ")
    pilihan(go)


# PILIHAN ANTRIAN
def pilihan(go):
    if go == "1":
        lihatAntri()
    elif go == "2":
        tambahAntri()
    elif go == "3":
        statusAntri()
    elif go == "4":
        hapusAntri()
    elif go == "5":
        kapasitasNew()
    elif go == "6":
        keluar()
    else:
        print("Pilihan Tidak Ada.")
        menu()


# CLASS ANTRIAN
class queue:
    # DEFINE AWAL INIT
    def __init__(self):
        self.size = 0
        self.current_size = 0
        self.data = []

    # UNTUK CEK ANTRIAN KOSONG
    def isempty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    # UNTUK TAMBAH KAPASITAS ANTRIAN
    def kapasitas(self):
        print("=== PERBARUI KAPASITAS ANTRIAN ===")
        n = int(input("Masukan kapasitas antrian terbaru : "))
        if self.current_size > n:
            print("Kapasitas antrian lebih kecil dari sebelumnya")
        else:
            self.size = n
            print("Kapasitas antrian telah diperbarui")
        menu()

    # UNTUK CEK ANTRIAN PENUH
    # Stack yang digunakan adalah isfull
    def isfull(self):
        if self.current_size == self.size:
            return True
        else:
            return False

    # UNTUK TAMBAH ANTRIAN
    def enqueue(self):
        print("=== Tambah Antrian ===")
        if self.size == 0:
            print("Antrian Belum Ada.")
            cek = input("Lanjut membuat antrian? (Y/N)?")
            cek = cek.upper()
            if cek == "Y":
                n = int(input("Masukan Kapasitas Antrian : "))
                self.size = n
                print("Antrian dengan kapasitas", n, "telah dibuat")
                menu()
            else:
                menu()
        elif self.isfull():
            print("Maaf Antrian Penuh.")
        else:
            databaru = input("Masukan data baru : ")
            databaru = databaru.upper()
            self.data.append(databaru)
            self.current_size = len(self.data)
            print()
            for i in range(self.size):
                print("     [%2d]       " % (self.size - i), end="")
            print()

            for i in range(self.size):
                print(" --------------- ", end="")
            print()

            jumlahkosong = self.size - self.current_size
            for i in range(self.size):
                if i < jumlahkosong:
                    print("     %10s " % (""), end="")
                else:
                    print("     %10s " %
                          (self.data[self.size - 1 - i]), end="")

            print()
            for i in range(self.size):
                print(" --------------- ", end="")
            print()

            print(databaru+" masuk ke dalam antrian.")
            print("Urutan : ", self.current_size)
            estimasi = (self.current_size)*15
            print("Estimasi : ", estimasi, "menit")

        menu()

    # UNTUK HAPUS ANTRIAN DARI YANG PERTAMA KALI MASUK
    def dequeue(self):
        if self.isempty():
            print("Antrian Kosong")

            menu()
        else:
            datakeluar = self.data.pop(0)
            self.current_size = len(self.data)
            print(" ---- TERIMA KASIH ----")
            print(datakeluar, "Telah keluar antrian")

            for i in range(self.size):
                print("     [%2d]       " % (self.size - i), end="")
            print()

            for i in range(self.size):
                print(" --------------- ", end="")
            print()

            jumlahkosong = self.size - self.current_size
            for i in range(self.size):
                if i < jumlahkosong:
                    print("     %10s " % (""), end="")
                else:
                    print("     %10s " %
                          (self.data[self.size - 1 - i]), end="")

            print()
            for i in range(self.size):
                print(" --------------- ", end="")
            print()

            print("Sisa antrian : ", self.current_size)
            print("Urutan : ", self.current_size)
            estimasi = (self.current_size)*15
            print("Estimasi Total: ", estimasi, "menit")

        menu()

    # UNTUK CEK STATUS ANTRIAN (CARI DATA ANTRIAN)
    def status(self):
        index = 0
        print(" === STATUS ANTRIAN ===")
        cari = input("Masukan Nama : ")
        item = cari.upper()
        for i in self.data:
            if item in i:
                index = self.data.index(item)
                break
            else:
                continue
        print()

        for i in range(self.size):
            print("     [%2d]       " % (self.size - i), end="")
        print()

        for i in range(self.size):
            print(" --------------- ", end="")
        print()

        jumlahkosong = self.size - self.current_size
        for i in range(self.size):
            if i < jumlahkosong:
                print("     %10s " % (""), end="")
            else:
                print("     %10s " %
                      (self.data[self.size - 1 - i]), end="")

        print()
        for i in range(self.size):
            print(" --------------- ", end="")
        print()

        c = index + 1
        print(item)
        print("Urutan ", c)
        estimasi = c * 15
        print("Estimasi : ", estimasi, "menit")

        menu()

    # UNTUK LIHAT DATA ANTRIAN ADA BERAPA BANYAK
    def lihat(self):
        print(" === ANTRIAN ===")
        if self.isempty():
            print("Antrian Kosong")
        else:
            for i in range(self.size):
                print("     [%2d]       " % (self.size - i), end="")
            print()

            for i in range(self.size):
                print(" --------------- ", end="")
            print()

            jumlahkosong = self.size - self.current_size
            for i in range(self.size):
                if i < jumlahkosong:
                    print("     %10s " % (""), end="")
                else:
                    print("     %10s " %
                          (self.data[self.size - 1 - i]), end="")

            print()

            for i in range(self.size):
                print(" --------------- ", end="")
            print()

            print("Kapasitas Antrian    :", self.size)
            print("Banyak Antrian       :", self.current_size)

            if self.isempty:
                print("Antrian Terdepan     : -")
                print("Antrian Terakhir     : -")
            else:
                print("Antrian Terdepan     :", self.data[0])
                print("Antrian Terakhir     :", self.data[self.current_size-1])

            print("Estimasi Total: ", self.current_size*15, "menit")

        menu()


def lihatAntri():
    q.lihat()


def tambahAntri():
    q.enqueue()


def statusAntri():
    q.status()


def hapusAntri():
    q.dequeue()


def kapasitasNew():
    q.kapasitas()


def keluar():
    print(" === TERIMA KASIH ===")


q = queue()
menu()
