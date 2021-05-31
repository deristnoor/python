# soal exercise 5 session 06

my_fav_movie = set(input("Masukkan 5 film kesukaan anda dipisahkan dengan koma: ").split(','))
your_fav_movie = set(input("Masukkan 5 film kesukaan anda dipisahkan dengan koma: ").split(','))

matching_movie_set = my_fav_movie.intersection(your_fav_movie)

percentage = (len(matching_movie_set)/len(my_fav_movie)) * 100

txt = "Matching movie percentage are {}%"
print(txt.format(percentage))