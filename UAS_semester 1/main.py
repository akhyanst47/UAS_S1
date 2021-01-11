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