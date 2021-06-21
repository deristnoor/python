# 8
# Buatlah sebuah program menu untuk menghitung beberapa rumus bangun ruang.  
# Ketika memasukan angka 1, akan menghitung rumus segitiga 
# Ketika memasukan angka 2, akan menghitung rumus persegi 
# Ketika memasukan angka 3 atau karakter lain, akan mengeluarkan output ‘Masukkan Inputan Yang Benar’ 

while (True):
    input_menu = input('''
Selamat datang

bentuk apa yang ingin dihitung?
1. menghitung luas segitiga
2. menghitung luas persegi

masukkan angka:
''')

    if input_menu == '1':
        print("luas segitiga")
        break
    elif input_menu == '2':
        print("luas persegi")
        break
    else:
        print("\nmasukkan inputan yang benar")