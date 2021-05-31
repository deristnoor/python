# Soal exercise 3 session 04

# adalal lanjutan dari excercise 06 session 03
# dimana pada exercise ini akan menambahkan
# fitur uang yang dibayarkan dan uang kembali

# input daftar belanja
jml_apel = int(input("Masukkan jumlah Apel: "))
jml_jeruk = int(input("Masukkan jumlah Jeruk: "))
jml_anggur = int(input("Masukkan jumlah Anggur: "))

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
uang_bayar = int(input("Masukkan jumlah uang : "))

# fitur kembalian
# condition dimana uang yang dibayarkan berlebih, pas, dan kurang
if uang_bayar < total_belanja:
    print("Transaksi anda dibatalkan\nuang yang dibayarkan kurang " + str(total_belanja - uang_bayar))
elif uang_bayar == total_belanja:
    print("Terima kasih")
elif uang_bayar > total_belanja:
    print("Terima kasih\n\nUang kembali anda : " + str(uang_bayar - total_belanja))
else:
    print("Mohon periksa kembali uang yang dibayarkan")