# Soal exercise 3 session 06

# adalal lanjutan dari excercise 03 session 05
# dimana pada exercise ini akan menambahkan
# fitur menu

list_buah = [
    ['Apel', 20, 10000],
    ['Jeruk', 15, 15000],
    ['Anggur', 25, 20000],
]

cart = []

while(True):
    txt = '''
    Selamat datang di Pasar Buah

    List Menu :
    1. Daftar Buah
    2. Menambah Buah
    3. Menghapus Buah
    4. Membeli Buah
    5. Exit Program
    '''
    input_menu = input('''
    Selamat datang di Pasar Buah

    List Menu :
    1. Daftar Buah
    2. Menambah Buah
    3. Menghapus Buah
    4. Membeli Buah
    5. Exit Program
    
    Masukkan angka Menu yang dijalankan: '''
    )

    if input_menu == '1':
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(list_buah)):
            print('{}\t| {}  \t| {}\t| {}'.format(i, list_buah[i][0], list_buah[i][1], list_buah[i][2]))

    elif input_menu == '2':
        nama_buah = input("Masukkan nama buah: ")
        stock_buah = int(input("Masukkan stock buah: "))
        harga_buah = int(input("Masukkan harga buah: "))
        list_buah.append([nama_buah, stock_buah, harga_buah])
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(list_buah)):
            print('{}\t| {}  \t| {}\t| {}'.format(i, list_buah[i][0], list_buah[i][1], list_buah[i][2]))


    elif input_menu == '3':
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(list_buah)):
            print('{}\t| {}  \t| {}\t| {}'.format(i, list_buah[i][0], list_buah[i][1], list_buah[i][2]))
        index_buah = int(input("Masukkan index buah yang ingin dihapus: "))
        del list_buah[index_buah]
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(list_buah)):
            print('{}\t| {}  \t| {}\t| {}'.format(i, list_buah[i][0], list_buah[i][1], list_buah[i][2]))

    elif input_menu == '4':

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(list_buah)):
            print('{}\t| {}  \t| {}\t| {}'.format(i, list_buah[i][0], list_buah[i][1], list_buah[i][2]))
        while(True):
            index_buah = int(input("Masukkan index buah yang ingin dibeli: "))
            jml_buah = int(input("Masukkan jumlah yang ingin dibeli: "))
            if jml_buah > list_buah[index_buah][1]:
                print('Stock tidak cukup, stock {} tinggal {}'.format(list_buah[index_buah][0], list_buah[index_buah][1]))
            else:
                cart.append([list_buah[index_buah][0], jml_buah, list_buah[index_buah][2], index_buah])
            print('Cart: ')
            print('Nama  \t| Jumlah\t| Harga')
            for item in cart:
                print('{}\t| {}  \t| {}'.format(item[0], item[1], item[2]))
            checker = input('Mau beli yang lain? (y/t)')
            if checker == 't':
                break
        print('Daftar belanja: ')
        print('Nama  \t| Jumlah\t| Harga\t| Total Harga')
        total_harga = 0
        for item in cart:
            print('{}\t| {}  \t| {}\t| {}'.format(item[0], item[1], item[2], item[1] * item[2]))
            total_harga += item[1] * item[2]
        while(True):
            print('Total yang harus dibayar = {}'.format(total_harga))
            uang_bayar = int(input("Masukkan jumlah uang : "))
            if uang_bayar > total_harga:
                change = uang_bayar - total_harga
                print('Terimakasih \n\nUang kembali anda: {}'.format(change))
                for item in cart:
                    list_buah[item[3]][1] -= item[1]
                cart.clear()
                break
            elif uang_bayar == total_harga:
                print('Terima kasih')
                break
            else:
                print("Transaksi anda dibatalkan\nuang yang dibayarkan kurang " + str(total_harga - uang_bayar))


    elif input_menu == '5':
        break
    else:
        print("Angka menu hanya 1-5")

