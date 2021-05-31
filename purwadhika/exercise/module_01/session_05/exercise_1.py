# soal exercise 1 session 05

# loop drawing
# ***
# **
# *
# **
# ***

stars = ''
size = 9

for i in range(size):
    if i < 5:
        for j in range(5 - i):
            stars += '* '
        stars += '\n'
    else:
        for k in range(i - 3):
            stars += '* '
        stars += '\n'

print(stars)