# soal exercise 2 session 05

# loop drawing
#           *
#         * * *
#       * * * * * 
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * * 
#         * * *
#           *
#         

stars = ''
size = 18

for i in range(size):
    if i < 9:
       if i % 2 == 0 :
            if i < 9:
                for j in range(9 - i):
                    stars += ' '
            for k in range(i + 1):
                stars += '* '
            stars += '\n'
    else:
        if i % 2 == 0 :
            if i > 9:
                for j in range(i - 7):
                    stars += ' '
            for k in range(17 - i):
                stars += '* '
            stars += '\n'

print(stars)