# Soal exercise 3 session 05

# adalal lanjutan dari excercise 03 session 04
# dimana pada exercise ini akan menambahkan
# fitur stock

# jumlah stock masing-masing produk
stock_apel = 8
stock_jeruk = 7
stock_anggur = 3

# input daftar belanja
# apabila jumlah input lebih dari stock, maka akan meminta input kembali
while (True):
    jml_apel = int(input("Masukkan jumlah Apel: "))
    if jml_apel > stock_apel:
        print("Jumlah yang dimasukkan terlalu banyak")
    else:
        break

while (True):
    jml_jeruk = int(input("Masukkan jumlah Jeruk: "))
    if jml_jeruk > stock_jeruk:
        print("Jumlah yang dimasukkan terlalu banyak")
    else:
        break

while (True):
    jml_anggur = int(input("Masukkan jumlah Anggur: "))
    if jml_anggur > stock_anggur:
        print("Jumlah yang dimasukkan terlalu banyak")
    else:
        break

# daftar harga produk
hrg_apel = 10000
hrg_apel = 10000
hrg_jeruk = 15000
hrg_anggur = 20000

# perhitungan total harga masing-masing produk
total_hrg_apel = (jml_apel * hrg_apel) 
total_hrg_jeruk = (jml_jeruk * hrg_jeruk)
total_hrg_anggur = (jml_anggur * hrg_anggur)

# total belanja
total_belanja = total_hrg_apel + total_hrg_jeruk + total_hrg_anggur

# text yang akan muncul saat eksekusi program
txt = '''
Detail Belanja

Apel : {jumlah_apel} x {harga_apel} = {total_harga_apel}
Jeruk : {jumlah_jeruk} x {harga_jeruk} = {total_harga_jeruk}
Apel : {jumlah_anggur} x {harga_anggur} = {total_harga_anggur}

Total : {total}
'''

print(txt.format(
    jumlah_apel = jml_apel,
    harga_apel = hrg_apel,
    jumlah_jeruk = jml_jeruk,
    harga_jeruk = hrg_jeruk,
    jumlah_anggur = jml_anggur,
    harga_anggur = hrg_anggur,
    total_harga_apel = total_hrg_apel,
    total_harga_jeruk = total_hrg_jeruk,
    total_harga_anggur = total_hrg_anggur,
    total = total_belanja,
))

# input uang bayar
# fitur kembalian
# condition dimana uang yang dibayarkan berlebih, pas, dan kurang
while (True):
    uang_bayar = int(input("Masukkan jumlah uang : "))
    if uang_bayar < total_belanja:
        print("Transaksi anda dibatalkan\nuang yang dibayarkan kurang " + str(total_belanja - uang_bayar))
    elif uang_bayar > total_belanja:
        print("Terima kasih\n\nUang kembali anda : " + str(uang_bayar - total_belanja))
        break
    else:
        print("Terima Kasih")
        break


