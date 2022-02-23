#data collection
daftarMobil = [
        {'PLAT' : 'D 1234 AB',
        'MERK' : 'TOYOTA',
        'TYPE' : 'ALL NEW ALPHARD',
        'JENIS' : 'MPV',
        'TAHUN PRODUKSI' : '2020',
        'HARGA SEWA' : 3000000,
        'TRANSMISI' : 'MATIC',
        'TERSEDIA' : 'YA' },

        {'PLAT' : 'D 2345 CD',
        'MERK' : 'TOYOTA',
        'TYPE' : 'NEW AGYA GR',
        'JENIS' : 'LCGC',
        'TAHUN PRODUKSI' : '2018',
        'HARGA SEWA' : 600000,
        'TRANSMISI' : 'MANUAL',
        'TERSEDIA' : 'TIDAK' },

        {'PLAT' : 'D 3456 EF',
        'MERK' : 'HONDA',
        'TYPE' : 'CIVIC TYPE R',
        'JENIS' : 'SEDAN',
        'TAHUN PRODUKSI' : '2018',
        'HARGA SEWA' : 2000000,
        'TRANSMISI' : 'MATIC',
        'TERSEDIA' : 'TIDAK' },
        
        {'PLAT' : 'D 4567 FG',
        'MERK' : 'HONDA',
        'TYPE' : 'ALL NEW HONDA BRIO',
        'JENIS' : 'LCGC',
        'TAHUN PRODUKSI' : '2020',
        'HARGA SEWA' : 800000,
        'TRANSMISI' : 'MANUAL',
        'TERSEDIA' : 'ADA' },
        
        {'PLAT' : 'D 5678 HI',
        'MERK' : 'MERCEDES',
        'TYPE' : 'GLA CLASS',
        'JENIS' : 'SUV',
        'TAHUN PRODUKSI' : '2021',
        'HARGA SEWA' : 3500000,
        'TRANSMISI' : 'MATIC',
        'TERSEDIA' : 'ADA' },
        
        {'PLAT' : 'D 6789 JK',
        'MERK' : 'MERCEDES',
        'TYPE' : 'S-CLASS',
        'JENIS' : 'SEDAN',
        'TAHUN PRODUKSI' : '2020',
        'HARGA SEWA' : 4000000,
        'TRANSMISI' : 'MATIC',
        'TERSEDIA' : 'ADA' }]

#read data
#function untuk menampilkan seluruh data
def printData (i) :
    print('Mobil', i+1)
    print('PLAT : ', daftarMobil[i]['PLAT'])
    print('MERK : ', daftarMobil[i]['MERK'])
    print('TYPE : ', daftarMobil[i]['TYPE'])
    print('JENIS : ', daftarMobil[i]['JENIS'])
    print('TAHUN PRODUKSI : ', daftarMobil[i]['TAHUN PRODUKSI'])
    print('HARGA SEWA : ', daftarMobil[i]['HARGA SEWA'])
    print('TRANSMISI : ', daftarMobil[i]['TRANSMISI'])
    print('TERSEDIA : ', daftarMobil[i]['TERSEDIA'])
    print()

def seluruhData () :
    if (len(daftarMobil) == 0) :
        print ("Tidak ada data")
    else :
        for x in range (len(daftarMobil)) :
            printData (x)

#function untuk menampilkan data tertentu
def searchData(uid) :
    tandai = -1
    for x in range (len(daftarMobil)) :
        if (uid == daftarMobil[x]['PLAT']) :
            tandai = x
    return tandai

def dataTertentu () :
    uid = (input("Silahkan Masukkan Nomor Plat Mobil : ")).upper()
    lokasiindex = searchData(uid)
    if lokasiindex == -1 :
        print('')
        print('*Data tidak ditemukan*')
        print('')
    else :
        print('Mobil dengan Plat Nomor ', (uid), ' :')
        printData(lokasiindex)

#function untuk menampilkan menu report data mobil
def reportDataMobil () :
    i = 0
    while(i != 3) :
        print('\t\t\t Report Data Mobil \t\t\t\n')
        print('1. Report Seluruh Data \n2. Report Data Tertentu \n3. Kembali ke Menu Utama \n')
        i = int(input('Silahkan pilih Sub Menu Read Data [1-3] : '))
        print(" ")
        if (i == 3):
            break
        elif (i == 1) :
            seluruhData ()
        elif (i == 2) :
            dataTertentu ()


#create data
#function inputan untuk create data
def inputCreateData () :
    temp = input('Masukkan NOMOR PLAT : ').upper()
    if (searchData(temp) >= 0) :
        print ("*Data Sudah Ada*")
        return False
    else :
        varInputCreate = {
            'PLAT' : temp,
            'MERK' : input('Masukkan MERK : ').upper(),
            'TYPE' : input('Masukkan TYPE : ').upper(), 
            'JENIS' : input('Masukkan JENIS : ').upper(),
            'TAHUN PRODUKSI' : input('Masukkan TAHUN PRODUKSI : '),  
            'HARGA SEWA' : int(input('Masukkan HARGA SEWA (Nominal Angka) : ')),
            'TRANSMISI' : input('Masukkan TRANSMISI : ').upper(),
            'TERSEDIA' : input('Masukkan TERSEDIA : ').upper()}
        return varInputCreate

#funtion untuk menyimpan inputan create data
def simpanCreateData () :
    temp = inputCreateData()
    if ( temp == False) :
        print ("*Coba Ulangi*")
    else :
        simpan = input('Apakah data akan disimpan? (Y/N) : ').upper()
        if (simpan == 'Y') :
            daftarMobil.append(temp)
            print('Data Tersimpan')
        elif (simpan == 'N' ):
            print ("Input Batal")
        else :
            while(simpan != 'Y' ) : 
                simpan = input('Apakah data akan disimpan? (Y/N) : ').upper()
                if(simpan == 'Y') :
                    daftarMobil.append(temp)
                    print('*Data Tersimpan*')
                    break
                elif (simpan == 'N' ):
                    print ("*Input Batal*")
                    break
                else :
                    simpan = input('Apakah data akan disimpan? (Y/N) : ').upper()

#function untuk menampilkan menu create data
def menuTambahDataMobil () :
    tambah = 0
    while(tambah !=2 ) :
        print('\t\t\t Menambah Data Mobil \t\t\t\n')
        print('1. Tambah Data Mobil \n2. Kembali ke Menu Utama \n')
        tambah = int(input('Silahkan pilih Sub Menu Create Data [1-2] : '))
        print(" ")
        if (tambah == 2) :
            break
        elif (tambah == 1) :
            simpanCreateData ()
        else : 
            print('*Pilihan tidak tersedia, silahkan coba lagi* \n')


#update data
#function inputan untuk menyimpan inputan update data
def simpanUpdateData () :
    indexPlat = searchData (input('Masukan Nomor Plat Mobil : ').upper())
    if indexPlat == -1 :
        print('')
        print('*Data tidak ditemukan*')
        print('')
    else :
        printData (indexPlat)
        pilihan = input('Tekan Y untuk lanjut dan tekan N untuk cancel : ').upper() 
        if (pilihan == 'Y') :
            indexUpdate = input('Masukan Kolom yang ingin diedit : ').upper()
            if((indexUpdate == 'PLAT') or (indexUpdate == 'MERK') or (indexUpdate == 'TYPE') or (indexUpdate == 'JENIS')
            or (indexUpdate == 'TAHUN PRODUKSI') or (indexUpdate == 'TRANSMISI') or 
            indexUpdate == 'TERSEDIA') :
                temp = input('Input Value baru : ').upper()
                konfirmasi = input("Yakin akan di update Y/N ? ").upper()
                if (konfirmasi == 'Y') :
                    daftarMobil[indexPlat][indexUpdate] = temp
                    print('Data [', indexPlat, '] [',indexUpdate,'] berhasil di Update')
                elif (konfirmasi == 'N') :
                    print('Tidak Jadi Update')
                else :
                    while(konfirmasi != 'Y') :
                        konfirmasi = input("Yakin akan di update Y/N ? ").upper()
                        if (konfirmasi == 'Y') :
                            daftarMobil[indexPlat][indexUpdate] = temp
                            print('Data [', indexPlat, '] [',indexUpdate,'] berhasil di Update')
                            break
                        elif (konfirmasi == 'N') :
                            print('Tidak Jadi Update')
                            break
                        else :
                            print ("Pilihan salah coba lagi")
            elif (indexUpdate == 'HARGA SEWA') :
                temp = int(input('Input Value baru : '))
                konfirmasi = input("Yakin akan di update Y/N ? ").upper()
                if (konfirmasi == 'Y') :
                    daftarMobil[indexPlat][indexUpdate] = temp
                    print('Data [', indexPlat, '] [',indexUpdate,'] berhasil di Update')
                elif (konfirmasi == 'N') :
                    print('Tidak Jadi Update')
                else :
                    while(konfirmasi != 'Y') :
                        konfirmasi = input("Yakin akan di update Y/N ? ").upper()
                        if (konfirmasi == 'Y') :
                            daftarMobil[indexPlat][indexUpdate] = temp
                            print('Data [', indexPlat, '] [',indexUpdate,'] berhasil di Update')
                            break
                        elif (konfirmasi == 'N') :
                            print('Tidak Jadi Update')
                            break
                        else :
                            print ("Pilihan salah coba lagi")
            else :
                print ('*Kolom tidak tersedia*')
        elif (pilihan == 'N') :
            print('Update Batal')
        else :
            while(pilihan != 'Y' ) :
                pilihan = input('Tekan Y untuk lanjut dan tekan N untuk cancel : ').upper()
                if (pilihan == 'Y') :
                    indexUpdate = input('Masukan Kolom yang ingin diedit : ').upper()
                    if((indexUpdate == 'PLAT') or (indexUpdate == 'MERK') or (indexUpdate == 'TYPE') or (indexUpdate == 'JENIS')
                    or (indexUpdate == 'TAHUN PRODUKSI') or (indexUpdate == 'TRANSMISI') or 
                    indexUpdate == 'TERSEDIA') :
                        temp = input('Input Value baru : ').upper()
                        konfirmasi = input("Yakin akan di update Y/N ? ").upper()
                        if (konfirmasi == 'Y') :
                            konfirmasi = input("Yakin akan di update Y/N ? ").upper()
                            daftarMobil[indexPlat][indexUpdate] = temp
                            print('Data [', indexPlat, '] [',indexUpdate,'] berhasil di Update')
                            break
                        elif (konfirmasi == 'N') :
                            print('Tidak Jadi Update')
                            break
                        else :
                            while(konfirmasi != 'Y') :
                                if (konfirmasi == 'Y') :
                                    daftarMobil[indexPlat][indexUpdate] = temp
                                    print('Data [', indexPlat, '] [',indexUpdate,'] berhasil di Update')
                                    break
                                elif (konfirmasi == 'N') :
                                    print('Tidak Jadi Update')
                                    break
                                else :
                                    print ("Pilihan Salah Coba lagi")
                    elif (indexUpdate == 'HARGA SEWA') :
                        temp = int(input('Input Value baru : '))
                        konfirmasi = input("Yakin akan di update Y/N ? ").upper()
                        if (konfirmasi == 'Y') :
                            daftarMobil[indexPlat][indexUpdate] = temp
                            print('Data [', indexPlat, '] [',indexUpdate,'] berhasil di Update')
                        elif (konfirmasi == 'N') :
                            print('Tidak Jadi Update')
                        else :
                            while(konfirmasi != 'Y') :
                                konfirmasi = input("Yakin akan di update Y/N ? ").upper()
                                if (konfirmasi == 'Y') :
                                    daftarMobil[indexPlat][indexUpdate] = temp
                                    print('Data [', indexPlat, '] [',indexUpdate,'] berhasil di Update')
                                    break
                                elif (konfirmasi == 'N') :
                                    print('Tidak Jadi Update')
                                    break
                                else :
                                    print("pilihan salah coba lagi")
                elif (pilihan == 'N') :
                    print('Tidak jadi Update')
                    break
                else :
                    print('*Pilihan salah, coba lagi*')

#function untuk menampilkan menu update data
def menuDataUpdate () :
    perbarui = 0
    while(perbarui !=2 ) :
        print('\t\t\t Mengubah Data Mobil \t\t\t\n')
        print('1. Ubah Data Mobil \n2. Kembali ke Menu Utama \n')
        perbarui = int(input('Silahkan pilih Sub Menu Update Data [1-2] : '))
        print(" ")
        if (perbarui == 2) :
            break
        elif (perbarui == 1) :
            simpanUpdateData ()
        else : 
            print('Pilihan tidak tersedia, silahkan coba lagi \n')


#function inputan untuk menghapus data mobil
def hapusDataMobil () :
    indexPlat = searchData (input('Masukan Nomor Plat Mobil : ').upper())
    if indexPlat == -1 :
        print('')
        print('*Plat nomor tidak ditemukan*')
        print('')
    else :
        pilihan = input('Apakah data akan dihapus? (Y/N) : ').upper() 
        if(pilihan == 'Y') :
            del daftarMobil[indexPlat]
            print('*Data berhasil dihapus*')
        elif(pilihan == 'N') :  
            print ('Data tidak Terhapus')
        else :
            print('pilihan salah coba lagi')
            while(pilihan != 'Y') :
                pilihan = input('Apakah data akan dihapus? (Y/N) : ').upper()
                if (pilihan == 'Y') :
                    print('*Data berhasil dihapus*')
                    del daftarMobil[indexPlat]
                elif(pilihan == 'N') :
                    print ('Data tidak Terhapus')
                    break
                else :
                    print('pilihan salah coba lagi')
                                      
#function untuk menampilkan menu hapus data
def menuDataDelete () :
    hapus = 0
    while(hapus !=2 ) :
        print('\t\t\t Menghapus Data Mobil \t\t\t\n')
        print('1. Hapus Data Mobil \n2. Kembali ke Menu Utama \n')
        hapus = int(input('Silahkan pilih Sub Menu Hapus Data [1-2] : '))
        print(" ")
        if (hapus == 2) :
            break
        elif (hapus == 1) :
            hapusDataMobil ()
        else : 
            print('Pilihan tidak tersedia, silahkan coba lagi \n')


#function untuk menampilkan menu awal
def menuAwal () :
    i = 0
    while(i != 5) :
        print('\t\t\t DATA RECORD RENTAL MOBIL MINANGKABAU \t\t\t')
        print('1. Report Data Mobil \n2. Menambahkan Data Mobil \n3. Mengubah Data Mobil \n4. Menghapus Data Mobil \n5. Exit')
        i = int(input('Silahkan pilih Main Menu [1-5] : '))
        print (' ')
        if (i == 5):
            print("Thank You and Good Bye!!!")
            break
        elif (i == 1) :
            reportDataMobil()
        elif (i == 2) :
            menuTambahDataMobil()
        elif (i == 3) :
            menuDataUpdate ()
        elif (i == 4) :
            menuDataDelete ()
        else :
            print('*Pilihan yang anda masukkan salah*')
            print(' ')
menuAwal()

