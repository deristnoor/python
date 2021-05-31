# Soal exercise 04 session 03

# Saat ini, jumlah usian Andi dan Budi = 49 tahun
# dengan rasio usia Andi dan Budi = 0.4
# Berapa usia Andi dan Budi 2 tahun lagi?

# note:
# x = usia andi
# y = usia budi

# known
# x + y = 49
# x / y = 0.4

# x = 0.4 * y 
# (0.4 * y) + y = 49
# y = 49 / 1.4

y = int(49 / 1.4)
x = 49 - 35

txt1 = "Usia Andi sekarang adalah {} tahun\nUsia Budi sekarang adalah {} tahun"
print(txt1.format(x,y))

x = x + 2
y = y + 2

txt2 = "Usia Andi setelah 2 tahun adalah {} tahun\nUsia Budi setelah 2 tahun adalah {} tahun"
print(txt2.format(x,y))