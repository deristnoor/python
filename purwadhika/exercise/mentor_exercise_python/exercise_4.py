# 4. 
# input = '32.054,23'
# output = '32,054.23' (koma diganti titik, titik diganti koma)

# solution 1
input = '32.054,23'
input = list(input)
# output = print(input[:2] + ',' + input[3:6] + '.' + input[7:])
for i in range(len(input)):
    if input[i] == '.':
        input[i] = ','
    elif input[i] == ',':
        input[i] = '.'


print(''.join(input))

# solution 2
input = '32.054,23'
for i in input:
    if i == ".":
        print(",", end="")
    elif i == ",":
        print(".", end="" )
    else:
        print(i, end="")