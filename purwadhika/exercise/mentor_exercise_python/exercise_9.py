# 9
# input: Nama saya Rizal
# output amaN ayas laziR

# solution 1
x = input("Masukkan input: ")
x = x.split(" ")

for i in x:
    if len(i) > 3:
        list=[]
        for char in i:    
            list.append(char)
        
        list.reverse()
        y = ''.join(list)
        print(y, end=" ")

    else:
        print(i, end=" ")

# solution 2
txt = input("Masukkan kalimat: ")
txt_split = txt.split(" ")
for word in txt_split:
    if len(word) > 3:
        char_list = list(word)
        char_list.reverse()
        join  = ''.join(char_list)
        print(join, end=" ")
    else:
        print(word, end=" ")