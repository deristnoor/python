# 6. 
# [12, 15, 1, 7, 4, 100]
# Buat algoritma untuk mencari angka tertinggi di dalam list tanpa menggunakan fungsi max atau sort

x = [12, 15, 1, 7, 4, 100]
max_val = x[0]
print(max_val)

for i in x:
    if i > max_val:
        max_val = i

print(max_val)
