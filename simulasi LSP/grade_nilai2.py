while True:
    name_siswa = input("Masuka Nama Anda : ")
    nilai_harian = int(input("Masukan Nilai Harian : "))
    nilai_uts = int(input("Masukan Nilai UTS : "))
    nilai_uas = int(input("Masukan Nilai UAS : "))
    nilai_akhir = int(nilai_harian*40+nilai_uts*30+nilai_uas*30)/100

    if nilai_akhir >= 85:
        predikat_nilai = 'Amat Baik'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
    
    elif nilai_akhir >= 75:
        predikat_nilai = 'Baik'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)

    elif nilai_akhir >= 65:
        predikat_nilai = 'Cukup'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)

    elif nilai_akhir >= 55:
        predikat_nilai = 'Kurang'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)

    else:    
        predikat_nilai = 'Kurang Sekali'
        print("Nama Lengkap Anda = ",name_siswa)
        print("Nilai Akhir Anda = ",nilai_akhir)
        print("Predikat Anda = ",predikat_nilai)
        
