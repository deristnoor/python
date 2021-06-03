# 9
# input: Nama saya Rizal
# output amaN ayas laziR

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
