# UAS_S1

#main.py
from model.daftar_nilai import *
from view.view_nilai import *

while True:
    c = input("\nA)dd, E)dit, S)earch, D)elete L)ist, Q)uit: ")

    if (c.lower() == 'a'):
        tambah_data()

    elif (c.lower() == 'e'):
        ubah_data()

    elif (c.lower() == 's'):
        cetak_hasil_pencarian()

    elif (c.lower() == 'd'):
        hapus_data()

    elif (c.lower() == 'l'):
        cetak_daftar_nilai()

    elif (c.lower() == 'q'):
        break

    else:
        print("Silahkan pilih menu yang tersedia!")
        
#daftar_nilai.py

from view.input_nilai import *

dataMhs = {}

def tambah_data():
    global dataMhs
    nama = input_nama()
    nim = input_nim()
    nilaiTugas = input_nilaiTugas()
    nilaiUts = input_nilaiUas()
    nilaiUas = input_nilaiUas()
    nilaiAkhir = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
    dataMhs[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
    print("\nData Berhasil Ditambahkan!")
    return dataMhs

def ubah_data():
    nama = input("Masukkan Nama: ")
    if nama in dataMhs.keys():
        nim           = input_nim()
        nilaiTugas    = input_nilaiTugas()
        nilaiUts      = input_nilaiUts()
        nilaiUas      = input_nilaiUas()
        nilaiAkhir    = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        dataMhs[nama]  = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
        print("\nData Berhasil Di Update!")
    else:
        print("Data tidak ditemukan!")

def hapus_data():
    nama = input("Masukkan Nama:  ")
    if nama in dataMhs.keys():
        del dataMhs[nama]
        print("Data",nama,"Telah dihapus!")
    else:
        print("Data Mahasiswa Tidak Ada".format(nama))
#input_nilai.py
def input_nama():
    global nama
    nama = input("Masukkan Nama        : ")
    return nama

def input_nim():
    global nim
    nim = input("Masukkan NIM         : ")
    return nim

def input_nilaiTugas():
    global nilaiTugas
    nilaiTugas = int(input("Masukkan Nilai Tugas : "))
    return nilaiTugas

def input_nilaiUts():
    global nilaiUts
    nilaiUts = int(input("Masukkan Nilai UTS   : "))
    return nilaiUts

def input_nilaiUas():
    global nilaiUas
    nilaiUas = int(input("Masukkan Nilai UAS   : "))
    return nilaiUas
    
#view_nilai.py
from model.daftar_nilai import *

def cetak_daftar_nilai():
    if dataMhs.items():
        print("╔═══════════════════════════════════════════════════════════════════════════════════════════╗")
        print("╠═══════════════════════════════════════ DAFTAR NILAI ══════════════════════════════════════╣")
        print("╠══════╦══════════════════════╦═══════════════╦══════════╦═════════╦═════════╦══════════════╣")
        print("║  No  ║         NAMA         ║      NIM      ║   TUGAS  ║   UTS   ║   UAS   ║ NILAI AKHIR  ║")
        print("╠══════║══════════════════════║═══════════════║══════════║═════════║═════════║══════════════╣")
        i = 0
        for x in dataMhs.items():
            i += 1
            print("║ {6:4} ║ {0:20s} ║ {1:13} ║ {2:8d} ║  {3:6d} ║ {4:7d} ║ {5:12.2f} ║ " 
                    .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("╚══════╩══════════════════════╩═══════════════╩══════════╩═════════╩═════════╩══════════════╝")
    else:
        print("╔═══════════════════════════════════════════════════════════════════════════════════════════╗")
        print("╠═══════════════════════════════════════ DAFTAR NILAI ══════════════════════════════════════╣")
        print("╠══════╦══════════════════════╦═══════════════╦══════════╦═════════╦═════════╦══════════════╣")
        print("║  No  ║         NAMA         ║      NIM      ║   TUGAS  ║   UTS   ║   UAS   ║ NILAI AKHIR  ║")
        print("╠══════╩══════════════════════╩═══════════════╩══════════╩═════════╩═════════╩══════════════╣")
        print("║                                 Tidak Ada Daftar Nilai                                    ║")
        print("╚═══════════════════════════════════════════════════════════════════════════════════════════╝")

def cetak_hasil_pencarian():
    nama = input("Masukkan Nama        : ")
    if nama in dataMhs.keys():
        print("╔════════════════════════════════════════════════════════════════════════════════════╗")
        print("╠═══════════════════════════════════ DAFTAR NILAI ═══════════════════════════════════╣")
        print("╠══════════════════════╦═══════════════╦══════════╦═════════╦═════════╦══════════════╣")
        print("║         NAMA         ║      NIM      ║   TUGAS  ║   UTS   ║   UAS   ║ NILAI AKHIR  ║")
        print("╠══════════════════════║═══════════════║══════════║═════════║═════════║══════════════╣")
        print("║ {0:20s} ║ {1:13} ║ {2:8d} ║  {3:6d} ║ {4:7d} ║ {5:12.2f} ║ " 
                .format(nama, dataMhs[nama][0], dataMhs[nama][1],dataMhs[nama][2], dataMhs[nama][3],dataMhs[nama][4]))
        print("╚══════════════════════╩═══════════════╩══════════╩═════════╩═════════╩══════════════╝")
    else:
        print("Datanya {0} Tidak Ada ".format(nama))
        
        
        
