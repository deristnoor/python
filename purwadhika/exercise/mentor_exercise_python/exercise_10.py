# 10
# Buat algoritma/fungsi untuk mencari berapa kali tiap kata muncul dalam 1 kalimat.

# contoh:

# kata = 'Aku baru makan nasi terus aku mau makan mie nanti malam'

# output: 
# Jumlah kata 'Aku' ada sebanyak 2
# Jumlah kata 'Baru' ada sebanyak 1
# Jumlah kata 'Makan' ada sebanyak 2
# Jumlah kata 'Terus' ada sebanyak 1
# Jumlah kata 'Mau' ada sebanyak 1
# Jumlah kata 'Mie' ada sebanyak 1
# Jumlah kata 'Nanti' ada sebanyak 1
# Jumlah kata 'Malam' ada sebanyak 1

# solution 1
def word_count(x):
    y = x.split(" ")
    z = []

    for i in y:
        b = i.capitalize()
        z.append(b)

    a = list(set(z))
    a.sort()

    for word in a:
        j = 0
        for k in z:
            if word == k:    
                j += 1
        print("jumlah kata {} ada sebanyak {}".format(word, j))
    return

x = 'Aku baru makan nasi terus aku mau makan mie nanti malam'
word_count(x)

# solution 2
def word_count(txt):
    txt_split = txt.split(" ")
    txt_capitalize = []
    for word in txt_split:
        txt_capitalize.append(word.capitalize())
    txt_filter = list(set(txt_capitalize))
    txt_filter.sort()
    for word in txt_filter:
        count = 0
        for word_check in txt_capitalize:
            if word == word_check:
                count += 1
        print("Jumlah kata '{}' ada sebanyak {}".format(word,count))
    return