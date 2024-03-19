import random
import string
import os

# Daftar hari dalam seminggu
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]

# Memasukkan informasi mengenai mata pelajaran, guru, hari, dan jam
mata_pelajaran = {}
lanjut = True
while lanjut:
    print("Masukkan informasi mengenai mata pelajaran:")
    mapel = input("Mapel: ")
    guru = input("Guru: ")
    hari_kelas = input("Hari: ")
    jam_kelas = input("Jam: ")
    ruangan = input("Ruangan: ")
    
    # Membuat ID unik untuk setiap mata pelajaran
    id_mapel = ''.join(random.choices(string.ascii_uppercase, k=10)) + ''.join(random.choices(string.digits, k=10))

    # Membuat nama ruangan secara acak menggunakan os.urandom
    ruangan = "L" + str(random.randint(100, 999))
    
    # Menambahkan informasi ke dalam dictionary mata_pelajaran
    mata_pelajaran[id_mapel] = {"Mapel": mapel, "Guru": guru, "Hari": hari_kelas, "Jam": jam_kelas, "Ruangan": ruangan}

    # Memeriksa apakah pengguna ingin melanjutkan
    lanjut_input = input("Lanjut (y/t)? ")
    if lanjut_input.lower() != 'y':
        lanjut = False

# Menampilkan informasi mata pelajaran dengan format tabel
print("\nID\t\tMAPEL\t\t\tGURU\t\tHARI\t\tJAM\t\tRUANGAN")
for id_mapel, info in mata_pelajaran.items():
    print(f"{id_mapel}\t\t{info['Mapel']}\t\t\t{info['Guru']}\t\t{info['Hari']}\t\t{info['Jam']}\t\t{info['Ruangan']}")