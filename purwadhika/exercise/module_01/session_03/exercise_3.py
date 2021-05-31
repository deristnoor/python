# Soal exercise 03 session 03

# 485 hari.
# Nyatakan dalam tahun, bulan, minggu dan hari.
# *1 bulan =  30 hari, 1 tahun = 360 hari.

x = 485

# perhitungan tahun
tahun = x // 360

# perhitungan bulan
# sisa hari dari tahun // hari dalam 1 bulan
bulan = (x % 360) // 30

# perhitungan minggu
# sisa  hari dari bulan // hari dalam 1 minggu
minggu = ((x % 360) % 30) // 7

# perhitungan hari 
# sisa hari dari keseluruhan
hari = ((x % 360) % 30)

txt = "485 hari sama dengan {} tahun, {} bulan, {} minngu, {} hari"
txt = txt.format(tahun, bulan, minggu, hari)
print(txt)