# soal exercise 01 session 06

# find min and max value from a list

numbers = [41,5,1,3,89,32]
min_val = numbers[0]
max_val = numbers[0]

for i in numbers:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print(numbers)
print(min_val)
print(max_val)    

