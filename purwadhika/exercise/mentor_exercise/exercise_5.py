# 5.
# input: masukkan 4 angka: 1234
# output 3412 (buatlah solusi hanya dengan menggunakan operasi matematika)

# solution 1
x = int(input("masukkan 4 angka: "))
output = 3412 - x
print(x + output)

# soulution 2
x = input("masukkan 4 angka: ")
y = (int(x[2]) * 1000) + (int(x[3]) * 100) + (int(x[0]) * 10) + (int(x[1]) * 1)
print(y)