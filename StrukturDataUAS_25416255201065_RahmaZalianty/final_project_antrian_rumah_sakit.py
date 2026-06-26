import csv
from collections import deque

FILE_DATA = "pasien.csv"

class SistemAntrianRumahSakit:
    def __init__(self):
        self.pasien = {}
        self.antrian = deque()
        self.riwayat = []  # Stack
        self.load_data()

    def load_data(self):
        try:
            with open(FILE_DATA, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.pasien[row["id"]] = row
        except FileNotFoundError:
            with open(FILE_DATA, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id","nama","umur","jenis_kelamin","keluhan"])

    def save_data(self):
        with open(FILE_DATA, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["id","nama","umur","jenis_kelamin","keluhan"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for data in self.pasien.values():
                writer.writerow(data)

    # CREATE
    def tambah_pasien(self):
        pid = input("ID Pasien: ")
        if pid in self.pasien:
            print("ID sudah digunakan!")
            return
        self.pasien[pid] = {
            "id": pid,
            "nama": input("Nama: "),
            "umur": input("Umur: "),
            "jenis_kelamin": input("Jenis Kelamin: "),
            "keluhan": input("Keluhan: ")
        }
        self.save_data()
        print("Data berhasil ditambahkan.")

    # READ
    def tampilkan_pasien(self):
        print("\nDATA PASIEN")
        print("-"*70)
        for p in self.pasien.values():
            print(f"{p['id']} | {p['nama']} | {p['umur']} | {p['jenis_kelamin']} | {p['keluhan']}")

    # UPDATE
    def edit_pasien(self):
        pid = input("Masukkan ID Pasien: ")
        if pid not in self.pasien:
            print("Data tidak ditemukan.")
            return
        self.pasien[pid]["nama"] = input("Nama Baru: ")
        self.pasien[pid]["umur"] = input("Umur Baru: ")
        self.pasien[pid]["jenis_kelamin"] = input("Jenis Kelamin Baru: ")
        self.pasien[pid]["keluhan"] = input("Keluhan Baru: ")
        self.save_data()
        print("Data berhasil diperbarui.")

    # DELETE
    def hapus_pasien(self):
        pid = input("Masukkan ID Pasien: ")
        if pid in self.pasien:
            del self.pasien[pid]
            self.save_data()
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    # SEARCHING
    def cari_pasien(self):
        key = input("Cari Nama/ID: ").lower()
        ditemukan = False
        for p in self.pasien.values():
            if key in p["id"].lower() or key in p["nama"].lower():
                print(p)
                ditemukan = True
        if not ditemukan:
            print("Data tidak ditemukan.")

    # SORTING (Bubble Sort)
    def sorting_nama(self):
        data = list(self.pasien.values())
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j]["nama"].lower() > data[j+1]["nama"].lower():
                    data[j], data[j+1] = data[j+1], data[j]
        for p in data:
            print(f"{p['id']} | {p['nama']}")

    # QUEUE
    def tambah_antrian(self):
        pid = input("Masukkan ID Pasien: ")
        if pid in self.pasien:
            self.antrian.append(pid)
            print("Pasien masuk antrian.")
        else:
            print("ID tidak ditemukan.")

    def lihat_antrian(self):
        if not self.antrian:
            print("Antrian kosong.")
            return
        for i, pid in enumerate(self.antrian, start=1):
            print(f"{i}. {self.pasien[pid]['nama']}")

    def panggil_pasien(self):
        if not self.antrian:
            print("Antrian kosong.")
            return
        pid = self.antrian.popleft()
        self.riwayat.append(pid)
        print("Pasien dipanggil:", self.pasien[pid]["nama"])

    # STACK
    def lihat_riwayat(self):
        print("Riwayat Pasien Dipanggil")
        for pid in reversed(self.riwayat):
            print(self.pasien[pid]["nama"])

def main():
    app = SistemAntrianRumahSakit()

    while True:
        print("\n===== SISTEM ANTRIAN RUMAH SAKIT =====")
        print("1. Tambah Pasien")
        print("2. Lihat Data Pasien")
        print("3. Edit Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Cari Pasien")
        print("6. Urutkan Data Pasien")
        print("7. Tambah ke Antrian")
        print("8. Lihat Antrian")
        print("9. Panggil Pasien")
        print("10. Riwayat Pasien Dipanggil")
        print("11. Keluar")

        pilih = input("Pilih Menu: ")

        if pilih == "1":
            app.tambah_pasien()
        elif pilih == "2":
            app.tampilkan_pasien()
        elif pilih == "3":
            app.edit_pasien()
        elif pilih == "4":
            app.hapus_pasien()
        elif pilih == "5":
            app.cari_pasien()
        elif pilih == "6":
            app.sorting_nama()
        elif pilih == "7":
            app.tambah_antrian()
        elif pilih == "8":
            app.lihat_antrian()
        elif pilih == "9":
            app.panggil_pasien()
        elif pilih == "10":
            app.lihat_riwayat()
        elif pilih == "11":
            print("Terima kasih.")
            break
        else:
            print("Menu tidak valid.")

if __name__ == "__main__":
    main()
